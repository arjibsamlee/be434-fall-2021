#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-13
Purpose: addition display
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='addition display',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('INT',
                        metavar='int',
                       nargs='+',
                        help='integers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get integers and add them together"""

    args = get_args()
    INT = args.INT
    num = len(INT)
    Total = 0
    trk = num
   

    

    numbers = ''
    for trk in range(num):
        try: 
            not type(int(INT[trk])) is int

        except:
            print ("usage: Only Integers Allowed")
        if trk > 0:
            Total = Total + int(INT[trk])
            numbers = ' + '.join(INT)
            trk = trk - 1
        else:
            Total = Total + int(INT[trk])
            numbers = ''.join(INT)
            



    print('{} = '.format(numbers) + str(Total))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
