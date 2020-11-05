#!/usr/bin/env python3

import requests
import argparse
import csv
import pandas as pd
from matplotlib import pyplot as plt
from loadfile import setdir


def graph(country):

    # Calls function to set current working directory to txtfiles
    setdir()

    country = country.upper()

    df = pd.read_csv("covid19.csv")

    # Converts date(string) to datetime object
    df["dates"] = pd.to_datetime(df["dates"])

    df.sort_values("dates", inplace=True)

    # Plots graph
    x = df["dates"]
    y1 = df["cases"]
    y2 = df["deaths"]
    y3 = df["recoveries"]

    plt.plot(x, y1, color="y", label="Cases")
    plt.plot(x, y2, color="r", label="Deaths")
    plt.plot(x, y3, color="g", label="Recoveries")
    plt.title("Covid19 Graph")
    plt.grid()

    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.show()


def listcountries():

    url = "https://api.covid19api.com/countries"

    source = requests.get(url)

    list_ = source.json()

    for line in list_:
        print("Country: {}, Slug: {}".format(line["Country"], line["Slug"]))


if __name__ == "__main__":

    total_cases_old = 0
    total_deaths_old = 0
    total_rec_old = 0

    # Calls function to set current working directory to txtfiles
    setdir()

    with open("covid19.csv", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["dates",
                             "cases",
                             "deaths",
                             "recoveries"])

    # Parse if correct argument passed. Type -s show to get list of list
    # Type -c [COUNTRY] to get country results
    # Usage: covid19_tracker.py -c Singapore, covid19_tracker.py -s show
    # country and show are optional arguments
    parser = argparse.ArgumentParser(description="Covid Cases")
    parser.add_argument(
        "-c",
        "--country",
        help="Pass a country(slug) as argument",
        type=str,
        nargs="?",
        default="Philippines",
    )
    parser.add_argument(
        "-s",
        "--list",
        help="Type 'show' to get list of available countries and exit",
        type=str,
        nargs="?",
        default="default",
    )
    args = parser.parse_args()

    if args.list == "show":
        listcountries()
        exit(0)
    elif args.list == "default":
        pass
    else:
        print("Invalid Argument, pass -h to get correct usage")
        exit(1)

    try:
        url_country = (
            "https://api.covid19api.com/total/dayone/country/" + args.country
        )
        url_base = requests.get(url_country)
        country = url_base.json()
        print("\nCountry: {}\n".format(args.country))

    except TypeError:
        print("Invalid Argument, pass -h to get correct usage")
        exit(1)

    for country_dict in country:

        try:
            total_cases = country_dict["Confirmed"]
            total_deaths = country_dict["Deaths"]
            total_rec = country_dict["Recovered"]

        except TypeError:
            exit(1)

        # Cases
        if total_cases == total_cases_old:  # means no new cases today
            new_cases = 0

        else:  # if there are new cases
            new_cases = total_cases - total_cases_old
            total_cases_old = total_cases

        # Deaths
        if total_deaths == total_deaths_old:  # means no new deaths today
            new_deaths = 0
            total__deaths_old = total_deaths
        else:  # if there are new deaths
            new_deaths = total_deaths - total_deaths_old
            total_deaths_old = total_deaths

        # Recovered
        if total_rec == total_rec_old:  # means no new recovered today
            new_rec = 0
            total_rec_old = total_rec
        else:  # if there are new recovered
            new_rec = total_rec - total_rec_old
            total_rec_old = total_rec

        datestr = country_dict["Date"]
        datestr = datestr.replace("T00:00:00Z", "")

        print("\nDate: {}".format(datestr))
        print("Total Cases: {}\nNew Cases: {}".format(total_cases, new_cases))
        print(
            "Total Deaths: {}\nNew Deaths: {}".format(total_deaths, new_deaths)
        )
        print(
            "Total Recoveries: {}\nNew Recoveries: {}".format(
                total_rec, new_rec
            )
        )
        print("Active Cases: {}".format(country_dict["Active"]))

        with open("covid19.csv", "a") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([datestr, new_cases, new_deaths, new_rec])

    graph(args.country)
