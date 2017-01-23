# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:pra_tempfile.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import os
import tempfile


def Make_File():
    ''' create a file'''
    file_name = './lib_practice/example.%s.txt' % os.getpid()
    temp = open(file_name, 'w+b')
#   print 'temp : {}'.format(temp)
#   print 'temp.name : {}'.format(temp.name)
    temp.write(b'hello, I\'m ahuang')
    temp.seek(0)
#   print '*' * 50
#   print 'content : {}'.format(temp.read())
    temp.close()
    return os.path.exists(file_name)
    os.remove(file_name)


def Make_Temporary_File():
    """Create a temp file"""
    temp = tempfile.TemporaryFile()
#   print 'temp : {}'.format(temp)
#   print 'temp.name : {}'.format(temp.name)
    temp.write(b'hello, I\'m ahuang')
    temp.seek(0)
#   print '*' * 50
#   print 'content : {}', temp.read()
    temp.close()  # then the system will automatically cleans up the file
    return os.path.exists(temp.name)


def Make_NamedTemporary_File():
    """Create a named temporary file"""
    temp = tempfile.NamedTemporaryFile()
#   print 'temp : {}', temp
#   print 'temp.name : {}', temp.name
    temp.write(b'hello, I\'m ahuang')
    temp.seek(0)
#   print '*' * 50
#   print 'content : {}', temp.read()
    temp.close()
    return os.path.exists(temp.name)


def Make_Temp_Dir():
    """create a temp directory"""
    TempDir = tempfile.mkdtemp()
    return os.path.exists(TempDir)
    os.removedirs(TempDir)
