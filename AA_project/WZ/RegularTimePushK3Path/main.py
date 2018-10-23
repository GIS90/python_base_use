# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: main.py
@time: 2016/10/28 10:00
@describe: 
@remark: 
------------------------------------------------
"""
import imp

dtmodule = imp.load_module("datetime", *imp.find_module('datetime'))
print datetime.datetime.now()

