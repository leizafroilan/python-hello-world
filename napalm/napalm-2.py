#!/usr/bin/env python3

from napalm import get_network_driver
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

    # Calls function to set current working directory to txtfiles
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

        loadYN = input(
            """Load old config or write new config or show
             running config <Old/New/Show> ?: """
        )
        loadYN = loadYN.lower()

        # Merge config written on old_config.cfg
        if loadYN == "old":
            os.system("clear")
            print("Loading  configuration")
            cisco_ios.load_merge_candidate(filename="old_config.cfg")
            diffs = cisco_ios.compare_config()
            # Calls function diff on loadfile to check if added config exists
            # If diffs length > 0, commits config, else, discards config
            loadfile.diff(diffs, cisco_ios)

        # Enables user to write commands and save it to new_config.cfg
        elif loadYN == "new":
            os.system("clear")
            loadfile.write_cmd()
            print("Saving to new_config.cfg")
            cisco_ios.load_merge_candidate(filename="new_config.cfg")
            diffs = cisco_ios.compare_config()
            # Calls function diff on loadfile to check if added config exists
            # If diffs length > 0, commits config, else, discards config
            loadfile.diff(diffs, cisco_ios)

        # Executes "show running-configuration"
        elif loadYN == "show":
            os.system("clear")
            print("Retrieving configuration for {}".format(hostname))
            config = cisco_ios.get_config()
            print(config["running"])
            input("\n\n<<<Press Enter to continue>>>")

        # Else, input is invalid and script returns to main selection
        else:
            continue
