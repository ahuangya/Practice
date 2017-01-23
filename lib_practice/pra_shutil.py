# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:pra_shutil.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import shutil
import os
import time


dirname = './lib_practice/example'
filename = './lib_practice/pra_shutil.py'


# def Info(filename):
#   """Displays the basic information about the file"""
#   stat_info=os.stat(filename)
#   print '\tMode:',stat_info.st_mode
#   print '\tCreated:',time.ctime(stat_info.st_ctime)
#   print '\tAccessed:',time.ctime(stat_info.st_atime)
#   print '\tModified:',time.ctime(stat_info.st_mtime)


def ShutilCopy(filename):
    """Copy the source files to the destination directory"""
#   print "SOURCE:"
#   Info(filename)
    shutil.copy(filename, dirname)
#   print 'DEST:'
#   Info(dirname+'/'+filename)
    os.path.exists(dirname + '/' + 'pra_shutil.py')


def exist(dirname):
    if os.path.exists(dirname):
        pass
    else:
        os.mkdir(dirname)

exist(dirname)
ShutilCopy(filename)
