#!/usr/bin/env python3

import hashlib
import itertools
import time
import argparse
import threading
import queue

def generate(string):
    result = hashlib.md5(string.encode()).hexdigest()
    print(result)


def crack(hash, seed, q):

    start = time.perf_counter()
    passwd = list(itertools.product(seed, repeat=4))

    for pw in passwd:
        result = hashlib.md5("".join(pw).encode()).hexdigest()
        passwd.remove(pw)
        print(f'{passwd.remove(pw)}************************')
        print("".join(pw))
        if result == hash:
            print(f'***{"".join(pw)}')
            end = time.perf_counter()
            print(f"Finished in {round(end-start, 2)}")
            q.put(pw)
            exit()



if __name__ == "__main__":

    q = queue.Queue()
    threads = []
    seed = "abcdefghijklmnopqrstuvwxyz1234567890"


    parser = argparse.ArgumentParser(description="Encrypt/Decrypt MD5 using 5-digit password")
    parser.add_argument(
            "-e",
            "--encrypt",
            help="encrypt MD5 hash",
            type=str,
            nargs="?",
                    )
    parser.add_argument(
            "-d",
            "--decrypt",
            help="decrypt MD5 hash",
            type=str,
            nargs="?",

        )
    args = parser.parse_args()

    if args.encrypt:
        generate(args.encrypt)
    elif args.decrypt:
        t1 = threading.Thread(target=crack, args=(args.decrypt, seed, q))
        t1.start()
        threads.append(t1)

        for thread in threads:
            thread.join()
            print(f'{"".join(q.get())}')
            print(thread)
            end = time.perf_counter()

    else:
        exit()
