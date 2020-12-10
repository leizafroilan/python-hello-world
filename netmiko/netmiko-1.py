#!/usr/bin/env python3

import netmiko
import credentials
import os
from loadfile import setdir
import signal


# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Dictionary to build ConnectHandler parameters
host = {
        "device_type": "cisco_ios",
        "username": credentials.uid(),
        "password": credentials.pw()
        }

# Calls function to set current working directory to txtfiles
setdir()

# Extracts device list from H-list.txt file and stores to variable/list device
with open("H-list") as f:
    devices = f.read().strip().splitlines()

# Extracts device command from commands.txt file and stores to cmds
with open("commands") as f:
    cmds = f.read().strip().splitlines()

for device in devices:
    try:
        host["ip"] = device
        print("Connecting to {}".format(device))
        nc = netmiko.ConnectHandler(**host)  # Connects to devices
        for cmd_list in cmds:

            filename = (
                nc.base_prompt
                + "_"
                + cmd_list.strip().replace(" ", "_")
                + ".txt"
            )  # Creates a file
            print("Saving to {}/{}".format(os.getcwd(), filename))
            with open(filename, "w") as outf:
                # Writes output to file
                outf.write("##########" + cmd_list + "##########\n")
                outf.write(nc.send_command(cmd_list) + "\n\n")
    except Exception as e:
        print("{} - {}".format(device, e))
