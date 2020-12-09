#!/usr/bin/env python3

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file
from loadfile import setdir
import os


def bkup():

    os.system("clear")

    setdir()
    PATH = os.getcwd()

    print("Performing backup...")
    nr = InitNornir("config.yaml")

    backup_files = nr.run(task=netmiko_send_command, command_string="show run")

    for each_host in backup_files:

        if not backup_files[each_host].failed:

            fname = "{}/{}-bkup.cfg".format(PATH, each_host)
            config = backup_files[each_host].result
            nr.run(
                task=write_file,
                content=config,
                filename=fname
            )

            print("Saved backup file on {}".format(fname))
        else:
            print("Error saving file for {}. Check {}/nornir.log".format(
                each_host, PATH
            ))
