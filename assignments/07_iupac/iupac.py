#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-19
Purpose: Translate IUPAC encoded DNA to regular expression
"""

import argparse
import sys

# from pprint import pprint

# pylint: disable=W0105


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate IUPAC encoded DNA to regular expression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='SEQ',
                        nargs='+',
                        type=str,
                        help='A DNA sequence')

    parser.add_argument('-o',
                        '--outfile',
                        help='Location for output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=[sys.stdout])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """IUPAC decoding"""

    args = get_args()
    seq = args.sequence
    data = range(len(seq))

    is_file = 'no' if args.outfile == [sys.stdout] else 'yes'
    # print(args)
    # print(is_file)

    iupac_table = {}
    # iupac_codes = open('iupac_codes.txt', encoding='utf-8')

    with open('iupac_codes.txt', encoding='utf-8') as iupac_codes:
        for line in iupac_codes:
            key, val = line.split()
            iupac_table[key] = val

    # pprint(iupac_table)

    for index in data:
        protein = ''
        seq_now = seq[index]
        # print(seq_now)

        for i in seq_now:
            # print('in for loop')
            compare = iupac_table.get(i.upper())

            # print('compare this ' + i + ' to ' + compare)

            if i == compare:
                protein += compare
                # print('in if')
            else:
                protein += '[' + compare + ']'
                # print('in else')
        # print(seq_now + ' ' + protein)

        if is_file == 'yes':
            print(seq_now + ' ' + protein, file=args.outfile)

        else:
            print(seq_now + ' ' + protein)

    if is_file == 'yes':
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
