#!/usr/bin/env python3

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file
from loadfile import setdir
import os


# Function to perform backup
if __name__ == "__main__":

    setdir()
    PATH = os.getcwd()

    nr = InitNornir("config.yaml")

    # Executes "show run" to all devices on hosts.yaml
    backup_files = nr.run(task=netmiko_send_command, command_string="show run")

    for host in backup_files:

        # If nornir successfully executes "show run"
        if not backup_files[host].failed:

            # Creates backup filename
            fname = f"{PATH}/{host}-bkup.cfg"

            # Show run result
            config = backup_files[host].result

            # Writes "show run" output to file using nornir
            nr.run(
                task=write_file,
                content=config,
                filename=fname
            )

            print(f"Saved backup file on {fname}")

        else:

            # If nornir is unable to execute "show run" on a device
            print(f"Error saving file for {host}. Check {PATH}/nornir.log")
