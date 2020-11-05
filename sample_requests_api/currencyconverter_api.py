#!/usr/bin/env python3

import requests
import argparse

"""
usage: currency_converter.py [-h] [-b BASE_RATE]

Currency Converter

optional arguments:
  -h, --help            show this help message and exit
  -b BASE_RATE, --base_rate BASE_RATE
"""

parser = argparse.ArgumentParser(description="Currency Converter")
parser.add_argument("-b", "--base_rate", type=str, nargs="?", default="USD")
args = parser.parse_args()

key = "cf24195ebacde7115476ce57"

url = "https://v6.exchangerate-api.com/v6/" + key + "/latest/" + args.base_rate

print("Retrieving currencies using GET request - {}\n".format(url))

url_dict = requests.get(url).json()

try:
    print("Documentation: {}".format(url_dict["documentation"]))
    print("Last update in UTC: {}".format(url_dict["time_last_update_utc"]))
    print("Next update in UTC: {}".format(url_dict["time_next_update_utc"]))
    print("Base rate: {}\n".format(url_dict["base_code"]))

    rates = url_dict["conversion_rates"]

except KeyError:
    print("Currency not found\n")
    exit(code=1)

for k, v in rates.items():
    print("{}: {}".format(k, v))

print("\n\nDefault base rate is USD")
print(
    """You can change base rate from USD to other currencies.
Usage: currency_converter.py [-h] [-b BASE_RATE]
Example: currency_converter.py -b SGD\n\n"""
)
