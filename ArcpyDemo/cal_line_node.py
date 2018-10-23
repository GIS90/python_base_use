# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: cal_line_node.py
@time: 2016/8/19 10:35
@describe: 
@remark: 
------------------------------------------------
"""
import arcpy


fc = r"E:\data\ty\linkgeo\linkgeo.shp"
fields = ["linkId", "SHAPE@JSON"]

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        print row

