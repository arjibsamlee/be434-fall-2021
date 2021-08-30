#! usr/bin/env python3
"""
Tests for mmk_hello.py
"""
import os
from subprocess import getoutput, getstatusoutput


prg = './mmk_hello.py'


#---------------------

def test_exists():
    # Does the file exixt?

    assert os.path.isfile(prg)

#----------------------
def test_runnable():
    # test runs on python3
    out = getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'

#-----------------------
def test_executable():
    # Says Hello Wolrd! by default
    out = getoutput(prg)
    assert out.strip() == 'Hello, World!'


#-------------------------
def test_usage():
    # the usage of the program
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg}{flag}')
        assert rv == 0
        assert out.lower().startswith('ussage')

#-------------------------------

def test_input():
    #test for input
    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = getstatusupdate(f'{prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'

# end program

