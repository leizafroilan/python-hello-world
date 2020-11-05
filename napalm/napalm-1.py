#!/usr/bin/env python3

from napalm import get_network_driver
import json
import signal
import os
import loadfile


if __name__ == "__main__":


    # Catches keyboard interrupts
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Uses environment variables stored on ~/.bash_profile
    uid = os.environ.get("RT_USERNAME")
    pw = os.environ.get("RT_PASS")


    # Calls function to set working directory to txtfiles
    loadfile.setdir()

    while True:

        # Test if input to select device is valid
        try:
            hostname = loadfile.select_device()
        except KeyError:
            continue
        except ValueError:
            continue

        driver = get_network_driver("ios")
        cisco_ios = driver(hostname, uid, pw)

        print("Connecting to {}".format(hostname))

        # Test if Napalm can connect to device
        try:
            cisco_ios.open()

        except Exception as e:
            os.system("clear")
            print("{} - {}".format(hostname, e))
            input("\n\n<<<Press Enter to continue>>>")
            continue

        try:
            command = loadfile.select_command()

        except KeyError:
            continue
        except ValueError:
            continue

        # If/Else to check if command is valid
        try:
            if command == "get_facts":
                print(
                    "Output for host {} for command {}\n\n".format(
                        hostname, command
                    ),
                    json.dumps(cisco_ios.get_facts(), indent=3),
                )

            elif command == "get_interfaces":
                print(
                    "Output for host {} for command {}\n\n".format(
                        hostname, command
                    ),
                    json.dumps(cisco_ios.get_interfaces(), indent=3),
                )
            else:
                print("Command is invalid")

        except:
            continue

        input("\n\n<<<Press Enter to continue>>>")
