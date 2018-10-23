# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: cal_polyline_length_gdal.py
@time: 2016/8/18 13:55
@describe: calaulate geometry length
@remark: polygon and polyline
------------------------------------------------
"""

import os
import sys
import datetime
from osgeo import ogr
from osgeo import gdal


def cal_length(ft):
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
    geoType = lyr.GetGeomType()
    print 'Feature geometry type is %s' % geoType
    print 'SpatialRef : %s' % spatialRef
    print 'Feature count is %d ' % lyr.GetFeatureCount(0)
    defn = lyr.GetLayerDefn()
    fieldNum = defn.GetFieldCount()
    # 遍历字段
    for index in range(fieldNum):
        print index
        field = defn.GetFieldDefn(index)
        print ('%s: %s(%d.%d)' % (field.GetNameRef(), field.GetFieldTypeName(field.GetType()), field.GetWidth(), field.GetPrecision()))
        if field.GetNameRef() == "Length":
            print "%s is contain Length field" % ftName
            break
        if index == (fieldNum - 1):
            areaField = ogr.FieldDefn("Length", ogr.OFTReal)
            areaField.SetWidth(32)
            areaField.SetPrecision(20)
            lyr.CreateField(areaField)
            print "%s is create Length field" % ftName
    for feature in lyr:
        geom = feature.GetGeometryRef()
        length = geom.Length()
        feature.SetField("Length", length)
        lyr.SetFeature(feature)
        geomInfo = str(geom.ExportToJson()).split(":")[2].split("}")[0]

    print "%s is calculated success." % ft

if __name__ == "__main__":

    # 数据的工作空间
    data_dir = r"E:\data\ty\linkgeo"
    start_time = datetime.datetime.now()
    file_list = os.listdir(data_dir)
    for shp in file_list:
        if shp.endswith(".shp"):
            print "----------Execute %s calculate length----------" % shp
            try:
                shp = os.path.join(data_dir, shp)
                cal_length(shp)
            except Exception as e:
                print "cal_lenth occur exception: %s, ahead of the end" % e.message
                sys.exit(1)
    end_time = datetime.datetime.now()
    exe_time = (end_time - start_time).seconds
    print "All features finish and cost time is : %s s." % exe_time
