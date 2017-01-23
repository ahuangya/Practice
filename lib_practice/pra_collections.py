# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:collections.py
# Author:huangya
# Description:
# time:2017-01-20
# ***************************************

from collections import *


def test_namedtuple():

    users = [('ahuang', 21, '160cm')]

    User = namedtuple('User', ['name', 'age', 'height'])
    name_list = []
    for user in users:
        user = User._make(user)
        name_list.append(user.name)
    return ''.join(name_list)


def test_OrderedDict():
    items = (
        ('ahuang', 21),
        ('xiaobai', 22),
        ('laobi', 23)
    )

    regular_dict = dict(items)
    ordered_dict = OrderedDict(items)
    return ordered_dict.items()[1]


def test_deque():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    return q[-1], q[0]


def test_defaultdict():
    dd = defaultdict(lambda: 'None')
    dd['key'] = 'abc'
    return dd['key2']
