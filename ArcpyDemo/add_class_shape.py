# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: add_class_shape.py
@time: 2016/8/22 16:42
@describe: add shape field class value
@remark: 
------------------------------------------------
"""

import datetime
import os
import sys

import arcpy

SHAPE_PATH = r"E:\data\ty\ty_map(wgs84)\linkgeo.shp"
FIELDS = ["FID", "RouteType", "Class"]


def add_class_field(fc_file, fc_dir):
    """
    判断有无class字段
    :param fc_file: 要素的名称
    :param fc_dir:  要素所在的文件夹
    :return: 有class返回true，否则返回false
    """
    assert isinstance(fc_dir, basestring)
    assert isinstance(fc_file, basestring)
    if not os.path.isdir(fc_dir):
        return False, "%s is not dir" % fc_dir
    arcpy.env.workspace = fc_dir
    fields = arcpy.ListFields(fc_file)
    for field in fields:
        if str(field.name).lower() == "class":
            return True, "%s is contain class field" % fc_file
    else:
        try:
            arcpy.AddField_management(fc_file,
                                      "Class",
                                      "LONG",
                                      "20",
                                      "",
                                      "",
                                      "",
                                      "NULLABLE",
                                      "NON_REQUIRED",
                                      "")
            return True, "%s is create class field" % fc_file
        except Exception as e:
            return False, "add_class_field().AddField_management occur exception: %s" % e.message


def add_class_values(fc):
    """
    计算class等级值
    :param fc: 要素
    :return: 无
    """
    fc_dir = os.path.dirname(fc)
    fc_file = os.path.basename(fc)

    arcpy.env.workspace = fc_dir
    isOK, msg = add_class_field(fc_file, fc_dir)
    if isOK is False:
        print "Adanced over: %s" % msg
        sys.exit(1)
    else:
        with arcpy.da.UpdateCursor(fc_file, FIELDS) as cursor:
            for row in cursor:
                class_value = row[1].encode("utf-8")
                if class_value == "高速":
                    row[2] = 1
                elif class_value == "省道" or class_value == "国道":
                    row[2] = 2
                else:
                    row[2] = 5
                cursor.updateRow(row)
                print row[0]
        print "%s update class field ok" % fc_file


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    add_class_values(SHAPE_PATH)
    end_time = datetime.datetime.now()
    exe_time = (end_time - start_time).seconds
    print "All features finish and cost time is : %s s." % exe_time
