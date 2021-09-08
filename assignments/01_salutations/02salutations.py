#!/usr/bin/env python3
"""
Author : Megan Kane
Date   : 20210908
Purpose: In class settup of the file
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='testingsetupfile',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
    parser.add_argument('-g',
                        '--greeting',
                        help='greeting to use',
                        metavar='greeting',
                        default='Moni')

    parser.add_argument('-n',
                        '--name',
                        help='name to greet',
                        metavar='name',
                        
                        default= 'Zungu')

    parser.add_argument('-e',
                        '--excited',
                        help='will ithave an !',
                        metavar='excited',                        
                        default= '.')

   
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
   
    print(args.greeting + ' ' + args.name + args.excited)



# --------------------------------------------------
if __name__ == '__main__':
    main()
