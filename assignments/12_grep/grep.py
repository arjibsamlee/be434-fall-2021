#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-11-17
Purpose: return lines with provided words.
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
        description='return lines with provided words.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pat = args.pattern
    files = args.file

    # findall in re look at regular expressions

    case = args.insensitive

    matches = ''


    for file in files:

        if len(files) > 1:
            # print(file.name, ':', sep='', end=' ')
            matches += file.name
            matches += ':'
            # print(matches)

        lines = file.readlines()

        # print(lines)
        matched = ''

        for line in lines:
            matched = ''
            if case and re.search(pat, line,re.IGNORECASE):
                # print(line, end='')
                matched += line
                # print(matches)
                # print('case insensitive')
            elif re.search(pat, line):
                # print(line, end='')
                matched += line
                # print(matches)
            else:
                # print('nomatch')
                pass
            if matched and len(files) > 1:
                # print(file.name, ':', sep='', end=' ')
                matches += file.name
                matches += ':'
                # print(matches)
            matches += matched

    print(matches)


# --------------------------------------------------
if __name__ == '__main__':
    main()
