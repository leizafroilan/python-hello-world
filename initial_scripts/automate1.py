#!/usr/bin/env python3


import netmiko
from getpass import getpass

# Device IP addresses. Creates a list device = ['192.168.1.221', '192.168.1.222']
device = """
192.168.1.221
192.168.1.222
192.168.1.223
""".strip().splitlines()

devices = {"device_type": "cisco_ios"}

# Prompt for username/password
username = input("Username: ")
password = None

# Verify if password matches. Sets password to  None if  passwords dont match to repeat the loop
while not password:
    password = getpass()
    password1 = getpass("Re-type Password: ")
    if password != password1:
        print("Try again")
        password = None

# Assigns username and passwords completing the
# dictionary devices(ip:'x', device_type:'cisco_ios', username:'x', password:'x')
devices["username"] = username
devices["password"] = password

for x in device:

    try:
        devices["ip"] = x
        nc = netmiko.ConnectHandler(**devices)
        print(nc.send_command("show clock"))
    except (netmiko.ssh_exception.NetmikoAuthenticationException):
        print(x, "Authentication Failure\n")
    except (netmiko.ssh_exception.NetMikoTimeoutException):
        print(x, "Network Timeout\n")
    except Exception:
        print(x, "Unknown Error\n")
