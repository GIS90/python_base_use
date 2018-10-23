# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: JsToTxt.py
@time: 2016/11/9 14:56
@describe: *.js file transfer to *.txt file
@remark: None
------------------------------------------------
"""

import os
import sys


__SOURCE_FORMAT = ".js"
__TARGET_FORMAT = ".txt"


def transfer(source_folder, target_folder, is_copy=False, is_delete_souece=False):
    assert isinstance(source_folder, basestring)
    assert isinstance(target_folder, basestring)

    if is_copy:
        import shutil
        if os.path.exists(target_folder):
            print "%s is exist, please reinput other a new folder." % target_folder
            sys.exit(1)
        print "working copy %s" % source_folder
        shutil.copytree(source_folder, target_folder)

    for dirpath, _, filenames in os.walk(target_folder):
        for filename in filenames:
            if filename.endswith(__SOURCE_FORMAT):
                cur_file_name = os.path.splitext(filename)[0]
                cur_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, (cur_file_name + __TARGET_FORMAT))
                try:
                    os.renames(cur_file, new_file)
                    print new_file
                except IOError as e:
                    print "os.renames occur IOError: %s" % e.message
                except Exception as e:
                    print "os.renames occur Exception: %s" % e.message

    if is_delete_souece:
        import shutil
        shutil.rmtree(source_folder)


if __name__ == "__main__":
    """
        设定好数据源目录，输入数据目录，运行即可
    """
    print "start............................"
    source_folder = r"E:\data\qd_data_js\data\population_density\population_period_avg"
    target_folder = r"E:\data\qd_data_js\txt1"
    if not os.path.exists(source_folder):
        print "%s is not exist, exit." % source_folder
        sys.exit(1)
    is_copy = True
    is_delete_souece = False
    try:
        transfer(source_folder, target_folder, is_copy, is_delete_souece)
    except Exception as e:
        print "transfer occur: %s" % e.message
    else:
        print "end............"
