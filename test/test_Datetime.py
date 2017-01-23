# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_Datetime.py
# Author:huangya
# Description:
# time:2017-01-18
# ***************************************

import pytest
from lib_practice.pra_datetime import *
import datetime


def testMyDate():
    """
    Get the date of the next 10 days from today,
    Determine whether the date of the first day is accurate
    """
    assert MyDate(0).getDays(1, 10) == '2017-01-23'


def testDays2Num():
    """
    Input a day,and today a difference of a few days
    """
    assert Days2Num('2017-02-01') == '10 days'
