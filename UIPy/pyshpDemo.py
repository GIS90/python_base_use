


#coding:utf-8



import shapefile
import arcpy
import os

shpPath=r'E:\Py_file'
arcpy.env.workspace=shpPath



#Reader------------
# for shp in arcpy.ListFiles('*.shp'):
#     sp=os.path.join(shpPath,shp)
#     sf=shapefile.Reader(sp)
#     print sf
#     print sf.shapeName,sf.shapeType,sf.shpLength,len(sf.shapes())
#     f=sf.fields
#     print f
#     r=sf.records()
#     print len(r)
#
#
#
#
#
# print '---------------------------------------------------------------'

#Write--------------------------
# point
# w=shapefile.Writer(shapefile.POINT)
# print w.shapeType
# w.autoBalane=1
# w.point(120,50,0,0)
# w.point(121,51,0,0)
# w.point(121,50,0,0)
# w.point(120,51,0,0)
# w.field('NAME')
# w.field('TYPE','C','20')
# w.record('p1','point')
# w.record('p2','point')
# w.record('p3','point')
# w.record('p4','point')
# w.save('myPoint')
# print '---------------------------------------------------------------'
#
# #polyline
# w=shapefile.Writer(shapefile.POLYLINE)
# print w.shapeType
# w.autoBalane=1
# w.line(parts=[[[120, 50],[121, 51],[121, 50],[120, 51]]],shapeType=3)
# w.field('NAME')
# w.record('line')
# w.save('myLine')
# print '---------------------------------------------------------------'
#
# #polylgon
# w=shapefile.Writer(shapefile.POLYGON)
# print w.shapeType
# w.autoBalane=1
# w.poly(parts=[[[120, 50, 0, 0],[121, 51, 0, 0],[121, 50, 0, 0],[120, 51, 0, 0]]],shapeType=5)
# w.field('NAME')
# w.record('Polygon')
# w.save('myPolygon')
# print '---------------------------------------------------------------'


#Editor--------------
for shp in arcpy.ListFiles('*.shp'):

    sp=os.path.join(shpPath,shp)
    e=shapefile.Editor(shapefile='E:\Py_file\myPolygon.shp')

    e.autoBalance=1

print '---------------------------------------------------------------'