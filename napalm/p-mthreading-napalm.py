#!/usr/bin/env python3

import pandas as pd
import os
import signal
import time
import argparse
from loadfile import setdir
from napalm import get_network_driver
from multiprocessing.dummy import Pool as ThreadPool
from seedconfig import load_seed
from seedconfig import generate_seed

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)


def run(ipaddr):

    # Calls function to set current working directory to txtfiles
    setdir()

    # To parse the correct file equivalent to the ip address
    df = pd.read_csv("new_file.csv")
    df = df.loc[df["host"] == ipaddr]
    df.set_index("host", inplace=True)
    fname = "{}_ACL.cfg".format(df.loc[ipaddr, "site_id"])

    driver = get_network_driver("ios")
    np = driver(ipaddr, "admin", "cisco123")

    try:
        print("Connecting to {}".format(ipaddr))
        # Logs in to cisco ios devices using Napalm
        np.open()
        print("Deploying configuration to {}".format(ipaddr))
        # Pushes seed file to devices
        np.load_merge_candidate(filename=fname)
        np.commit_config()
        # Closes connection
        np.close()
        print("Successfully deployed configuration to {}".format(ipaddr))

    # Catches all errors and continues loop
    except Exception as e:
        print("{} - {}".format(ipaddr, e))
        pass


if __name__ == "__main__":

    setdir()

    hosts = []

    os.system("clear")
    # Loads csv file
    df = pd.read_csv("new_file.csv")

    # Creates list to be used on multithreading
    for eachline in df["host"]:
        hosts.append(eachline)

    parser = argparse.ArgumentParser()
    parser.add_argument("threads_num", type=int, help="Number of threads")
    args = parser.parse_args()

    # Loops selection while user is not pressing CTRL+C
    while True:

        select = input(
            """1. Load config file\n2. Convert config file to Cisco commands
3. Deploy config file to Cisco devices\n"""
        )

        os.system("clear")

        # Calls load_seed function
        if select == "1":
            load_seed()
        # Calls generate_seed function
        elif select == "2":
            generate_seed()
        # Calls run function
        elif select == "3":
            start = time.perf_counter()
            threads = ThreadPool(args.threads_num)
            threads.map(run, hosts)
            threads.close
            threads.join
            end = time.perf_counter()
            input(
                "\n\nFinished in {} seconds. Press Enter to continue".format(
                    round(end - start, 3)
                )
            )
            os.system("clear")
        # Continues loop if input is invalid
        else:
            print("Invalid Input")
            pass
