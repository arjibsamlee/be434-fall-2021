#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-22
Purpose: Provide informtion on Tamriel, its countries, cultures and lore
"""

import argparse
import csv
import io
from tabulate import tabulate


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

    typelist = []

    if requested == 'all' or requested == None:
        print("Welcome to the Elder Scrolls Guide!")
        print(f"You can request information on {typelist}")
        print("just type -r followed by one of the keywords.")
    else:
        print("haven't built the rest yet")

    # print(f'You can request = "{requested}"')
    # print(f'int_arg = "{race_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
