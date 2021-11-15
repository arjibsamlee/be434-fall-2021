#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-11-15
Purpose: an assignemnt
"""

import argparse
import os

# pylint: disable=W0105,missing-function-docstring,unspecified-encoding,consider-using-with
# flake8: noqa

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='an assignemnt',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='input text or file')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    seqs = ''

    if os.path.isfile(args.text):
        # print("the file name is: ", args.text)
        seq = open(args.text).readlines()
        # print(seq)
        infile =[]

        for line in seq:
            line.strip('\n')
            # print(line)
            infile.append(rle(line))

        seqs = ''.join(infile)

    else:
        # print('the sequence was given as text', args.text)
        seqs = rle(args.text)


    # print("the translated sequnce is: ", seqs)
    print(seqs)


# ---------------------------------------------------
def rle(ujeni):

    final = ''
    lastchar = ''

    count = 1

    # print('entered rle')

    for n in ujeni:
        # print('in for loop')
        if n == lastchar:
            count +=1
            # print('if')
        elif count > 1:
            final += str(count)
            final += n
            count = 1
            # print('esleif')
        else:
            final += n
            count = 1
            # print('else')

        lastchar = n
    if count > 1:
        final += str(count)
    # print('the final string is: ', final)

    return final







# --------------------------------------------------
if __name__ == '__main__':
    main()
