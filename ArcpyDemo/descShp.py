# coding:utf-8


import os

import arcpy

filePath = r"E:\data\hz_bus\busline_ne0"
arcpy.env.workspace = filePath

for shp in arcpy.ListFiles('*.shp'):
    feature = os.path.join(filePath, shp)
    desc = arcpy.Describe(feature)
    print "Feature Type:  " + desc.featureType
    print "Shape Type :   " + desc.shapeType
    print "Spatial Index: " + str(desc.hasSpatialIndex)
