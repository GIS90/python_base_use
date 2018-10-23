# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import re

import arcpy

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/8"

fc = r"E:\data\ws\ws_linkgeo_201702\LinkGeo.shp"
fields = ["LinkId", "SHAPE@JSON"]
pattern = re.compile(r".+(\]\],\[\[).+", re.I)

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        fid = row[0]
        geom = row[1]
        rlt = pattern.search(geom)
        if rlt: print fid
