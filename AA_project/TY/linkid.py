# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:


    it generator objectid: linkid
------------------------------------------------
"""
import arcpy
import codecs
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/19"


shape = r'E:\data\ty\sde_data\linkgeo.shp'
fields = ['objectid', 'linkid']
jsfile = os.path.join(os.path.dirname(shape), 'linkid.js')
print jsfile
jsfile = os.path.abspath(jsfile)

count = 110
with open(jsfile, 'w') as f:
    f.write('{')
    with arcpy.da.SearchCursor(shape, fields) as cursor:
        index = 1
        for row in cursor:
            objectid = int(row[0])
            linkid = int(row[1])
            line = '"%s": "%s"' % (objectid, linkid)
            f.write(line)
            f.write(',') if index < count else []
            index += 1
        f.write('}')
    f.close()

print 'end'






