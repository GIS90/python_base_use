# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    core module
------------------------------------------------
"""

try:
    import gdal
    import ogr
except Exception:
    from osgeo import gdal
    from osgeo import ogr

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/11"


class Singletone(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Singletone.__instance is None:
            Singletone.__instance = object.__new__(cls, *args)

        return Singletone.__instance


class VERT_TYPE(object):
    """
    ALL: every feature break ponit to generate node
    MID: every feature mid ponit to generate node
    START: every feature start ponit to generate node
    END: every feature end ponit to generate node
    BOTH_ENDS: every feature start ponit and end point to generate node
    DANGLE:
    dealut is all
    """
    All = 'ALL'
    MID = 'MID'
    START = 'START'
    END = 'END'
    BOTH_ENDS = 'BOTH_ENDS'
    DANGLE = 'DANGLE'


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
    TEXT —名称或其他文本特性。
    FLOAT —特定范围内含小数值的数值。
    DOUBLE —特定范围内含小数值的数值。
    SHORT —特定范围内不含小数值的数值；编码值。
    LONG —特定范围内不含小数值的数值。
    DATE —日期和/或时间。
    BLOB —影像或其他多媒体。
    RASTER —栅格影像。
    GUID —GUID 值
    """
    TEXT = 'TEXT'
    FLOAT = 'FLOAT'
    DOUBLE = 'DOUBLE'
    SHORT = 'SHORT'
    LONG = 'LONG'
    DATE = 'DATE'
    BLOB = 'BLOB'
    RASTER = 'RASTER'
    GUID = 'GUID'


class GFIELD_TYPE(object):
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
