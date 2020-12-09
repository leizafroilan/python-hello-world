#!/usr/bin/env python3


import threading
import time
from cliscraping import automate
import signal
from loadfile import setdir
import os

if __name__ == "__main__":

    threads = []

    # Catches keyboard interrupts
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Calls function to set current working directory to txtfiles
    setdir()


    # Extracts device list from H-list.txt and stores in variable/list device
    with open("H-list") as f:
        devices = f.read().strip().splitlines()

    start = time.perf_counter()

    for device in devices:

        # Executes multi-threading
        t = threading.Thread(target=automate, args=(device,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()


    print("\n\nCheck output on {}".format(os.getcwd()))
    print("\n\nFinished in", round(finish - start, 3), "second(s)")
