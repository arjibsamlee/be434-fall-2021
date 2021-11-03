#!/usr/bin/env python3
"""
Author : Megan Kane <arjibsamlee@yahoo.com>
Date   : 2021-10-27
Purpose: I don't know yet
"""

import argparse
import os
import Bio


# pylint: disable=W0105


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
                        type=argparse.FileType('wt'),
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

    parentdir = os.getcwd()

    outpath = os.path.join(parentdir,directory.name)


    print(directory.name, outpath)

    if os.path.exists(outpath) is not True:
        os.makedirs(outpath)
        print("new directory:",outpath)

    for _ in filenames:
        print(_)
        split_biofile(_)

    print("Done, files in", outpath)


# ---------------------------
def split_biofile(filename):
    list1 = []
    list2 = []

    count = 1

    reader = SeqIO.parse(filename, 'fasta')

    # get each record. Put the even into list2 and the odd into list1
    for rec in reader:
        print('ID :', rec.id)
        print('Seq:', str(rec.seq))
        if count % 2 == 0:
            list2.append(rec.id,rec.seq)
        else:
            list1.append(rec.id,rec.seq)
        count += 1

    # get file name and extention
    f_name, f_ext = os.path.splitext(filename)

    file1_name = f_name + "_01" + f_ext
    file2_name = f_name + "_02" + f_ext

    file1 = open(file1_name,"a")
    file2 = open(file2_name,"a")

    for _x in list1:
        # print list items to file1
        file1.write(_x)


    for _y in list2:
        # print list items into file2
        file2.write(_y)

    file1.close()
    file2.close()










# --------------------------------------------------
if __name__ == '__main__':
    main()
