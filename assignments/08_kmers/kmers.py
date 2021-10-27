#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-13
Purpose: look for commmon words between files
"""

import argparse


# pylint: disable=W0105,too-many-locals


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    onefile = args.file1
    twofile = args.file2
    len_kmer = args.kmer

    # print('File 1 = "{}"'.format(onefile.name if onefile else ''))
    # print('File 2 = "{}"'.format(twofile.name if twofile else ''))

    oneset = set()
    twoset = set()

    onedict = {}
    twodict = {}

    onelist = []
    twolist = []

    for line in onefile.read().split():
        # print(line)
        for i in range(0, len(line)):
            # print( i)
            kmer = get_char(line, i, len_kmer)
            # print(kmer)
            if kmer is not None:
                oneset.add(kmer)
                onelist.append(kmer)
            i += 1
    # print('first set of kmers ', oneset)

    for line in twofile.read().split():
        # print(line)
        for i in range(0, len(line)):
            kmer = get_char(line, i, len_kmer)
            # print(kmer)
            if kmer is not None:
                twoset.add(kmer)
                twolist.append(kmer)
            i += 1
    # print('first set of kmers ', twoset)

    # oneset.remove(None)
    # twoset.remove(None)

    cset = oneset.intersection(twoset)
    # print(cset)

    # common = " ".join(str(e) for e in cset)
    # print("Kmers that are in common: ",common)

    for x in cset:
        # print('items of cset:',x)
        onenum = onelist.count(x)
        twonum = twolist.count(x)

        onedict.update({x: onenum})
        twodict.update({x: twonum})

        print(f'{x:10}{onenum:6}{twonum:6}')


# ----------------------------------------------------------------
def get_char(test_str, num_start, num_char):
    """get desired number of chars of a string"""
    ichi = ''
    num_end = num_start + num_char
    ichi = test_str[num_start:num_end]
    # print(ichi, 'characters collected')
    if len(ichi) != num_char:
        ichi = None

    # print('get kmer number of characters', ichi)
    return ichi


# --------------------------------------------------------------
if __name__ == '__main__':
    main()
