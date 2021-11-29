#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './tamriel.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput(f'{prg}')
    assert rv == 0
    assert out.startswith('Welcome to the Elder Scrolls Guide!')


# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(f'{prg} -r race')
    assert rv == 0
    assert out.startswith("getting requested")


# --------------------------------------------------
def test_03():
    """test"""

    rv, out = getstatusoutput(f'{prg} -r ce')
    assert rv == 0
    assert out.startswith("Not a valid request.")
