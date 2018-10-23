# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: cal_node_polyline.py
@time: 2016/8/23 10:25
@describe: 
@remark:
编程思想：
1.遍历获取每条路网的geom，把起点，终点坐标加入数组
2.根据数据坐标点生成点坐标
3.点坐标赋值
4.把点属性值赋予路网
------------------------------------------------
"""

import os
import sys
import datetime
import shutil
from osgeo import ogr
from osgeo import gdal
from osgeo import osr


DRIVER = "ESRI Shapefile"
GDAL_FILE_CODE = "GDAL_FILENAME_IS_UTF8"
SHAPE_CODE = "SHAPE_ENCODING"


class OpenShapeException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg
        print msg


def DefineRef(fc_path, fc_name, ref_code):
    sr = osr.SpatialReference()
    sr.ImportFromEPSG(ref_code)
    prj_file = os.path.join(fc_path, os.path.splitext(fc_name)[0] + '.prj')
    prj = open(prj_file, 'w')
    sr.MorphToESRI()
    prj.write(sr.ExportToWkt())
    prj.close()


def ReadPolyline(source_file):
    """
    Read polyline
    :param source_file:
    :return: line_lyr
    """
    gdal.SetConfigOption(GDAL_FILE_CODE, "NO")
    gdal.SetConfigOption(SHAPE_CODE, "")
    ogr.RegisterAll()
    line_driver = ogr.GetDriverByName(DRIVER)
    line_ds = line_driver.Open(source_file)
    if line_ds is None:
        raise OpenShapeException("%s is not open" % source_file)
    line_lyr = line_ds.GetLayerByIndex(0)
    line_spatial_ref = line_lyr.GetSpatialRef()
    line_fecture_count = line_lyr.GetFeatureCount(0)
    print 'SpatialRef : %s' % line_spatial_ref
    print 'Feature count is %d ' % line_fecture_count
    return line_lyr


def do_node(source_file, target_dir):

    assert isinstance(source_file, basestring)
    assert isinstance(target_dir, basestring)
    if os.path.exists(target_dir):
        print '%s is exist, deleting file.' % target_dir
        shutil.rmtree(target_dir)
        os.makedirs(target_dir)
    else:
        print '%s is not exist, making dirs.' % target_dir
        os.makedirs(target_dir)
    source_name = os.path.split(source_file)[1]
    target_name = os.path.join(os.path.splitext(source_name)[0] + "_p")

    line_lyr = ReadPolyline(source_file)

    # write point shape
    point_geoms = []
    gdal.SetConfigOption(GDAL_FILE_CODE, "NO")
    gdal.SetConfigOption(SHAPE_CODE, "")
    ogr.RegisterAll()
    point_driver = ogr.GetDriverByName(DRIVER)
    point_ds = point_driver.CreateDataSource(target_dir)
    point_lyr = point_ds.CreateLayer(target_name, geom_type=ogr.wkbPoint)
    point_field_defn = ogr.FieldDefn("ID", ogr.OFTInteger)
    point_field_defn.SetWidth(4)
    point_lyr.CreateField(point_field_defn)
    point_defn = point_lyr.GetLayerDefn()
    point_feature = ogr.Feature(point_defn)

    for feature in line_lyr:
        geom = feature.GetGeometryRef()
        geomInfo = str(geom.ExportToJson()).split(":")[2].split("}")[0]
        geomInfo = geomInfo.split("[ [")[1].split("] ]")[0].split("], [")
        start_geom = geomInfo[0]
        end_geom = geomInfo[len(geomInfo) - 1]
        if start_geom not in point_geoms:
            point_geoms.append(start_geom)
        if end_geom not in point_geoms:
            point_geoms.append(end_geom)
    print len(point_geoms)
    id_value = 0
    for point_geom in point_geoms:
        x = float(str(point_geom).split(",")[0])
        y = float(str(point_geom).split(",")[1])
        point_feature.SetField("ID", id_value)
        id_value += 1
        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(x, y)
        point_feature.SetGeometry(point)
        point_lyr.CreateFeature(point_feature)
    spatial_ref_code = 4326
    DefineRef(target_dir, target_name, spatial_ref_code)
    point_feature.Destroy()
    point_ds.Destroy()
    line_ds.Destroy()
    print 'Create %s shpFile success' % target_name


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    source_file = r'E:\data\ty\linkgeo\linkgeotest.shp'
    target_dir = r'E:\data\ty\linkgeo_p'
    # try:
    do_node(source_file, target_dir)
    # except Exception as e:
    #     print "do_node occur exception: %s, ahead of the end" % e.message
    #     sys.exit(1)
    end_time = datetime.datetime.now()
    exe_time = (end_time - start_time).seconds
    print "All features finish and cost time is : %s s." % exe_time
