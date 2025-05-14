from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication
import logging

from serial import PortNotOpenError

from chipboard_configuration_software.command_generator.generate_command_string import generate_commands

logger = logging.getLogger(__name__)


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
