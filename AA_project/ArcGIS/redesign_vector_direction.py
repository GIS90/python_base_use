# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
redesign to linkgeo direction of polyline shape,
in order to shape direction of vector same as
route direction of reality and to part in ZhiShu calcelation
if shape contains of innormal direction data
------------------------------------------------
"""
import sys

import arcpy

try:
    import gdal
    import ogr
except ImportError:
    from osgeo import gdal
    from osgeo import ogr


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/6"

shape = r'E:\data\ty\ling.shp'
fields = ['id', 'SHAPE@JSON']
with arcpy.da.SearchCursor(shape, fields) as cursor:
    for fc in cursor:
        print fc[0], fc[1]