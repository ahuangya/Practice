# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:pra_datetime.py
# Author:huangya
# Description:
# time:2017-01-18
# ***************************************

import datetime
import time


class MyDate:
    def __init__(self, i):
        self.i = i

    def getDays(self, st, end):
        today = datetime.date.today() + datetime.timedelta(self.i)
        oneday = datetime.timedelta(days=1)
        tomorrow = today + oneday
        li = []
        for i in range(0, end):
            today = today + oneday
            li.append(str(today))
        return li[0]


def Days2Num(inputday):
    today = datetime.date.today()
    today = datetime.datetime.strptime(str(today), '%Y-%m-%d')
    inputday = datetime.datetime.strptime(inputday, '%Y-%m-%d')
    Distance = inputday - today
    return str(Distance).replace(', 0:00:00', '')
