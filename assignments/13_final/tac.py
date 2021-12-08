#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-12-06
Purpose: Reverse of concatenating a file
"""


import argparse
import sys


# pylint: disable=W0105,no-else-break,missing-function-docstring,unspecified-encoding,consider-using-with
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


    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """A file to concatenate files and print them"""

    args = get_args()

    filenames = args.file
    outfile = args.outfile

    cat = []
    tac = []

    # iterate over imputed files
    for filename in filenames:
        lines = filename.readlines()  # read lines of file

        # or each file get each line
        for line in lines:
            # print('create cat')
            cat.append(line)

        for o in reversed(cat):
            # print('reverseing cat')
            tac.append(o)

        cat = []

    if outfile != sys.stdout:
        # f = open(outfile,"w")

        # print('Output is in file:', outfile)
        for element in tac:
            # print('in for statement')
            if element == '':
                # print('empty')
                break
            else:
                # print('not empty')
                # element += "\n"
                outfile.write(element)
                # f.write(element)

        # print('Output is in file: ', outfile.name, sep='')
        # f.close()

    else:
        print(*tac, sep="")

# --------------------------------------------------
if __name__ == '__main__':
    main()
