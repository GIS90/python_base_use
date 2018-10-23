# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/4'
"""

import os
import csv
import shutil
import datetime
from osgeo import gdal
from osgeo import ogr
from osgeo import osr


def ReadXY(csvFile):
    csvfile = file(csvFile, 'rb')
    content = csv.reader(csvfile)
    return content


def AddField(fLyr, fName, fType, fWidth):
    fieldDefn = ogr.FieldDefn(fName, fType)
    fieldDefn.SetWidth(fWidth)
    fLyr.CreateField(fieldDefn)


def SetFieldValue(feat, fName, fValue):
    feat.SetField(fName, fValue)


def DefineRef(shpPath, shpName, refCode):
    sr = osr.SpatialReference()
    sr.ImportFromEPSG(refCode)
    prjFile = os.path.join(shpPath, os.path.splitext(shpName)[0] + 'prj')
    prj = open(prjFile, 'w')
    sr.MorphToESRI()
    prj.write(sr.ExportToWkt())


def CreatePoint(sourFile, shpField):

    sourPath = os.path.split(sourFile)[0]
    sourName = os.path.split(sourFile)[1]
    sourInfo = ReadXY(sourFile)
    destName = os.path.splitext(sourName)[0]
    destPath = os.path.join(sourPath, os.path.splitext(sourName)[0] + '_Shp')
    if os.path.exists(destPath):
        print '%s is exist, deleting file.' % destPath
        shutil.rmtree(destPath)
        os.makedirs(destPath)

    else:
        print '%s is not exist, making dirs.' % destPath
        os.makedirs(destPath)
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
    gdal.SetConfigOption("SHAPE_ENCODING", "")
    ogr.RegisterAll()
    driver = ogr.GetDriverByName('ESRI Shapefile')
    ds = driver.CreateDataSource(destPath)
    shpLayer = ds.CreateLayer(destName, geom_type=ogr.wkbPoint)

    lineNum = 0
    medallion_name = ''
    hack_license_name = ''
    vendor_id_name = ''
    rate_code_name = ''
    store_and_fwd_flag_name = ''
    pickup_datetime_name = ''
    dropoff_datetime_name = ''
    passenger_count_name = ''
    trip_time_in_secs_name = ''
    trip_distance_name = ''
    pickup_longitude_name = ''
    pickup_latitude_name = ''
    dropoff_longitude_name = ''
    dropoff_latitude_name = ''
    for line in sourInfo:
        print lineNum
        if lineNum == 0:
            try:
                # 创建字段
                medallion_name = line[0]
                AddField(shpLayer, medallion_name, ogr.OFTString, 100)
                # hack_license_name = line[1]
                hack_license_name = 'hack_lic'
                AddField(shpLayer, hack_license_name, ogr.OFTString, 100)
                vendor_id_name = line[2]
                AddField(shpLayer, vendor_id_name, ogr.OFTString, 25)
                rate_code_name = line[3]
                AddField(shpLayer, rate_code_name, ogr.OFTString, 25)
                # store_and_fwd_flag_name = line[4]
                store_and_fwd_flag_name = 'store_fwd'
                AddField(shpLayer, store_and_fwd_flag_name, ogr.OFTString, 10)
                # pickup_datetime_name = line[5]
                pickup_datetime_name = 'pick_time'
                AddField(shpLayer, pickup_datetime_name, ogr.OFTString, 50)
                # dropoff_datetime_name = line[6]
                dropoff_datetime_name = 'drop_time'
                AddField(shpLayer, dropoff_datetime_name, ogr.OFTString, 50)
                # passenger_count_name = line[7]
                passenger_count_name = 'psg_count'
                AddField(shpLayer, passenger_count_name, ogr.OFSTInt16, 20)
                # trip_time_in_secs_name = line[8]
                trip_time_in_secs_name = 'cost_time'
                AddField(shpLayer, trip_time_in_secs_name, ogr.OFTString, 20)
                # trip_distance_name = line[9]
                trip_distance_name = 'distance'
                AddField(shpLayer, trip_distance_name, ogr.OFSTInt16, 20)
                # pickup_longitude_name = line[10]
                pickup_longitude_name = 'pick_log'
                AddField(shpLayer, pickup_longitude_name, ogr.OFTString, 20)
                # pickup_latitude_name = line[11]
                pickup_latitude_name = 'pick_lat'
                AddField(shpLayer, pickup_latitude_name, ogr.OFTString, 20)
                # dropoff_longitude_name = line[12]
                dropoff_longitude_name = 'drop_log'
                AddField(shpLayer, dropoff_longitude_name, ogr.OFTString, 20)
                # dropoff_latitude_name = line[13]
                dropoff_latitude_name = 'drop_lat'
                AddField(shpLayer, dropoff_latitude_name, ogr.OFTString, 20)

                # 创建feature
                defn = shpLayer.GetLayerDefn()
                feature = ogr.Feature(defn)
                lineNum += 1
            except Exception as ae:
                print 'CreatePoint.AddField() occur exception : %s.' % ae.message
        else:
            try:
                # 字段赋值
                medallion = line[1]
                SetFieldValue(feature, medallion_name, medallion)
                hack_license = line[2]
                SetFieldValue(feature, hack_license_name, hack_license)
                vendor_id = line[3]
                SetFieldValue(feature, vendor_id_name, vendor_id)
                rate_code = line[4]
                SetFieldValue(feature, rate_code_name, rate_code)
                store_and_fwd_flag = line[5]
                SetFieldValue(feature, store_and_fwd_flag_name, store_and_fwd_flag)
                pickup_datetime = line[6]
                SetFieldValue(feature, pickup_datetime_name, pickup_datetime)
                dropoff_datetime = line[6]
                SetFieldValue(feature, dropoff_datetime_name, dropoff_datetime)
                passenger_count = line[7]
                SetFieldValue(feature, passenger_count_name, passenger_count)
                trip_time_in_secs = line[8]
                SetFieldValue(feature, trip_time_in_secs_name, trip_time_in_secs)
                trip_distance = line[9]
                SetFieldValue(feature, trip_distance_name, trip_distance)
                pickup_longitude = line[10]
                SetFieldValue(feature, pickup_longitude_name, pickup_longitude)
                pickup_latitude = line[11]
                SetFieldValue(feature, pickup_latitude_name, pickup_latitude)
                dropoff_longitude = line[12]
                SetFieldValue(feature, dropoff_longitude_name, dropoff_longitude)
                dropoff_latitude = line[13]
                SetFieldValue(feature, dropoff_latitude_name, dropoff_latitude)

                # 添加坐标
                shpField[0] = dropoff_longitude
                shpField[1] = dropoff_latitude
                point = ogr.Geometry(ogr.wkbPoint)
                point.AddPoint(float(shpField[0]), float(shpField[1]))
                feature.SetGeometry(point)
                shpLayer.CreateFeature(feature)
                lineNum += 1
            except Exception as ce:
                print 'CreatePoint.CreateFeature() || SetFieldValue() occur exception : %s.' % ce.message
    refCode = 4326
    DefineRef(destPath, sourName, refCode)
    feature.Destroy()
    ds.Destroy()
    print 'Create %s shpFile success' % destName


if __name__ == '__main__':

    dataSour = r"E:\data\XY"
    # 遍历的后缀可以是.dbf,.txt,xls,csv等等
    dataType = '.csv'
    xyFields = ['longitude', 'latitude']
    startTime = datetime.datetime.now()
    print "Python Tool Start,Time Is : ", startTime
    # 调用def
    fileList = os.listdir(dataSour)
    for f in fileList:
        if f.endswith(dataType):
            sour = os.path.join(dataSour, f)
            print 'Working file is %s.' % sour
            CreatePoint(sour, xyFields)
    endTime = datetime.datetime.now()
    print "Python Tool End,Time Spend Is:", (endTime - startTime)
