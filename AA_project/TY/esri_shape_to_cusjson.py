# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import arcpy
import codecs
import os
import simplejson


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/5/8"

print 'start'
shape = r"E:\data\ty\country\country.shp"
fields = ['netid', 'SHAPE@JSON']
f = os.path.splitext(shape)[0] + ".js"
target = codecs.open(f, mode='w')
target.write('{')

with arcpy.da.SearchCursor(shape, fields) as cursor:
    max = 6
    index = 1
    for row in cursor:
        netid = row[0]
        geoms = simplejson.loads(str(row[1]))["rings"]
        line = '"%s": "%s"' % (netid, geoms)
        target.write(line)
        target.write(',') if index < max else 0
        index += 1

    target.write('}')

print 'end'





