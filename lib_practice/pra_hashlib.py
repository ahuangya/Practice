# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:pra_hashlib.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import hashlib
from functools import wraps
import time


db = {}


LOGIN_DICT = {'ERROR': 'login failed,cause by wrong password',
              'SUCCESS': 'login success'
              }
REGISTER_DICT = {'ERROR': 'Entering the password twice is not the same',
                 'SUCCESS': 'regisration success'}
INFORMATION = {'INFO': 'Do you want to log in now:(y|n)',
               'PASSWORD': 'please input password:',
               'USERNAME': 'please input username:',
               'REPASSWORD': 'please input password again:'}
USER_DICT = {'NAME': 'name:', 'PASSWORD': 'password:'}


def MD5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.clock()
        result = function(*args, **kwargs)
        t1 = time.clock()
        print "Total time running %s: %s s" % \
              (function.func_name, str(t1 - t0))
        return result

    return function_timer


@fn_timer
def register(username, password1, password2):
    if password1 == password2:
        db[str(username)] = MD5(password1)
        print REGISTER_DICT['SUCCESS']
    else:
        print REGISTER_DICT['ERROR']
        exit()


def login(name, pawd):
    if MD5(pawd) == db[name]:
        print LOGIN_DICT['SUCCESS']
        return 0
    else:
        print LOGIN_DICT['ERROR']
        return 1


def judgement():
    if raw_input(INFORMATION['INFO']) == 'y':
        login(name=raw_input(USER_DICT['NAME']),
              pawd=raw_input(USER_DICT['PASSWORD']))
    else:
        exit()

if __name__ == '__main__':
    register(username=raw_input(INFORMATION['USERNAME']),
             password1=raw_input(INFORMATION['PASSWORD']),
             password2=raw_input(INFORMATION['REPASSWORD']))
    judgement()
