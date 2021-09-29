#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-22
Purpose: concatenate a file
"""

import argparse
import os
import io
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='concatenate a file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        
                        nargs='+',
                        help='one or more file names')

    parser.add_argument('-n',
                        '--number',
                        help='print line numbers',                        
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    filenames = args.file
    numbers = args.number
    
    '''
    print(filenames)
    if numbers:
        print('True')
    '''
    for filename in filenames:
        linenum = 1        
        try:
            os.path.isfile(filename)
        except:
            print('No such file or directory: ',filename)
            
        else:
            f = open(filename,'r')
            lines = f.readlines()   
            for line in lines:

                if numbers:
                    print(str(linenum), " ", line)
                else:
                    print(line)
                linenum += 1

            




    


# --------------------------------------------------
if __name__ == '__main__':
    main()
