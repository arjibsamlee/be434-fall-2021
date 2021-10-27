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
   
  parser.add_argument('-k',
                        '--kmer',
                        help='Number of characters in kmer',
                        metavar='KMER',
                        type=int,
                        default=3)    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    onefile = args.file1
    twofile = args.file2
    len_kmer = args.kmer

    print('File 1 = "{}"'.format(onefile.name if onefile else ''))
    print('File 2 = "{}"'.format(twofile.name if twofile else ''))

    oneset = set()
    twoset = set()
    
    onedict = {}
    twodict = {}
   

    for line in onefile.readline():
        print(line)
        for i in line:
            kmer = get_char(line, i, i + len_kmer)
            print(kmer)
            oneset.add(kmer)
            
     for line in twofile.readline():
        print(line)
        for i in line:
            kmer = get_char(line, i, i + len_kmer)
            print(kmer)
            twoset.add(kmer)
            
    print(oneset)
    print(twoset)

    cset = oneset.intersection(twoset)
    common = "\n".join(str(e) for e in cset)
    print("Kmers that are in common: ",common)
    
    for x in common:
        onenum = oneset.count(x)
        twonum = twoset.count(x)
        
        onedict.update(x, onenum)
        twodict.update(x, twonum)
        
        print(x, '       ', onenum, twonum, sep='   ', end='\n')
        
          
#----------------------------------------------------------------
def get_char(test_str, num_start, num_char):
    """get desired number of chars of a string"""
    ichi = ''
    num_end = num_start + num_char
    ichi = test_str[num_start:num_end]

    return ichi
  

# --------------------------------------------------------------
if __name__ == '__main__':
    main()

