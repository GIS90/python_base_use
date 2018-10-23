# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
use esri geomtry js file to generate esri shapefile

working:
    analysis js file
    initialize gdal
    create define field
    set field value
    generate polgen
    feature set geometry(polygen)
    feature append layer

model:
    Singleton model
------------------------------------------------
"""
import datetime
import os
import shutil

import simplejson

try:
    import gdal
    import ogr
except ImportError:
    from osgeo import gdal
    from osgeo import ogr

import sys

reload(sys)
sys.setdefaultencoding('utf8')

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/7"

GDAL_FILENAME_CODE = "GDAL_FILENAME_IS_UTF8"
GDAL_SHAPE_CODE = "SHAPE_ENCODING"
DRIVER = "ESRI Shapefile"


class GEOMTYPE(object):
    POINT = ogr.wkbPoint
    POLYLINE = ogr.wkbLineString
    POLYGEN = ogr.wkbPolygon


class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args)
            return Singleton.__instance


class Field(Singleton):
    def __new__(cls, *args, **kwargs):
        pass

    @staticmethod
    def addfield(layer, name, ftype, width):
        try:
            defn = ogr.FieldDefn(name, ftype)
            defn.SetWidth(width)
            layer.CreateField(defn)
        except Exception as e:
            raise Exception('addfield is error: %s' % e.message)

    @staticmethod
    def setvalue(feat, name, value):
        try:
            feat.SetField(name, value)
        except Exception as e:
            raise Exception('setvalue is error: %s' % e.message)


def get_file_json(js):
    try:
        with open(jsfile, 'r') as f:
            jsdata = f.read()
            jsdict = simplejson.loads(jsdata)
            return jsdict
    except IOError as e:
        raise Exception('get_file_json IOError is error: %s' % e.message)
    except Exception as e:
        raise Exception('get_file_json Exception is error: %s' % e.message)


def main(jsfile):
    if not os.path.exists(jsfile):
        raise Exception('%s is not exist' % jsfile)
    if not os.path.isfile(jsfile) or jsfile.endswith('*.js'):
        raise Exception('%s is not available js file' % jsfile)

    jsdict = get_file_json(jsfile)

    jspath = os.path.split(jsfile)[0]
    jsname = os.path.split(jsfile)[1]
    shpname = os.path.splitext(jsname)[0]
    shpath = os.path.join(jspath, os.path.splitext(jsname)[0] + '_shp')
    if os.path.exists(shpath):
        print '%s is exist, deleting file.' % shpath
        shutil.rmtree(shpath)
        os.makedirs(shpath)
    else:
        print '%s is not exist, making dirs.' % shpath
        os.makedirs(shpath)

    gdal_init()
    def gdal_init():
        try:
            gdal.SetConfigOption(GDAL_FILENAME_CODE, "NO")
            gdal.SetConfigOption(GDAL_SHAPE_CODE, "")
            ogr.RegisterAll()
        except Exception as e:
            raise Exception('gdal initialize failure')

    driver = ogr.GetDriverByName(DRIVER)
    ds = driver.CreateDataSource(shpath)
    layer = ds.CreateLayer(shpname, geom_type=GEOMTYPE.POLYGEN)

    ftcount = len(jsdict['features'])
    for index in range(0, ftcount, 1):
        name = (jsdict['features'][index]['properties']['name']).encode('gbk')
        geoms = str(jsdict['features'][index]['geometry']['coordinates'][0])
        geojson = """{"type":"Polygon","coordinates": %s}""" % geoms

        print index, ": %s" % name.decode('gbk')

        if index == 0:
            Field.addfield(layer, 'name', ogr.OFTString, 40)
            defn = layer.GetLayerDefn()
            feature = ogr.Feature(defn)
        else:
            Field.setvalue(feature, 'name', name)
            polygen = ogr.CreateGeometryFromJson(geojson)
            feature.SetGeometry(polygen)
            layer.CreateFeature(feature)


if __name__ == '__main__':

    jsfile = r'E:\data\jn\jining1.js'
    startime = datetime.datetime.now()
    print "start time is : ", startime
    # 调用def
    try:
        main(jsfile)
    except Exception as e:
        print 'main is error: %s, advance exit' % e.message
        sys.exit(1)
    endtime = datetime.datetime.now()
    print "speed time is:", (endtime - startime)
