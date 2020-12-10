#!/usr/bin/env python3

import pandas as pd
import os
import signal
from loadfile import setdir
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_configure
from nornir.core.filter import F
from nornir_utils.plugins.functions import print_result
from seedconfig import load_seed, generate_seed
from nornirbackup import bkup


# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)


def push_config(task):

    setdir()

    df = pd.read_csv("seed.csv")
    df = df.loc[df["hostname"] == task.host.name]
    df.set_index("hostname", inplace=True)

    fname = "{}_ACL.cfg".format(df.loc[task.host.name, "site_id"])

    task.run(task=napalm_configure,
             replace=False,
             filename=fname,
             )


def run():

    nr = InitNornir("config.yaml")
    csr1000v = nr.filter(F(groups__contains="csr1000v"))
    results = csr1000v.run(task=push_config)
    print_result(results)
    input("\n\nPress Enter to continue")


if __name__ == "__main__":

    setdir()

    # Loops selection while user is not pressing CTRL+C
    while True:

        os.system("clear")

        select = input("""1. Load config file\n2. Convert config file to Cisco commands
3. Deploy config file to Cisco devices\n4. Backup running config\n""")

        # Calls load_seed function
        if select == "1":
            load_seed()

        # Calls generate_seed function
        elif select == "2":
            generate_seed()

        # Calls pushconfig and run functions
        elif select == "3":
            run()

        # Calls nornirbackup function
        elif select == "4":
            bkup()

        # Continues loop if input is invalid
        else:
            pass
