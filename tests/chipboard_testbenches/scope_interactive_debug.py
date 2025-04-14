import sys

from tm_devices import DeviceManager, PYVISA_PY_BACKEND
from tm_devices.drivers import MDO3K
from src.chipboard_configuration_software.uart_link.utils import print_with_bars
"""
event # 21 -> 101.31 sec
event # 1017 -> 102.31 sec
#2008 -> 103.31
#3008 -> 104.31
#7008 -> 108.31
#10008 -> 111.31
#36017 -> 137.31
"""
try:
    with DeviceManager(verbose=True) as dm:
        dm.visa_library = PYVISA_PY_BACKEND
        scope: MDO3K = dm.add_scope("10.229.115.112")
        print_with_bars("Connected to Scope, interactive SCPI utility")

        while True:

            command = input("Enter command to send or ctrl+c to exit.\n")

            if command[-1] == '?':
                reply = scope.query(f"{command}")
                if len(reply) > 10:
                    print(f"Received: \n {reply[0:10]} ..<{len(reply)}>.. {reply[-10:]} ")
                else:
                    print(f"Received: \n {reply} ")
            else:
                scope.write(command)


except KeyboardInterrupt:
    print("Exiting...")
    sys.exit(0)
