#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-20
Purpose: jump the five encryption
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='jump the five encryption',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='One argument to decrypt')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    nums = args.positional
    dcode = ''
    i = len(nums)

    enc =   dict([
        ('1', '9'),
        ('2', '8'),
        ('3', '7'),
        ('4', '6'),
        ('5', '0'),
        ('6', '4'),
        ('7', '3'),
        ('8', '2'),
        ('9', '1'),
        ('0', '5')
    ])
   
   # print(enc)
    for dcode in nums:
    #     if dcode in enc:
    #         print(enc[dcode], end = '')
    #     else:
    #         print(dcode, end = '')
        print(enc.get(dcode, dcode), end = '')
    print("")
   



# --------------------------------------------------
if __name__ == '__main__':
    main()
