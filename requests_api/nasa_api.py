#!/usr/bin/env python3

import requests
import argparse

"""
usage: sample.py [-h] [-s SEARCH]

NASA API - takes search string as argument

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        add search string as argument
"""

# Checks if correct argument is passed. Takes -s as argument
# Example: nasa_api -s "mars rover"
parser = argparse.ArgumentParser(
    description="NASA API - takes search string as argument"
)
parser.add_argument(
    "-s", "--search", help="add search string as argument", type=str
)
args = parser.parse_args()

# NASA API
url = "https://images-api.nasa.gov/search?"
param = {"q": args.search}

response = requests.get(url, params=param).json()

sources = response["collection"]["items"]

for source in sources:

    data = source["data"]
    href = source["href"]
    for d in data:

        # Loops on every data
        print(
            "\nTitle: {}\nDescription: {}\nDate Created:{}\n ".format(
                d["title"], d["description"], d["date_created"],
            )
        )

    # Gets all links from each data
    links = requests.get(href).json()
    for link in links:
        print("Links: {}".format(link))
