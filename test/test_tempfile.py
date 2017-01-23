# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_tempfile.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import pytest
from lib_practice.pra_tempfile import *


def test_Make_File():
    """
    Judge the existence of the file
    Existence is true
    There is no false
    """
    assert(Make_File(), True)


def test_Make_Temporary_File():
    """
    Temporary files will not exist after being closed
    """
    assert(Make_Temporary_File(), False)


def test_Make_NamedTemporary_File():
    """
    A named temporary file will not exist after it is closed
    """
    assert(Make_NamedTemporary_File(), False)


def test_Make_Temp_Dir():
    """
    Whether the temporary directory exists
    """
    assert(Make_Temp_Dir(), True)
