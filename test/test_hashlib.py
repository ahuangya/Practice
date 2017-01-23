# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_hashlib.py
# Author:huangya
# Description:
# time:2017-01-22
# ***************************************

import pytest
from lib_practice.pra_hashlib import *


def test_register():
    """
    Use the name, password for user registration,
    the success of the registration function is stored in the db,
    Determine whether the user's password in db is equal to the MD5
    encrypted password
    """
    register('ahuang', '123456', '123456')
    assert db['ahuang'] == MD5('123456')


def test_login():
    """
    Successful registration function can normal landing
    """
    assert login('ahuang', '123456') == 0
