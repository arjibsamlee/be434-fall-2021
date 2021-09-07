#!/usr/bin/env python3  

"""
Author:     Megan Kane
Class:      BE 534
Purpose:    print greetings
Type:       Assignment 1
"""

import argparse

#-------------------------------

def get_args():
    # pull the command line arguments

    parser = argparse.ArgumentParser(description='Greetings and salutations')

    parser.add_argument('-g', '--greeting', metavar='greeting',
                        default='Howdy', help='the greeting used')
    parser.add_argument('-n', '--name', metavar='name',
                        default='Stranger', help='Name to greet')
    parser.add_argument('-e', '--excited', metavar='include exclaimation point',
                        default='.', help='punctuation to include')



    return parser.parse_args()
#-------------------------------

def main():
    ## define the main program

    args = get_args()
    print(args.greeting + ' ' + args.name + args.excited)

#-------------------------------
if __name__ == '__main__':
    main()

