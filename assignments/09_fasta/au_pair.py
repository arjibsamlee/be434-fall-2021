#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-27
Purpose: I don't know yet
"""

import argparse
import os

from Bio import SeqIO


# pylint: disable=W0105,missing-function-docstring,unspecified-encoding,consider-using-with
# flake8: noqa
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I dont know yet',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')


    '''args = parser.parse_args()
    print ('filenames', name(args.file))
    filenames = []

    for _ in args.file:
        filenames = os.path.basename(args.file)
        print('filenames so far:', filenames)
    # return args '''
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filenames = args.file
    directory = args.outdir

    # parentdir = os.getcwd()

    # outpath = os.path.join(parentdir,directory.name)

    # print(directory.name, outpath)

    if os.path.exists(directory) is not True:
        os.makedirs(directory)
        # print("new directory:",outpath)

    for fh in filenames:
        # print(_)
        split_biofile(fh, directory)

    print('Done, see output in "', directory,'"', sep="")


# ---------------------------
def split_biofile(filename, out):
    list1 = []
    list2 = []

    count = 1

    reader = SeqIO.parse(filename, 'fasta')

    # get each record. Put the even into list2 and the odd into list1
    for rec in reader:
        # print('ID :', rec)
        # print('Seq:', str(rec.seq))
        if count % 2 == 0:
            list2.append(rec)
        else:
            list1.append(rec)

        count += 1

    # get file name and extention
    f_name, f_ext = os.path.splitext(os.path.basename(filename.name))

    file1_name = os.path.join(out, f_name + "_1" + f_ext)
    file2_name = os.path.join(out, f_name + "_2" + f_ext)

    file1 = open(file1_name,"a")
    file2 = open(file2_name,"a")

    for _x in list1:
        # print list items to file1
        SeqIO.write(_x, file1, 'fasta')

    for _y in list2:
        # print list items into file2
        SeqIO.write(_y, file2, 'fasta')

    file1.close()
    file2.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
