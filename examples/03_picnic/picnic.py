#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-13
Purpose: Items for picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Items for picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')
   
    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Write out items for the picnic"""

    args = get_args()
    items = args.item
    num = len(items)
   
    
    if args.sorted:
        items.sort()


    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items [-1] = 'and ' + items [-1]
        bringing = ', ' .join(items)




    print('You are bringing {}.'.format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
