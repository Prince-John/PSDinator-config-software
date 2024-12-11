import sys

from tm_devices import DeviceManager, PYVISA_PY_BACKEND
from tm_devices.drivers import MDO3K
from src.uart_link.utils import print_with_bars

try:
    with DeviceManager(verbose=True) as dm:
        dm.visa_library = PYVISA_PY_BACKEND
        scope: MDO3K = dm.add_scope("10.229.115.178")
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
