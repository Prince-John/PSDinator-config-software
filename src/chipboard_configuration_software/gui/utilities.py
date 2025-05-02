import logging

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QCheckBox, QApplication, QSlider
from serial import PortNotOpenError

from chipboard_configuration_software.command_generator.commands.configuration_types.chipboard_config_types import \
    ChipboardConfigurationDict
from chipboard_configuration_software.command_generator.commands.configuration_types.literal_types import BoolStr, \
    ChipboardConfigurationDictKey
from chipboard_configuration_software.command_generator.generate_command_string import generate_commands

logger = logging.getLogger(__name__)


def camel_case_split(s):
    """https://stackoverflow.com/a/58996565"""
    idx = list(map(str.isupper, s))
    # mark change of case
    l = [0]
    for (i, (x, y)) in enumerate(zip(idx, idx[1:])):
        if x and not y:  # "Ul"
            l.append(i)
        elif not x and y:  # "lU"
            l.append(i + 1)
    l.append(len(s))
    # for "lUl", index of "U" will pop twice, have to filter that
    return [s[x:y] for x, y in zip(l, l[1:]) if x < y]


def split_camelcase_to_underscore(text):
    return "_".join(camel_case_split(text))


def remove_underscore(string, index):
    return string.split("_")[index]


def get_channel(checkbox):
    channel = int(remove_underscore(str(checkbox.objectName()), 1))

    return channel


def set_slider_silently(slider: QSlider, pos: int):
    slider.blockSignals(True)
    slider.setSliderPosition(pos)
    slider.blockSignals(False)


def set_checkbox_silently(checkbox: QCheckBox, state: BoolStr):
    checkbox.blockSignals(True)
    checkbox.setChecked(state == "True")
    checkbox.blockSignals(False)


def configure_chipboard(config_handler, uart_link, status_message, component: ChipboardConfigurationDictKey = None):
    command_dict = config_handler.get_changes()

    if not command_dict or (component and component not in command_dict):
        text = f"No changes to configure for {component}" if component else "No changes to configure"
        status_message.emit(text)
        logger.info(text)
        return

    message = "!"

    if component is not None:
        command_dict = {component: command_dict[component]}
        message = f" component: {component}!"

    commands = generate_commands(command_dict)

    # Track success and failure
    success_count = 0
    failures = []

    try:
        uart_link.send_stx()
        for command in commands:
            try:
                uart_link.send_CMD(command_string=command, message=f"Sending: {command}")
                success_count += 1

            except Exception as e:
                logger.warning(f"Command '{command[:-1]}' failed: {e}")
                status_message.emit(f"Configuration Warning! {e}")
                failures.append((command[:-1], str(e)))
                QApplication.processEvents()
                continue

        logger.info(f"Configured Chipboard{message}")

        total = len(commands)
        failure_count = len(failures)

        if success_count == total:
            config_handler.update_currently_loaded_chipboard_config(component=component)
            final_msg = f"All {total} commands configured successfully!"
            logger.info(final_msg)
            status_message.emit(final_msg)
        else:
            final_msg = f"{success_count}/{total} commands succeeded, {failure_count} failed."
            logger.warning(final_msg)
            status_message.emit(final_msg)

            # Show detailed window
            # show_failure_details(failures)

        uart_link.send_etx()

    except ConnectionRefusedError as e:
        logger.error(f"Unable to get into chipboard configuration mode! {e}")
        status_message.emit(f"Unable to get into chipboard configuration mode! {e}")
    except PortNotOpenError as e:
        logger.error(e)
        status_message.emit(f"Error: Device is not connected! {e}")

    except Exception as e:
        logger.error(f"Unexpected Exception: {e}")
        status_message.emit(f"Unexpected Exception: {e}")
