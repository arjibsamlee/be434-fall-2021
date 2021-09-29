#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-27
Purpose: shout out the message given
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='shout out the message given',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,                        
                        help='Input string')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    message = args.text
    outfile = args.outfile

    
    #print(message)
    #
    if outfile:
        #print(outfile)
        f = open(outfile,'x')
        f.write(message)
    else:
        if os.path.isfile(message):
            #print('is file')
            m = open(message)
            print((m.read()).upper())
        else:
            print(message.upper())
   


# --------------------------------------------------
if __name__ == '__main__':
    main()
