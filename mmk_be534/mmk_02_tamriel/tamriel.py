#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-22
Purpose: Provide informtion on Tamriel, its countries, cultures and lore
"""

import argparse
import pandas as pd

# pylint: disable=W0105,consider-using-in,line-too-long,missing-function-docstring,unspecified-encoding,consider-using-with
# flake8: noqa


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='provide informtion on Tamriel, its countries, cultures and lore',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-r',
                        '--request',
                        help='Type of information you are requesting about the Elder Scrolls Universe',
                        metavar='str',
                        nargs='?',
                        type=str,
                        default='all')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    requested = args.request
    # print(requested)
    datafile = "mmk_tamriel.csv" # this is the data file
    tamriel_data = pd.read_csv(datafile)

    typelist = []
    typelist = get_types(tamriel_data)

    if requested == 'all' or requested is None:
        print("Welcome to the Elder Scrolls Guide!")
        print(f"You can request information on {typelist}")
        print("just type -r followed by one of the keywords.")
    elif requested in typelist:
        req_items = get_items(requested, tamriel_data)
        print("You have asked for all the entries that are listed as", requested, ".")
        print(req_items)
    else:
        print("Not a valid request.")
        print(f"You can request information on {typelist}")
        print("just type -r followed by one of the keywords.")



def get_types(tamriel_panda):
    "This is grabbing the types of data available"
    datatypes = []

    headers = list(tamriel_panda.columns.values)

    firstheader = headers[0]

    datatypes = list(tamriel_panda[firstheader].unique())

    return datatypes


def get_items(searchterm, tamriel_panda):
    "This searches for all entries that are classified based on the search term."
    print("getting requested data")
    # print(tamriel_panda)

    items = ""

    headers = list(tamriel_panda.columns.values)

    firstheader = headers[0]

    items = tamriel_panda.loc[tamriel_panda[firstheader] == searchterm]

    return items

# --------------------------------------------------
if __name__ == '__main__':
    main()
