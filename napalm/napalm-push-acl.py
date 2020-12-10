#!/usr/bin/env python3

import pandas as pd
import os
import signal
import time
from loadfile import setdir
from napalm import get_network_driver

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)


def load_seed():

    # Calls function to set current working directory to txtfiles
    setdir()

    os.system("clear")
    seed = []

    print("Type END to save and quit file\n")
    while True:
        _input = input("")
        # If input is END, breaks loop
        if _input == "END":
            break

        # Appends current input to new input on varible list - seed
        seed.append(_input)

    # Saves seed value to seed.txt
    with open("seed.txt", "w") as outf:
        for eachline in seed:
            outf.write("{}\n".format(eachline))

    os.system("clear")


def generate_seed():

    # Calls function to set current working directory to txtfiles
    setdir()

    os.system("clear")

    start = time.perf_counter()

    # Loads csv file
    df = pd.read_csv("new_file.csv")

    for index, eachline in enumerate(df["site_id"]):

        # Create str filename with site id as reference
        filename = "{}_ACL.cfg".format(eachline)

        # Catches error if file is not found
        # Current file will be renamed with .old extension
        try:
            os.rename(filename, "{}.old".format(filename))
        except Exception:
            pass

        # Converts seed file NETS variables to their equivalent IP from
        # new_file.csv
        with open("seed.txt", "r") as f:
            seed = f.read()
            seed = seed.replace("NETA.", df.loc[index, "neta"])
            seed = seed.replace("NETB.", df.loc[index, "netb"])
            seed = seed.replace("NETC.", df.loc[index, "netc"])

            # Saves variable seed to file named stored in variable filename
            with open(filename, "a") as outf:
                outf.write(seed)
        print("File saved on {}".format(os.path.join(os.getcwd(), filename)))

    end = time.perf_counter()
    input(
        "\n\nFinished in {} seconds. Press Enter to continue".format(
            round(end - start, 3)
        )
    )

    os.system("clear")


def run():

    # Calls function to set current working directory to txtfiles
    setdir()

    os.system("clear")

    start = time.perf_counter()

    # Loads csv file
    df = pd.read_csv("new_file.csv")

    # Loops to each host from new_csv.csv column "host"
    for index, eachline in enumerate(df["host"]):

        fname = "{}_ACL.cfg".format(df.loc[index, "site_id"])

        driver = get_network_driver("ios")
        np = driver(eachline, "admin", "cisco123")

        try:
            # Logs in to cisco ios devices using Napalm
            print("Connecting to {}".format(eachline))
            np.open()
            print("Deploying configuration to {}".format(eachline))
            # Pushes seed file to devices
            np.load_merge_candidate(filename=fname)
            np.commit_config()
            # Closes connection
            np.close()
            print("Successfully deployed configuration to {}".format(eachline))

        # Catches all errors and continues loop
        except Exception as e:
            print("{} - {}".format(eachline, e))
            continue

    end = time.perf_counter()
    input(
        "\n\nFinished in {} seconds. Press Enter to continue".format(
            round(end - start, 3)
        )
    )

    os.system("clear")


if __name__ == "__main__":

    os.system("clear")

    # Loops selection while user is not pressing CTRL+C
    while True:
        select = input(
            """1. Load config file\n2. Convert config file to Cisco commands
3. Deploy config file to Cisco devices\n"""
        )

        # Calls load_seed function
        if select == "1":
            load_seed()
        # Calls generate_seed function
        elif select == "2":
            generate_seed()
        # Calls run function
        elif select == "3":
            run()
        # Continues loop if input is invalid
        else:
            print("Invalid Input")
            pass
