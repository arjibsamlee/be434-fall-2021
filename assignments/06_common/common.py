#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-13
Purpose: look for commmon words between files
"""

import argparse


# pylint: disable=W0105


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='look for commmon words between files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    onefile = args.file1
    twofile = args.file2
    output = args.outfile

    # print('File 1 = "{}"'.format(onefile.name if onefile else ''))
    # print('File 2 = "{}"'.format(twofile.name if twofile else ''))

    oneset = set()
    twoset = set()

    for word in onefile.read().split():
        oneset.add(word)

    for word in twofile.read().split():
        twoset.add(word)

    # print(oneset)
    # print(twoset)

    cset = oneset.intersection(twoset)
    common = "\n".join(str(e) for e in cset)

    # print("words that are in common: ",common)

    if args.outfile:
        print(common, file=output)
        # print('in if')
    else:
        print(common, sep='\n')
        # print('in else')


# --------------------------------------------------
if __name__ == '__main__':
    main()
