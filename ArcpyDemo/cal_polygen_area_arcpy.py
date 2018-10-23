# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/27'
"""

import arcpy

infc = r'E:\data\nj_js\zq_shp\NJ_ZQ.shp'

# Enter for loop for each feature
#
for row in arcpy.da.SearchCursor(infc, ["ID", "SHAPE@AREA"]):
    # Print x,y coordinates of each point feature
    #
    x = row[0]
    y = row[1]
    print("{0}, {1}".format(x, y))
