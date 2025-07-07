from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication
import logging

from serial import PortNotOpenError

from chipboard_configuration_software.command_generator.generate_command_string import generate_commands

logger = logging.getLogger(__name__)


class BaseCommandWorker(QObject):
    status_update = Signal(str)
    progress_update = Signal(int)

    def __init__(self, uart_link):
        super().__init__()
        self.uart_link = uart_link

    def _send_commands(self, commands: list[str]) -> tuple[int, int]:
        total = len(commands)
        success = 0

        try:
            self.uart_link.send_stx()

            for i, command in enumerate(commands, 1):
                try:
                    self.uart_link.send_CMD(command_string=command, message=f"Sending: {command}")
                    self.status_update.emit(f"✔️ Command sent: {command}")
                    success += 1
                except Exception as e:
                    msg = f"❌ Command failed: {command} — {e}"
                    self.status_update.emit(msg)
                    logger.warning(msg)

                self.progress_update.emit(int((i / total) * 100))
                QApplication.processEvents()

            self.uart_link.send_etx()
            return success, total

        except ConnectionRefusedError as e:
            logger.error(f"Unable to get into chipboard configuration mode! {e}")
            self.status_update.emit(f"Unable to get into chipboard configuration mode! {e}")

        except PortNotOpenError as e:
            logger.error(f"Device not connected: {e}")
            self.status_update.emit(f"Error: Device is not connected! {e}")

        except Exception as e:
            logger.exception("Unexpected Exception during command sending")
            self.status_update.emit(f"Unexpected Exception: {e}")

        return success, total


class ChipboardConfigurator(QObject):
    status_update = Signal(str)
    progress_update = Signal(int)
    config_done = Signal()
    partial_success = Signal(list)  # List[fails]

    def __init__(self, config_handler, uart_link, component=None):
        super().__init__()
        self.config_handler = config_handler
        self.uart_link = uart_link
        self.component = component

    def run(self):

        command_dict = self.config_handler.get_changes()

        if not command_dict or (self.component and self.component not in command_dict):
            text = f"No changes to configure for {self.component}" if self.component else "No changes to configure"
            self.status_update.emit(text)
            logger.info(text)
            self.config_done.emit()
            return

        message = f" component: {self.component}!" if self.component else "!"

        if self.component:
            command_dict = {self.component: command_dict[self.component]}

        commands = generate_commands(command_dict)
        success_count = 0
        failures = []
        total = len(commands)

        try:
            self.uart_link.send_stx()

            for i, command in enumerate(commands, 1):
                try:
                    self.uart_link.send_CMD(command_string=command, message=f"Sending: {command}")
                    logger.debug(f"Sent command :{command[:-1]}")
                    success_count += 1
                    self.status_update.emit(f"✔️ Command sent: {command}")
                except Exception as e:
                    logger.warning(f"Command '{command[:-1]}' failed: {e}")
                    self.status_update.emit(f"❌ Command failed: {command[:-1]} — {e}")
                    failures.append((command[:-1], str(e)))

                percent_done = int((i / total) * 100)
                self.progress_update.emit(percent_done)
                QApplication.processEvents()

            logger.info(f"Configured Chipboard{message}")

            if success_count == total:
                self.config_handler.update_currently_loaded_chipboard_config(component=self.component)
                self.status_update.emit(f"✅ All {total} commands succeeded.")
            else:
                summary = f"⚠️ {success_count}/{total} succeeded. {len(failures)} failed."
                logger.warning(summary)
                self.status_update.emit(summary)
                self.partial_success.emit(failures)

            self.uart_link.send_etx()

        except ConnectionRefusedError as e:
            logger.error(f"Unable to get into chipboard configuration mode! {e}")
            self.status_update.emit(f"Unable to get into chipboard configuration mode! {e}")

        except PortNotOpenError as e:
            logger.error(e)
            self.status_update.emit(f"Error: Device is not connected! {e}")

        except Exception as e:
            logger.error(f"Unexpected Exception: {e}")
            self.status_update.emit(f"Unexpected Exception: {e}")

        self.config_done.emit()


class ChipboardResetter(BaseCommandWorker):
    reset_done = Signal()
    reset_command_map = {"cfd": "CFD:RST:",
                         "psd": {"force": "PSD:RST:01",
                                 "digital": "PSD:RST:00",
                                 "all": "PSD:RST:"},
                         "all": "RST:"
                         }

    def __init__(self, uart_link, component: str = None, reset_type: str = None):
        super().__init__(uart_link)
        self.uart_link = uart_link
        self.component = "all" if component is None else component
        self.reset_type = "all" if reset_type is None else reset_type

    def run(self):

        command = self.reset_command_map[self.component]

        if isinstance(command, dict):
            command = command[self.reset_type]

        command = f"{command}\0"
        self.status_update.emit(f"🔄 Sending {self.reset_type} reset to {self.component}...")

        success, total = self._send_commands([command])

        if success == total:
            self.status_update.emit(f"✅ {self.component} reset complete.")
        else:
            self.status_update.emit(f"❌ {self.component} reset failed.")

        self.reset_done.emit()


def threaded_configure_chipboard(parent_ui, config_handler, uart_link, component=None) -> (
        QThread, ChipboardConfigurator):
    thread = QThread()
    worker = ChipboardConfigurator(config_handler, uart_link, component)
    worker.moveToThread(thread)
    logger.debug("IN threaded configure")
    worker.status_update.connect(parent_ui.status_message.emit)
    worker.progress_update.connect(parent_ui.progressBar.setValue)
    worker.partial_success.connect(parent_ui._on_chipboard_config_done)

    worker.config_done.connect(thread.quit)
    worker.config_done.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    thread.started.connect(worker.run)
    logger.debug("Starting Thread now!")
    return thread, worker


def threaded_reset_chipboard(parent_ui, uart_link, component: str = None, reset_type=None) -> \
        (QThread, ChipboardResetter):
    thread = QThread()
    worker = ChipboardResetter(uart_link, component, reset_type)
    worker.moveToThread(thread)
    logger.debug("IN threaded reset")
    worker.status_update.connect(parent_ui.status_message.emit)
    worker.progress_update.connect(parent_ui.progressBar.setValue)

    worker.reset_done.connect(thread.quit)
    worker.reset_done.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    thread.started.connect(worker.run)
    logger.debug("Starting Thread now!")
    return thread, worker
