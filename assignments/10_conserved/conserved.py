#!/usr/bin/env python3
"""
Author : Megan Kane <aribsamlee@yahoo.com>
Date   : 2021-11-08
Purpose: compare 2 sequences
"""
import argparse


# pylint: disable=W0105,missing-function-docstring,unspecified-encoding,consider-using-with
# flake8: noqa
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I dont know yet',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filename = args.file

    outline = ''
    lines = []

    reader = filename.readlines()

    for rec in reader:
        print(rec, end='')
        lines.append(rec)

    # print(lines)

    samechars = list(lines[0])

    # print("samechars = ", samechars)

    for line in lines:
        i = 0
        while i <= len(samechars) -1:
            # print("Is ", line[i], "equal to ", samechars[i] )
            if line[i] != samechars[i]:
                # print(samechars[i])
                samechars[i] = 'X'
            i += 1
    #  print("samechars = ", samechars)

    for c in samechars:
        if c == '\n':
            outline += ''
        elif c != 'X':
            outline += '|'
            # print('not same')
        else:
            outline += c
            # print('same')

    print(outline)



# --------------------------------------------------
if __name__ == '__main__':
    main()
