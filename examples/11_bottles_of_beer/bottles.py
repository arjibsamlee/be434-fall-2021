#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-25
Purpose: 99 bottles of beer on the wall
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='99 bottles of beer on the wall',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--number',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=10)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    bottles = args.number

    if bottles < 1:
        sys.exit(f'--num "{args.number}" must be greater than 0')
    else:
        # print(f'number of bottles = "{bottles}"')
        for num in range(bottles, 0, -1):
            beerverse(num)


#---------------------------------------------------
def beerverse(num_verse):
    '''Bottles of beer song verse'''

    line_1 = ' of beer on the wall,\n'
    line_2 = ' of beer, \nTake one down, pass it around,\n'
    line_3 = ' of beer on the wall!\n'
    # line_4 = ' of beer on the wall!\n'
    line_5 = 'No more bottles of beer on the wall!\n'

    if num_verse == 1:
        tense = 'bottle'
        print(num_verse, ' ', tense, line_1, num_verse,  ' ', tense, line_2, line_5, sep='', end='\n')
    elif num_verse == 2:
        tense = 'bottle'
        print(num_verse,  ' bottles', line_1, num_verse,  ' ', tense, line_2, num_verse -1, ' ', tense, line_3, sep='', end='\n')
    else:
        tense = 'bottles'
        print(num_verse,  ' ', tense, line_1, num_verse,  ' ', tense, line_2, num_verse -1, ' ', tense, line_3, sep='', end='\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
