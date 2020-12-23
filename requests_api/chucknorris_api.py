#!/usr/bin/env python3

import requests
import argparse
import os
import signal
import random

# Catches keyboard interrupts
signal.signal(signal.SIGPIPE, signal.SIG_DFL)
signal.signal(signal.SIGINT, signal.SIG_DFL)


def categories():

    url = "https://api.chucknorris.io/jokes/categories"

    source = requests.get(url).json()

    return source


if __name__ == "__main__":

    while True:

        os.system("clear")

        source = categories()
        rnd = random.choice(source)

        # def = random.choice()
        # Parse if correct argument passed. Type -s show to get list of list
        # Type -c [CATEGORY] to get category results
        # Usage: chucknorris.py -c science, chucknorris.py -s show
        # category and show are optional arguments
        parser = argparse.ArgumentParser(description="Chuck Norris Jokes")
        parser.add_argument(
            "-c",
            "--category",
            help="Pass a category as argument",
            type=str,
            nargs="?",
            default=rnd,
        )
        parser.add_argument(
            "-s",
            "--list",
            help="Type 'show' to get list of available categories and exit",
            type=str,
            nargs="?",
            default="default",
        )
        args = parser.parse_args()

        if args.list == "show":
            source = categories()
            print("List of categories: {}".format(source))
            exit(0)
        elif args.list == "default":
            pass
        else:
            print("Invalid Argument, pass -h to get correct usage")
            exit(1)

        if args.category is None:
            print("Invalid Argument, pass -h to get correct usage")
            exit(1)
        else:
            pass

        myheaders = {"content-type": "application/json"}
        param = {"category": args.category}

        url = "https://api.chucknorris.io/jokes/random?"

        try:
            source = requests.get(url, params=param, headers=myheaders).json()

            print(
                "Category: {}\nCreated at: {}\nURL: {}\nJoke: {}".format(
                    source["categories"],
                    source["created_at"],
                    source["url"],
                    source["value"],
                )
            )

        except KeyError:
            print("Invalid Argument, pass -h to get correct usage")
            exit(1)

        input("\n\nPress Enter to get another joke(CTRL+C to exit)")
