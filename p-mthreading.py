#!/usr/bin/env python3

import time
import os
import signal
import argparse
from cliscraping import automate
from multiprocessing.dummy import Pool as ThreadPool


# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == "__main__":

    threads = []
    ip = []

    parser = argparse.ArgumentParser()
    parser.add_argument("threads_num", help="Number of thread pool", type=int)
    args = parser.parse_args()

    # Extracts devicelist from H-list.txt and stores in variable/list device
    with open("H-list") as f:
        devices = f.read().strip().splitlines()

    for device in devices:
        ip.append(device)

    start = time.perf_counter()

    # Executes multi-threading with thread pool
    threads = ThreadPool(args.threads_num)
    threads.map(automate, ip)
    threads.close
    threads.join

    finish = time.perf_counter()

    print("\n\nCheck output on {}".format(os.getcwd()))
    print("\n\nFinished in", round(finish - start, 3), "second(s)\n\n")
