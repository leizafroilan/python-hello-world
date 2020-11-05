#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file
from loadfile import setdir
import argparse
import os


# Function to perform backup
def bkup():

    setdir()
    PATH = os.getcwd()

    nr = InitNornir("config.yaml")

    backup_files = nr.run(task=netmiko_send_command, command_string="show run")

    for host in backup_files:

        if not backup_files[host].failed:

            fname = "{}/{}-bkup.cfg".format(PATH, host)
            config = backup_files[host].result
            nr.run(
                task=write_file,
                content=config,
                filename=fname
            )

            print("Saved backup file on {}".format(fname))
        else:
            print("Error saving file for {}. Check {}/nornir.log".format(
                host, PATH
            ))


# Function for other cli commands
def other_cmd(cmd):

    setdir()

    nr = InitNornir("config.yaml")
    results = nr.run(task=netmiko_send_command, command_string=cmd)
    print_result(results)


if __name__ == "__main__":

    # To correctly parse argument
    # Example usage nornir-1 "show version"
    # To execute backup, nornir-1 backup
    parser = argparse.ArgumentParser(
        description="Pass cisco command as argument"
    )
    parser.add_argument("cmd", help="Pass cisco command as argument", type=str)
    args = parser.parse_args()

    if args.cmd == "backup":
        bkup()

    else:
        other_cmd(args.cmd)
