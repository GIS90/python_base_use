#- * - coding: utf-8 - * -

import os,sys
import time
try:
    import ogr
except:
    from osgeo import ogr


shpFile = r'E:\data\qy\ceShi.shp'
driver = ogr.GetDriverByName('ESRI ShapeFile')
dataSource = driver.CreateDataSource(shpFile)
layer = dataSource.CreateLayer('ceShi',geom_type = ogr.wkbPoint)

nameField = ogr.FieldDefn()
nameField.SetName('name')
nameField.SetType(ogr.OFTString)
nameField.SetWidth(20)
layer.CreateField(nameField)

featDefine = layer.GetLayerDefn()
feature = ogr.Feature(featDefine)
feature.SetGeometry(ogr.wkbPoint)
feature.SetField('name','ceshi')

layer.CreateFeature(feature)