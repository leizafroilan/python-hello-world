#!/usr/bin/env python3

import netmiko
import credentials

# Device IP addresses. Creates a list device = ['192.168.1.221', '192.168.1.222', '192.168.1.223']

device = """
192.168.1.221
192.168.1.222
192.168.1.223
""".strip().splitlines()

# Dictionary to build ConnectHandler parameters
devices = {"device_type": "cisco_ios"}
devices["username"] = credentials.uid()
devices["password"] = credentials.pw()

for x in device:

    try:
        devices["ip"] = x
        nc = netmiko.ConnectHandler(**devices)
        print(nc.base_prompt, ":", x, ":", nc.send_command("show clock"))
    except (netmiko.ssh_exception.NetmikoAuthenticationException):
        print(x, "Authentication Failure\n")
    except (netmiko.ssh_exception.NetMikoTimeoutException):
        print(x, "Network Timeout\n")
    except Exception:
        print(x, "Unknown Error\n")
