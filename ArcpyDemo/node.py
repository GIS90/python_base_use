# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

import arcpy
import simplejson

alist = []
adict = {}
nodeid = 1000
shape = r'E:\data\ty\ty_test\linkgeo_ZZ.shp'
with arcpy.da.UpdateCursor(shape, ['SHAPE@JSON']) as cursor:
    for row in cursor:
        geoms = simplejson.loads(row[0])['paths']
        start = geoms[0][0]
        if start not in alist:
            adict[nodeid] = start
            nodeid += 1
        end = geoms[-1][-1]
        if end not in alist:
            adict[nodeid] = end
            nodeid += 1
print len(adict)
# with arcpy.da.UpdateCursor(shape, ('fromnode', 'SHAPE@JSON')) as cursor:
#         for row in cursor:
#             geoms = simplejson.loads(row[1])['paths']
#             start = geoms[0][0]
#             for k, v in adict.items():
#                 if start == v:
#                     row[0] = k
#                     cursor.updateRow(row)
#
#             end = geoms[-1][-1]
#             for k, v in adict.items():
#                 if start == v:
#                     row[0] = k
#                     cursor.updateRow(row)







