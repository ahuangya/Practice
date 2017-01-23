# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_shutil.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import pytest
from lib_practice.pra_shutil import *


def test_exists():
    """
    Determine whether the dst directory exists
    """
    exist(dirname)
    assert(os.path.exists(dirname), True)


def test_ShutilCopy():
    """
    Detects whether a file exists in the target directory after being copied
    """
    ShutilCopy(filename)
    assert(os.path.exists(dirname + '/' + 'pra_shutil.py'), True)
