# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_collections.py
# Author:huangya
# Description:
# time:2017-01-20
# ***************************************

import pytest
from lib_practice.pra_collections import *


def testnamedtuple():

    assert test_namedtuple() == 'ahuang'


def testOrderedDict():
    assert test_OrderedDict() == ('xiaobai', 22)


def testdeque():
    """
    Determine whether x and y have been inserted successfully
    """
    assert test_deque() == ('x', 'y')


def testdefaultdict():
    """
    If defaultdict takes a non-existent value,
    will return to the pre-set value will not be an error
    """
    assert test_defaultdict() == 'None'
