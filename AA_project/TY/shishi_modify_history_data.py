# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import os
import datetime
__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/12/22"

now = datetime.datetime.now() - datetime.timedelta(days=1)
cur_date = now.strftime("%Y-%m-%d")
cur_folder = "/opt/apache-tomcat-7.0.68/webapps/tsnav/data/history/"
cur_file_list = os.listdir(cur_folder)
for f in cur_file_list:
    f_old_name = f
    f_new_name = f_old_name[:-13] + cur_date + ".js"
    os.rename(f_old_name, f_new_name)
    print f_old_name, f_new_name








