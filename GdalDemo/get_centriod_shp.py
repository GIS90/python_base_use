# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: get_centriod_shp.py
@time: 2016/9/26 16:22
@describe: get centroid xy of the shapefile data, append field
@remark: 
------------------------------------------------
"""
import os
import sys
import datetime
import threading
from Queue import Queue
from osgeo import ogr
from osgeo import gdal


DRIVER = "ESRI Shapefile"
GDAL_FILE_CODE = "GDAL_FILENAME_IS_UTF8"
SHAPE_CODE = "SHAPE_ENCODING"


def check_xy(lyr, fd):
    defn = lyr.GetLayerDefn()
    field_num = defn.GetFieldCount()
    for index in range(field_num):
        field = defn.GetFieldDefn(index)
        # print ('%s: %s(%d.%d)' % (field.GetNameRef(), field.GetFieldTypeName(field.GetType()), field.GetWidth(), field.GetPrecision()))
        if field.GetNameRef() == fd:
            print "Contain %s field" % fd
            return
    xy_field = ogr.FieldDefn(fd, ogr.OFTReal)
    xy_field.SetWidth(32)
    xy_field.SetPrecision(20)
    lyr.CreateField(xy_field)
    print "Create %s field." % fd


def add_centroid(feature, fields):
    global lyr
    assert isinstance(fields, list)
    assert isinstance(feature, basestring)

    feature_name = os.path.split(feature)[1]
    gdal.SetConfigOption(GDAL_FILE_CODE, "NO")
    gdal.SetConfigOption(SHAPE_CODE, "")
    ogr.RegisterAll()
    esriDriver = ogr.GetDriverByName(DRIVER)
    ds = esriDriver.Open(feature, 1)
    if ds is None:
        raise "%s is not open." % feature_name
    lyr = ds.GetLayerByIndex(0)
    spatial_ref = lyr.GetSpatialRef()
    feature_num = lyr.GetFeatureCount(0)
    print 'SpatialRef : %s' % spatial_ref
    print 'Feature count is %d ' % feature_num

    # 遍历字段
    for field in fields:
        check_xy(lyr, field)

    queue = Queue()
    for in_feature in lyr:
        queue.put(in_feature)
    for i in range(1, 5, 1):
        th_name = "consumer_" + str(i)
        cons = Consumer(th_name, queue)
        cons.start()
    ds.Destroy()
    print "%s is calculated %d success." % (feature_name, feature_num)


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.work = queue

    def run(self):
        try:
            in_feature = self.work.get(1, 5)
            print in_feature
            geom = in_feature.GetGeometryRef()
            centroid = geom.Centroid()
            centroid_x = centroid.GetX()
            centroid_y = centroid.GetY()
            in_feature.SetField(fields[0], centroid_x)
            in_feature.SetField(fields[1], centroid_y)
            lyr.SetFeature(in_feature)
            print centroid_x, centroid_y
        except Exception as e:
            print "%s is finished." % self.name



if __name__ == '__main__':
    fields = ["centroid_x", "centroid_y"]
    data_source = r'E:\data\json\busline.shp'
    start_time = datetime.datetime.now()

    # try:
    add_centroid(data_source, fields)
    # except Exception as e:
    #     print "do_clip occur exception: %s, ahead of the end" % e.message
    #     sys.exit(1)
    end_time = datetime.datetime.now()
    exe_time = (end_time - start_time).seconds
    print "All features finish and cost time is : %s s." % exe_time

