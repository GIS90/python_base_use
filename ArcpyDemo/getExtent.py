#coding:utf-8



import arcpy
import os
dataPath=r'E:\2015Project\shp'
arcpy.env.workspace=dataPath
for i in arcpy.ListFiles('*.shp'):
    shp=os.path.join(dataPath,i)
    desc = arcpy.Describe(shp)
    print("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))
























