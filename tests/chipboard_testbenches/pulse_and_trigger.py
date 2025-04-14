"""
Pulses the AFG once and resets the oneshot trigger. Does not modify any other settings.

"""
from time import sleep
import sys

from tm_devices import DeviceManager, PYVISA_PY_BACKEND
from tm_devices.drivers import MDO3K
from src.chipboard_configuration_software.uart_link.utils import print_with_bars

if __name__ == "__main__":

    with DeviceManager(verbose=True) as dm:
        dm.visa_library = PYVISA_PY_BACKEND
        scope: MDO3K = dm.add_scope("10.229.115.112")
        scope.timeout = 100000
        scope.write("AFG:OUTPut:STATE 0")
        scope.write("AFG:TRIGger:SOUrce EXTernal")
        try:
            while True:
                input("Any key to reset scope and AFG")
                scope.write("AFG:OUTPut:STATE 1")
                scope.write("ACQuire:STATE OFF")
                scope.write("AFG:TRIGGER:INTERVAL 10")
                scope.write("ACQuire:STOPAfter SEQ")
                scope.write("ACQuire:STATE ON")
                sleep(3)
                print_with_bars("Scope Reset, sending Pulse!")
                scope.write("AFG:TRIGger FORCe")

        except KeyboardInterrupt:
            print("Exiting...")
            scope.write("AFG:OUTPut:STATE 0")
            scope.write("AFG:TRIGger:SOUrce INTERNal")
            sys.exit(0)
