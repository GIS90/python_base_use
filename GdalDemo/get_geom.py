# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/27'
"""


import os
from osgeo import ogr
from osgeo import gdal

DRIVER = "ESRI Shapefile"
GDAL_FILE_CODE = "GDAL_FILENAME_IS_UTF8"
SHAPE_CODE = "SHAPE_ENCODING"


def get_geoms(ft):
    ftName = os.path.split(ft)[1]
    gdal.SetConfigOption(GDAL_FILE_CODE, "NO")
    gdal.SetConfigOption(SHAPE_CODE, "")
    ogr.RegisterAll()
    esriDriver = ogr.GetDriverByName(DRIVER)
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
        geomInfo = str(geom.ExportToJson()).split(":")[2].split("}")[0]
        print geomInfo
        print geomInfo.lstrip(".")

    print "%s is calculated success." % ft

if __name__ == "__main__":
    data = r'E:\data\hz_bus\busline_120010\busline_lineidbus_120010.shp'
    get_geoms(data)
