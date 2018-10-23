# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
   to generate linkgeo shapefile formnode, tonode, linkid

keyword:
    formnode, tonode, linkid

working:
    linkgeo generate to node
    node append nodeid
    check linkgeo fields: formnode, tonode, linkid, length
    if:
        calculate
    else:
        create
        calculate
    save shapefile

------------------------------------------------
"""
import os
import shutil
import types
import shelve
import simplejson

from decimal import Decimal

import arcpy

try:
    import gdal
    import ogr
except Exception:
    from osgeo import gdal
    from osgeo import ogr

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/7"

IS_NODEDIR = True
TIME_FORMAT = '%Y-%m-%d %H:%m:%s'
GDAL_FILENAME_CODE = "GDAL_FILENAME_IS_UTF8"
GDAL_SHAPE_CODE = "SHAPE_ENCODING"
DRIVER = "ESRI Shapefile"


class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args)

        return Singleton.__instance


class GEOMTYPE(object):
    POINT = ogr.wkbPoint
    POLYLINE = ogr.wkbLineString
    POLYGEN = ogr.wkbPolygon


class FEATURE_TYPE(object):
    POINT = 'Point'
    LINE = 'Polyline'
    POLYGEN = 'Polygon'


class FIELD_TYPE(object):
    """

    """
    INT = ogr.OFTInteger
    INT_LIST = ogr.OFTIntegerList
    REAL = ogr.OFTReal
    REAL_LIST = ogr.OFTRealList
    STRING = ogr.OFTString
    STRING_LIST = ogr.OFTStringList
    WIDESTRING = ogr.OFTWideString
    WIDESTRING_LIST = ogr.OFTWideStringList
    BINARY = ogr.OFTBinary
    DATE = ogr.OFTDate
    TIME = ogr.OFTTime
    DATETIME = ogr.OFTDateTime
    INT64 = ogr.OFTInteger64
    INT64_LIST = ogr.OFTInteger64List
    NONE = ogr.OFSTNone
    BOOL = ogr.OFSTBoolean
    INT16 = ogr.OFSTInt16
    FLOAT32 = ogr.OFSTFloat32


class Field(Singleton):
    # noinspection PyMissingConstructor
    def __init__(self):
        super(Field, self).__init__
        pass

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


def ftcount(feature):
    """
    statics feature count
    :param feature:
    :return: int count
    """
    assert isinstance(feature, basestring)

    pass



def ftype(feature):
    assert isinstance(feature, basestring)

    if os.path.exists(feature):
        desc = arcpy.Describe(feature)
        if hasattr(desc, 'shapeType'):
            dt = desc.shapeType
            return str(dt)
    else:
        emsg = Exception('feature %s in not exist' % feature)
        raise emsg


def gdal_init(nodedir):
    try:
        gdal.SetConfigOption(GDAL_FILENAME_CODE, "NO")
        gdal.SetConfigOption(GDAL_SHAPE_CODE, "")
        ogr.RegisterAll()
        driver = ogr.GetDriverByName(DRIVER)
        ds = driver.CreateDataSource(nodedir)
        return ds
    except Exception as e:
        raise Exception('gdal initialize failure')


def ftnode(feature, fields, is_nodedir, nodedir=None):
    """
    generator linkgeo shapefile node informations
    :param shape: linkgeo shapefile
    :param is_nodedir: is or not create node dir
    :param nodedir: node dir path, default is shapefile/shapefile_node
    :return: linkgeo shapefile node
    """
    ftp = ftype(feature)
    if ftp == FEATURE_TYPE.LINE or ftp == FEATURE_TYPE.POLYGEN:
        ftname = os.path.splitext(os.path.basename(feature))[0]
        nodename = ftname + '_node'
        if is_nodedir:
            nodedir = os.path.join(os.path.dirname(feature), ftname + '_node')
            nodedir = os.path.abspath(nodedir)
        else:
            if not nodedir:
                nodedir = os.path.abspath(nodedir)
            nodedir = os.path.abspath(os.path.dirname(feature))
        node = os.path.abspath(os.path.join(nodedir, nodename))

        # 存在将会被覆盖
        if os.path.exists(nodedir):
            print '%s is exist, remove dir' % nodedir
            shutil.rmtree(nodedir)
        os.mkdir(nodedir)

        ds = gdal_init(nodedir)
        layer = ds.CreateLayer(nodename, geom_type=GEOMTYPE.POINT)

        shedb = shelve.open('shelve.db', flag='c', protocol=2, writeback=False)
        alist = []
        adict = {}
        index = 0
        eventid = 0

        with arcpy.da.SearchCursor(feature, fields) as cursor:
            Field.addfield(layer, 'eventid', FIELD_TYPE.INT, 20)
            defn = layer.GetLayerDefn()
            feature = ogr.Feature(defn)
            for row in cursor:
                index += 1
                eventid += 1
                geoms = simplejson.loads(row[0])['paths']
                start = geoms[0][0]
                end = geoms[-1][-1]
                geom = (start, end)
                for g in geom:
                    x = float(Decimal.from_float(g[0]).quantize(Decimal('0.0000')))
                    y = float(Decimal.from_float(g[1]).quantize(Decimal('0.0000')))
                    g = (x, y)
                    if g not in alist:
                        adict[g] = index
                        Field.setvalue(feature, 'eventid', index)
                        point = ogr.Geometry(GEOMTYPE.POINT)
                        point.AddPoint(x, y)
                        feature.SetGeometry(point)
                        layer.CreateFeature(feature)
        return node
    else:
        emsg = Exception('feature %s type is %s not available' % (shape, ftp))
        print emsg
        return


def main(shape, fields):
    """
    pyscript main
    :param shape: linkgeo shapefile
    :return: if Ture else False
    """
    assert isinstance(shape, basestring)

    if not os.path.exists(shape):
        print 'shape %s is not exist' % shape
    if not os.path.isfile(shape) and shape.endswith('%.shp'):
        print 'shape %s is not shapefile' % shape
    node = ftnode(shape, fields, is_nodedir=IS_NODEDIR, nodedir=None)



if __name__ == '__main__':
    fields = ['SHAPE@JSON']
    shape = r'E:\data\ty\ty_test\linkgeo_ZZ.shp'
    main(shape, fields)
