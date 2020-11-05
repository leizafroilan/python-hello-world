#!/usr/bin/env python3

import pandas as pd
import os
import time
from loadfile import setdir


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
    input("\n\nFinished in {} seconds. Press Enter to continue".format(round(end-start, 3)))

    os.system("clear")
