#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-04
Purpose: translate a given DNA/RNA sequence to amino acids
"""

import argparse
import os
from random import sample
import sys
import linecache

# pylint: disable=W0105

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='translate a given DNA/RNA sequence to amino acids',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein',
                        metavar='str',
                        help='DNA/RNA sequence')


    parser.add_argument('-c',
                        '--condonfile',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
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
    protein_in  = args.protein
    codon       = args.condonfile
    output      = args.outfile

    testfile = temp_file(codon)
    file_length = file_lines(testfile)

    sample = ''


    # print(f'protein_in = "{protein_in}"')
    # print('codonfile = "{}"'.format(codon.name if codon else ''))
    # print('file_arg = "{}"'.format(output.name if output else ''))
     # print('the codon file is', file_length, 'lines long.')
     # print('The first 3 digits of the input are:', get3(protein_in,0), '')

    j = 0 # counter for the section of the DNA/RNA sequence

    while j < len(protein_in):
        sample = get3(protein_in,j)
        sample = sample.upper()
        #print('starting at letter', str(j), 'the next 3 letters of the sequence are:', sample)
        #print(infile_check(testfile,sample))
        output.write(infile_check(testfile,sample))

        j += 3



#---------------------------------------------------
def temp_file(filename):
    temp = open('temp.txt','w+')
    for i in filename:
        temp.write(i)
       #print('in temp file test')
    temp.close()

    return ('temp.txt')

#---------------------------------------------------
def get3(test_str, num_start):
    twa = ''
    num_end = num_start+3
    twa = test_str[num_start:num_end]

    return twa

#---------------------------------------------------
def file_lines(filename):

    num_lines, num_words, num_bytes = 0, 0, 0
    for line in filename:
        num_lines += 1
        num_bytes += len(line)
        num_words += len(line.split())

    return num_lines


#---------------------------------------------------

def infile_check(filename,testfile):
    x = open(filename,'r')
    for i in x:
        #print(i)
        sample_test = i[0:3]
        # print(sample_test)
        if testfile == sample_test:
            return(i[4])

    x.close()
    return('-')




# --------------------------------------------------
if __name__ == '__main__':
    main()
