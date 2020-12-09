#!/usr/bin/env python3

import netmiko

# Device IP addresses. Creates a list device = ['192.168.1.221', '192.168.1.222']
device = """
192.168.1.221
192.168.1.222
""".strip().splitlines()

print(device)
devices = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "cisco",
}


for x in device:
    devices["ip"] = x
    nc = netmiko.ConnectHandler(**devices)  # Connects to devices
    print(nc.send_command("show clock"))
