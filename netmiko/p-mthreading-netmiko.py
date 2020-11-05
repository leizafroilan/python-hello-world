#!/usr/bin/env python3

import time
import os
import signal
import argparse
from multiprocessing.dummy import Pool as ThreadPool
from cliscraping import automate


if __name__ == "__main__":

    threads = []
    ip = []

    # Catches keyboard interrupts
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Checks if correct argument is passed
    parser = argparse.ArgumentParser()
    parser.add_argument("threads_num", type=int, help="Number of threads")
    args = parser.parse_args()

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

    print("\n\nCheck the output on {}".format(os.getcwd()))
    print("\n\nFinished in", round(finish - start, 3), "second(s)\n\n")
