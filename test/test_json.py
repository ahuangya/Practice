# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:test_json.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import pytest
from lib_practice.pra_json import *


def test_ergodic_json():
    """
    Determines the type of value
    """
    dict = {"key1": 12}
    assert (ergodic_json(dict2json(dict)), type(1))
