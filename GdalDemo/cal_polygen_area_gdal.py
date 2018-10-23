# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/27'
"""


import os
from osgeo import ogr
from osgeo import gdal


def calFtArea(ft):
    ftName = os.path.split(ft)[1]
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
    gdal.SetConfigOption("SHAPE_ENCODEING", "")
    ogr.RegisterAll()
    esriDriver = ogr.GetDriverByName("ESRI Shapefile")
    ds = esriDriver.Open(ft, 1)
    if ds is None:
        print "%s is not open." % ft
    lyr = ds.GetLayerByIndex(0)
    spatialRef = lyr.GetSpatialRef()
    print 'SpatialRef : %s' % spatialRef
    print 'Feature count is %d ' % lyr.GetFeatureCount(0)
    defn = lyr.GetLayerDefn()
    fieldNum = defn.GetFieldCount()
    # 遍历字段
    for index in range(fieldNum):
        print index
        field = defn.GetFieldDefn(index)
        print ('%s: %s(%d.%d)' % (field.GetNameRef(), field.GetFieldTypeName(field.GetType()), field.GetWidth(), field.GetPrecision()))
        if field.GetNameRef() == "Area":
            print "%s is contain Area field" % ftName
            break
        if index == (fieldNum - 1):
            areaField = ogr.FieldDefn("Area", ogr.OFTReal)
            areaField.SetWidth(32)
            areaField.SetPrecision(20)
            lyr.CreateField(areaField)
            print "%s is create Area field" % ftName
    for feature in lyr:
        geom = feature.GetGeometryRef()
        area = geom.GetArea()
        feature.SetField("Area", area)
        lyr.SetFeature(feature)
        geomInfo = str(geom.ExportToJson()).split(":")[2].split("}")[0]
        print geomInfo
        print geomInfo.lstrip(".")

    print "%s is calculated success." % ft

if __name__ == "__main__":
    data = r'E:\data\nj_js\zq_shp\NJ_ZQ.shp'
    calFtArea(data)
