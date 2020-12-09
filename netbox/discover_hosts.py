#!/usr/bin/env python3

import os
import threading
import queue
from jinja2 import Template
import netmiko


# Runs ping test to 192.168.1.x network
def discover(i, q3):

    if os.system(f"ping -c 1 192.168.10.{i}") == 0:
        q3.put(f"192.168.10.{i}")
    else:
        q3.put("")


# Creates host.yaml(used in nornir) and testbed.yaml(used in genie/pyats)
def testbed(_list):

    os.system("clear")

    testbed_temp = "/home/froi/DevNet/templates/testbed.j2"
    hosts_temp = "/home/froi/DevNet/templates/hosts.j2"
    testbed_configs = ""
    hosts_configs = ""

    path = os.environ.get("workdir")
    os.chdir(path)

    # Reads jinja template
    with open(testbed_temp, "r") as f:
        testbed = Template(f.read())
    with open(hosts_temp, "r") as f:
        hosts = Template(f.read())

    print("List of resolved devices\n------------------------")

    # Loops to all resolved devices using netmiko in connect function and
    # renders jinja template
    for device in _list:
        for k, v in device.items():
            print(f"{k:<17s} : {v:}")
            testbed_config = testbed.render(host=k, ip=v)
            testbed_configs += testbed_config + "\n"
            hosts_config = hosts.render(host=k, ip=v)
            hosts_configs += hosts_config + "\n"

    # Writes output to testbed.yaml
    with open("testbed.yaml", "w") as f:
        f.write("devices:" + "\n" + testbed_configs)

    # Writes output to hosts.yaml
    with open("hosts.yaml", "w") as f:
        f.write(hosts_configs)

    print(f"testbed.yaml and hosts.yaml are saved on {path}")


# Uses netmiko to check if it can connect to devices and stores hostnames
# Uses queue - q1 and q2 to track multi-threading output
def connect(hostname, q1, q2):

    device_dict = {}

    try:
        nc = netmiko.ConnectHandler(
                ip=hostname,
                username="admin",
                password="cisco",
                device_type="cisco_ios")

        device_dict[nc.base_prompt] = hostname
        q1.put(device_dict)
        q2.put(f"Resolved {hostname} to {nc.base_prompt}")

    except Exception as e:
        q1.put("")
        q2.put(f"{hostname} - Login Failed - {e}")


if __name__ == "__main__":

    threads = []
    threads1 = []
    device_list = []
    discovered_hosts = []
    q1 = queue.Queue()
    q2 = queue.Queue()
    q3 = queue.Queue()

    # Multi-threading to simultaneous ping sweep network 192.168.10.0/24
    for i in range(2, 253):
        t = threading.Thread(target=discover, args=(i, q3))
        t.start()
        threads1.append(t)

    for thread in threads1:
        thread.join()
        # Stores q3 to list - discovered_hosts
        discovered_hosts.append(q3.get())

    discovered_hosts = [str(x) for x in discovered_hosts if x]

    os.system("clear")

    # If no devices are discovered using ping sweep, program exits
    if len(discovered_hosts) == 0:
        print("No discovered devices")
        exit(0)

    print("Resolving hostnames and logging in to devices...")

    for host in discovered_hosts:

        # Multi-threading to simultaneously connect to all device_list
        # connect function uses netmiko
        t = threading.Thread(target=connect, args=(host, q1, q2))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
        # Stores q1 to list - device_list
        device_list.append(q1.get())
        # Prints q2 - "Resolved {hostname} to {nc.base_prompt}"
        print(q2.get())

    device_list = [x for x in device_list if x]

    # If netmiko is unable to connect to all devices
    if len(device_list) == 0:
        print("No resolved devices")
        exit(0)

    choice = input("\n\nCreate testbed/hosts.yaml for resolved hosts [Y/N]?")
    if choice.lower() == "y":
        testbed(device_list)
    else:
        print("Program ended with exit code 0")
        exit(0)
