# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: dbhandler_test.py
@time: 2016/9/22 15:39
@describe: 
@remark: 
------------------------------------------------
"""
import os
DIR = os.path.dirname(__file__)
print DIR
PARENT_DIR = os.path.join(DIR, "..")
print PARENT_DIR
PARENT_DIR = os.path.abspath(PARENT_DIR)
print PARENT_DIR
core_dir = os.path.abspath(os.path.join(PARENT_DIR, "core"))
import sys
sys.path.append(core_dir)
print core_dir



#
# db = DBHandler(DBTpye.MYSQL, "127.0.0.1", 3306, "root", "123456", "test")
# db.open()
# print db.open()
# if db.isopen():
#     sql = "busline_copy"
#     rlt = db.delete_all(sql)
#     print rlt
