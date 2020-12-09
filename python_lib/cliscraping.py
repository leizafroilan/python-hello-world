#!/usr/bin/env python3
import os
import netmiko
from loadfile import setdir


# Uses environment variables stored on ~/.bash_profile

uid = os.environ.get("RT_USERNAME")
pw = os.environ.get("RT_PASS")

# Calls function to set current working directory to txtfiles
setdir()

# Extracts device commands from commands file and stores to variable cmds

with open("commands") as f:
    cmds = f.read().strip().splitlines()


def automate(ipaddr):

    try:
        print("Connecting to {}".format(ipaddr))
        nc = netmiko.ConnectHandler(
            ip=ipaddr, username=uid, password=pw, device_type="cisco_ios"
        )  # Connects to devices
        for cmd in cmds:
            filename = (
                nc.base_prompt
                + "_"
                + cmd.strip().replace(" ", "_")
                + ".txt"
            )  # Creates a file
            with open(filename, "w") as outf:
                # Writes output to file
                outf.write("##########" + cmd + "##########\n")
                outf.write(nc.send_command(cmd) + "\n\n")
        print("{}: Completed configuration".format(ipaddr))
    except Exception as e:
        print("{} - {}".format(ipaddr, e))
