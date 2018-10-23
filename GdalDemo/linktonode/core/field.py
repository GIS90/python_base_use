# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import os
import types

import arcpy

try:
    import gdal
    import ogr
except Exception:
    from osgeo import gdal
    from osgeo import ogr

from define import Singletone

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/11"


class Field(Singletone):
    """
    shapefile fields operation
    """

    def __init__(self, feature):
        super(Field, self).__init__()
        self.feature = feature
        self.fields = self.__fields()

    def __fields(self):
        fields = []
        fieldlist = arcpy.ListFields(self.feature)
        for field in fieldlist:
            fields.append(field.name)
        return fields if fields else None

    def create(self, key, ftype, width, precision=""):
        """
        create feature field
        :param key: feature field name
        :param ftype: feature field type
        :param width: feature field length
        :param precision: feature field scale
        :return:
        """
        assert isinstance(key, basestring)
        assert isinstance(ftype, basestring)

        fields = self.fields
        featname = os.path.basename(self.feature)

        for field in fields:
            if str(field).lower() == key:
                print '%s is contain "%s" field' % (featname, key)
                return

        if not isinstance(type(width), types.IntType):
            width = str(width)
        if not isinstance(type(precision), types.IntType):
            width = str(precision)

        try:
            arcpy.AddField_management(in_table=self.feature,
                                      field_name=key,
                                      field_type=ftype,
                                      field_precision=width,
                                      field_scale=precision)
        except Exception as e:
            emsg = "Field.create is error: %s" % e.message
            raise Exception(emsg)
        else:
            print '%s is create "%s" field' % (featname, key)


    def delete(self, key):
        assert isinstance(key, basestring)

        keys = []
        featname = os.path.basename(self.feature)
        if key not in self.fields:
            print '%s delete "%s" field is null' % (featname, key)
            return
        if not isinstance(type(key), types.ListType):
            keys.append(key)
        try:
            arcpy.DeleteField_management(in_table=self.feature,
                                         drop_field=keys)
            print '%s is delete "%s" field' % (featname, key)
        except Exception as e:
            emsg = "Field.delete is error: %s" % e.message
            raise Exception(emsg)

    def exclude(self, key):
        assert isinstance(key, basestring)

        for field in self.fields:
            if field not in [key, 'FID', 'Shape']:
                self.delete(field)
            else:
                pass

    def setvalue(self, key, value):
        pass


class GField(Singletone):
    # noinspection PyMissingConstructor
    def __init__(self):
        super(GField, self).__init__
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
