#!/usr/bin/env pthon3  

"""
Author:     Megan Kane
Class:      BE 534
Purpose:    Say Hello
"""
#   call functions

import argparse

#-------------------------------

def get_args():
    # pull te command line arguments

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()
#-------------------------------

def main():
    # define the main program

    args = get_args()
    print("Hello, " + args.name + '!')

#-------------------------------
if __name__ == '__main__':
    main()

