# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/7'
"""


import arcpy


fc = r'E:\data\ws\ws_linkgeo_201607\LinkOrg.shp'
fields = ['RoadName', 'RoadId']

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        row[1] = 1
        cursor.updateRow(row)

print 'ok'


