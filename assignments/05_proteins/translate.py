#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-04
Purpose: translate a given DNA/RNA sequence to amino acids
"""

import argparse
# from pprint import pprint


# pylint: disable=W0105


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='translate a given DNA/RNA sequence to amino acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start of program"""
    # assign
    args = get_args()
    seq = args.sequence
    # codon = args.codons
    # output = args.outfile

    # print(args)

    codon_table = {}
    for line in args.codons:
        key, val = line.split()
        codon_table[key] = val

    # pprint(codon_table)

    k = 3
    protein = ''

    for codon in [seq[i:i+k] for i in range(0, len(seq) - k + 1)]:
        # print(codon_table.get(codon.upper(), '-'), end='')
        protein += codon_table.get(codon.upper(), '-')

    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()


# End file
