#!/usr/bin/env python3

import netmiko
import credentials
from loadfile import setdir

# Dictionary to build ConnectHandler parameters
devices = {"device_type": "cisco_ios"}
devices["username"] = credentials.uid()
devices["password"] = credentials.pw()

# Calls function to set current working directory to txtfiles
setdir()

# Extracts device list from H-list.txt file and stores to variable/list device
with open("H-list") as f:
    device = f.read().strip().splitlines()

# Extracts device commands from commands.txt file and stores to variable/list  cmds
with open("commands") as f:
    cmds = f.read().strip().splitlines()

for x in device:
    try:
        devices["ip"] = x
        print("Connecting to ", x)
        nc = netmiko.ConnectHandler(**devices)  # Connects to devices
        for cmd_list in cmds:
            print(nc.base_prompt, "\n", nc.send_command(cmd_list))
    except (netmiko.ssh_exception.NetmikoAuthenticationException):
        print(x, "Authentication Failure\n")
    except (netmiko.ssh_exception.NetMikoTimeoutException):
        print(x, "Network Timeout\n")
    except Exception:
        print(x, "Unknown Error\n")
