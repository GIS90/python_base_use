# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: rename_sour_data.py
@time: 2016/8/28 15:57
@describe: 
@remark: 
------------------------------------------------
"""

import os
import re


def rename(source_dir):
    file_name_list = os.listdir(source_dir)
    for fn in file_name_list:
        fn = fn.encode("utf-8")
        pattern = re.compile("^#")
        match = pattern.match(fn)
        if match:
            pattern = re.compile("#")
            match = pattern.split(fn)
            file_name_new = os.path.splitext(str(match[1]))[0] + ".csv"
            print file_name_new
            file_new = os.path.join(source_dir, file_name_new)
            file_old = os.path.join(source_dir, fn)
            os.rename(file_old, file_new)
    print "OK"


if __name__ == '__main__':
    source_dir = u"E:\\@Project\\20160828青岛js"
    rename(source_dir)

