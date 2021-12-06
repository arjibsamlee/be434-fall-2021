#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-22
Purpose: concatenate a file
"""

import argparse
import os
import sys
import re

# pylint: disable=W0105,missing-function-docstring,unspecified-encoding,consider-using-with
# flake8: noqa


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='concatenate a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='one or more file names')

    parser.add_argument('-n',
                        '--number',
                        help='print line numbers',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=str,
                        default=sys.stdout)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """A file to concatenate files and print them"""

    args = get_args()

    filenames = args.file
    # numbers = args.number
    outfile = args.outfile

    cat = []
    tac = []

    # iterate over imputed files
    for filename in filenames:
        linenum = 1  # counter
        lines = filename.readlines()  # read lines of file

        # or each file get each line
        for line in lines:
            cat.append(line)

    for o in reversed(cat):
        tac.append(o.strip("\n"))

    if os.path.isfile(outfile):
            #print('is file'):
        f = open(outfile,"w")
        print("Output is in file:", outfile)
        for element in tac:
            element += "\n"
            f.write(element)

        f.close()
    elif outfile != sys.stdout:
        f = open(outfile,'x')
        print("Output is in file:", outfile)

        for element in tac:
            # print(element)
            f.write(element)

        f.close()
    else:
        print(*tac, sep="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
