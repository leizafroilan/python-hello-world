#!/usr/bin/env python3

import yaml
import os
from jinja2 import Template
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir.core.filter import F


# Function to generate config file from jinja template
def interface_config():

    PATH = os.getcwd()

    file_yaml = os.path.join(PATH, "txtfiles/switch.yaml")
    file_temp = os.path.join(PATH, "templates/interface.j2")

    os.system("clear")

    # Reads jinja template
    with open(file_temp, "r") as f:
        temp = Template(f.read())

    # Reads config file
    with open(file_yaml, "r") as f:
        source = yaml.safe_load(f)

    # Loops until all hosts from file_yaml are read
    for host in source:

        interface_config = ""

        print(f"! Generated config for {host}")

        # Loops until all interfaces on each devices are read
        for k, v in source[host].items():

            # Renders template
            temp_config = temp.render(
                interface=k,
                desc=v["description"],
                enable=v["enable"],
                ip=v["ip"],
                mac=v["mac"]
                        )

            # Stores all interface config to variable interface_config
            interface_config += temp_config

        # Prints output for user review before pushing config to devices
        print(interface_config)

        fname = os.path.join(PATH, f"txtfiles/{host}.cfg")

        # Saves config to separate files on each devices
        with open(fname, "w") as outf:
            outf.write(interface_config + "\nend")


# Function to push config file generated from interface_config
# using nornir/napalm configure
def push_config(task):

    PATH = os.getcwd()
    fname = os.path.join(PATH, f"txtfiles/{task.host.name}.cfg")

    task.run(
            task=napalm_configure,
            replace=False,
            filename=fname
                )


# Function to display results - successful/failed
def display_results(results):

    for host in results:
        if not results[host].failed:
            print(f"{host} - Successfully deployed")
        else:
            print(f"{host} - Failed. Please check logs on {PATH}/nornir.log")


if __name__ == "__main__":

    PATH = os.getcwd()

    # Displays generated config from function interface_config
    interface_config()
    select = input("\nPush config to devices? [Y/N]")
    os.system("clear")

    if select == "Y" or select == "y":

        # Initializes nornir object
        nr = InitNornir(f"{os.path.join(PATH, 'txtfiles/config.yaml')}")
        # Filters only devices devices with csr1000v group from hosts.yaml file
        csr1000v = nr.filter(F(groups__contains="csr1000v"))
        # Runs nornir - logs in to each device and push config file
        results = csr1000v.run(task=push_config)

        # Calls display_results function
        display_results(results)

    else:
        # Exits code if Y/y is not selected
        print("Bye!")
        exit(0)
