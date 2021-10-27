#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-09-15
Purpose: Sing Do Re Mi like Maria
"""

import argparse

# pylint: disable=W0105,consider-using-enumerate
# flake8: noqa


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing Do Re Mi like Maria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Main program: Sing like Maria von Trapp"""

    args = get_args()
    notes = args.positional
    trk = len(notes)

    lyrics = dict([
    ('Do', 'Do, A deer, a female deer'),
    ('Re', 'Re, A drop of golden sun'),
    ('Mi', 'Mi, A name I call myself'),
    ('Fa', 'Fa, A long long way to run'),
    ('Sol', 'Sol, A needle pulling thread'),
    ('La', 'La, A note to follow sol'),
    ('Ti', 'Ti, A drink with jam and bread')])

    # print(lyrics)
    # print(f'positional = "{notes}"')

    for trk in range(len(notes)):
        # print('start for loop')
        if notes[trk] in lyrics:
            print(lyrics[notes[trk]])
        else:
            print('I don\'t know "'+ notes[trk] + '"')

        trk -= 1


# --------------------------------------------------
if __name__ == '__main__':
    main()
