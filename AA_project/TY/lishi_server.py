# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import codecs
import os

import arcpy

try:
    import ogr
    import gdal
except ImportError:
    from osgeo import ogr
    from osgeo import gdal

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/1/4"

shape = r'E:\data\ty\linkgeo\linkgeo_sde.shp'
fields = ['NAME', 'LinkId', 'Class', 'SHAPE@JSON']


gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
gdal.SetConfigOption("SHAPE_ENCODING", "")
ogr.RegisterAll()

driver = ogr.GetDriverByName('ESRI Shapefile')
ds = driver.Open(shape, 0)
if ds is None:
    print "could not open and over"
    sys.exit(1)

layer = ds.GetLayer(0)
lyrcount = layer.GetFeatureCount()
print 'feature count:', lyrcount

shape_folder = os.path.dirname(shape)
shape_file = os.path.basename(shape)
shape_name = os.path.splitext(shape_file)[0]
shape_fmt = os.path.splitext(shape_file)[1]

js = os.path.abspath(os.path.join(shape_folder, shape_name + '_lishi.js'))
fw = codecs.open(filename=js,
                 mode='w',
                 encoding='utf8',
                 errors='strict',
                 buffering=1)
fw.write("var hzLinesData ={\n")
with arcpy.da.SearchCursor(shape, fields) as cursor:
    n = 1
    for row in cursor:
        name = row[0]
        linkid = 'lid_' + str(int(row[1]))
        roadclass = row[2]
        geom = str(row[3]).split(':')[1].split(',"')[0]
        geom_spl = geom.split('[[[')[1].split(']]]')[0].split('],[')
        geom_new = '[['
        for i in range(0, len(geom_spl)):
            i_new = geom_spl[i].split(',')
            for ii in range(0, len(i_new)):
                value = str(round(float(i_new[ii]), 6))
                geom_new += value
                if ii == 0:
                    geom_new += ','
            if i < len(geom_spl) - 1:
                geom_new += '],['
        geom_new += ']]'
        line = '"%s":{"type":"Feature","geometry":{"type":"LineString","coordinates":%s},' % (linkid, geom_new)
        line += '"properties":{"roadName":"%s","linkId":"%s","iClass":%d}}' % (name, linkid, roadclass)
        fw.write(line)
        fw.write(',') if n < lyrcount else 0
        n += 1
    fw.write('}')
    fw.close()

print 'en'
