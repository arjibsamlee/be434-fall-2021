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
   
   
    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get integers and add them together"""

    args = get_args()
    INT = args.INT
    num = len(INT)
    Total = 0
    trk = num
   

    
  #  if args.sorted:
   #     INT.sort()
    #numbers = ''
    for trk in range(num):
        if not type(int(INT[trk])) is int:
           print ("Only Integers Allowed")
        if trk > 0:
            Total = Total + int(INT[trk])
            numbers = ' + '.join(INT)
            trk = trk - 1
        else:
            Total = Total + int(INT[trk])
            



    print('You are adding {} = '.format(numbers) + str(Total))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
