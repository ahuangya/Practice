# !/usr/bin/env python
# -*-coding:utf-8-*-
# **************************************
# Filename:pra_json.py
# Author:huangya
# Description:
# time:2017-01-21
# ***************************************

import json


global type_list
type_list = []


def dict2json(dict):
    """
    dict convert json
    """
    json_str = json.dumps(dict)
    return json_str


def ergodic_json(json_str):
    """
    input  json
    output value list
    """
    global type_list
    data = json.loads(json_str)
    keylist = data.keys()
    for i in range(len(keylist)):
        if type(data[keylist[i]]) == type({}):
            json_str = dict2json(data[keylist[i]])
            type_list.append(type(data[keylist[i]]))
            return ergodic_json(json_str)
        else:
            type_list.append(type(data[keylist[i]]))
            print type_list
    return type_list


dict = {"key1": 12}
ergodic_json(dict2json(dict))
