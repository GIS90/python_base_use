# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/4'
"""


import sys
from osgeo import gdal
from osgeo import ogr
from osgeo import osr


def Read(data):
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
    gdal.SetConfigOption("SHAPE_ENCODING", "")
    ogr.RegisterAll()
    driver = ogr.GetDriverByName('ESRI Shapefile')
    ds = driver.Open(data)
    if ds is None:
        print '%s not open' % data
        sys.exit(1)
    lyr = ds.GetLayerByIndex(0)
    spatialRef = lyr.GetSpatialRef()
    print 'SpatialRef : %s' % spatialRef
    print lyr.GetFeatureCount(0)
    defn = lyr.GetLayerDefn()
    fieldCount = defn.GetFieldCount()
    for index in range(fieldCount):
        field = defn.GetFieldDefn(index)
        print ('%s: %s(%d.%d)' % (field.GetNameRef(), field.GetFieldTypeName(field.GetType()), field.GetWidth(), field.GetPrecision()))
    print '--------------------------------------------------------'
    # feature = lyr.GetNextFeature()
    # while feature is not None:
    #     # 获取要素中的属性表内容
    #     line = ''
    #     for index in range(fieldCount):
    #         oField = defn.GetFieldDefn(index)
    #         line = " %s (%s) = " % (oField.GetNameRef(), oField.GetFieldTypeName(oField.GetType()))
    #         if feature.IsFieldSet(index):
    #             line += "%s" % (feature.GetFieldAsString(index))
    #         else:
    #             line += "(null)"
    #     print line
    #     geometry = feature.GetGeometryRef()
    #     print geometry
    #
    # feature.Destroy()
    ds.Destroy()


def Create(data):
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
    gdal.SetConfigOption("SHAPE_ENCODING", "")
    ogr.RegisterAll()
    driver = ogr.GetDriverByName('ESRI Shapefile')
    ds = driver.CreateDataSource(data)
    shapLayer = ds.CreateLayer("poi", geom_type=ogr.wkbPoint)
    # 添加字段
    fieldDefn = ogr.FieldDefn('id', ogr.OFTString)
    fieldDefn.SetWidth(4)
    shapLayer.CreateField(fieldDefn)
    # 创建feature
    defn = shapLayer.GetLayerDefn()
    feature = ogr.Feature(defn)
    # 添加属性
    feature.SetField("id", "liu")
    # 添加坐标
    point = ogr.Geometry(ogr.wkbPoint)
    point.AddPoint(float(113.56647912), float(22.16128203))
    feature.SetGeometry(point)
    shapLayer.CreateFeature(feature)
    feature.Destroy()
    ds.Destroy()
    print 'Create %s success' % feature


if __name__ == '__main__':
    shp = r'E:\data\nj_js\zq_shp\NJ_ZQ.shp'
    Read(shp)
    # shp = r'E:'
    # Create(shp)
