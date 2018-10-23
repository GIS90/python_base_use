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
import sys
import arcpy
import simplejson

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


class FEATURE(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        pass

    def __str__(self):
        return 'feature'

    @staticmethod
    def count(feature):
        """
        statics feature count
        :param feature:
        :return: int count
        """
        assert isinstance(feature, basestring)

        count = 0
        with arcpy.da.SearchCursor(feature, ["SHAPE@"]) as cursor:
            for _ in cursor:
                count += 1
        return count

    @staticmethod
    def type(feature):
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


def ftnode(feature, is_nodedir, nodedir=None):
    """
    generator linkgeo shapefile node informations
    :param shape: linkgeo shapefile
    :param is_nodedir: is or not create node dir
    :param nodedir: node dir path, default is shapefile/shapefile_node
    :return: linkgeo shapefile node
    """
    ftp = FEATURE.type(feature)
    if ftp == FEATURE_TYPE.LINE or ftp == FEATURE_TYPE.POLYGEN:
        ftname = os.path.splitext(os.path.basename(feature))[0]
        nodename = ftname + '_node'
        if is_nodedir:
            nodedir = os.path.join(os.path.dirname(feature), ftname + '_node')
            nodedir = os.path.abspath(nodedir)
        else:
            nodedir = os.path.abspath(nodedir)
        node = os.path.abspath(os.path.join(nodedir, nodename))

        # 存在将会被覆盖
        if os.path.exists(nodedir):
            print '%s is exist, remove dir' % nodedir
            shutil.rmtree(nodedir)
        os.mkdir(nodedir)

        ds = gdal_init(nodedir)
        layer = ds.CreateLayer(nodename, geom_type=GEOMTYPE.POINT)
        with arcpy.da.SearchCursor(feature, 'SHAPE@JSON') as cursor:
            GField.addfield(layer, 'nodeid', GFIELD_TYPE.INT, 20)
            defn = layer.GetLayerDefn()
            feature = ogr.Feature(defn)
            nodeid = 0
            alist = []
            for row in cursor:
                nodeid += 1
                geoms = simplejson.loads(row[0])['paths']
                start = geoms[0][0]
                end = geoms[-1][-1]
                geom = (start, end)
                for g in geom:
                    x = g[0]
                    y = g[1]
                    if g not in alist:
                        GField.setvalue(feature, 'nodeid', nodeid)
                        point = ogr.Geometry(GEOMTYPE.POINT)
                        point.AddPoint(x, y)
                        feature.SetGeometry(point)
                        layer.CreateFeature(feature)
        return node
        # arcpy.env.workspace = nodedir
        # try:
        #     arcpy.FeatureVerticesToPoints_management(in_features=feature,
        #                                              out_feature_class=node,
        #                                              point_location=VERT_TYPE.BOTH_ENDS)
        # except Exception as e:
        #     fv_emsg = 'ftnode FeatureVerticesToPoints_management is error: %s' % e.message
        #     raise Exception(fv_emsg)
        # else:
        #     try:
        #         arcpy.DeleteIdentical_management(in_dataset=node,
        #                                          fields=["Shape"],
        #                                          xy_tolerance="",
        #                                          z_tolerance="0")
        #
        #     except Exception as e:
        #         del_emsg = 'ftnode DeleteIdentical_management is error: %s' % e.message
        #         raise Exception(del_emsg)
        #     else:
        #         nodecount = FEATURE.count(node)
        #         print 'node count is %d' % nodecount
        #         return node
    else:
        emsg = Exception('feature %s type is %s not available' % (shape, ftp))
        print emsg
        return


def nodedict(node, shedb=None):
    """
    get node geomtry informations to dict
    :param node:
    :param shedb
    :return: node dict
    """
    adict = {}
    with arcpy.da.SearchCursor(node, ['nodeid', 'SHAPE@JSON']) as cursor:
        for row in cursor:
            nodeid = int(row[0])
            geoms = simplejson.loads(row[1])
            x = geoms['x']
            y = geoms['y']
            geom = [x, y]
            adict[nodeid] = geom
        return adict if adict else None


def main(shape):
    """
    pyscript main
    :param shape: linkgeo shapefile
    :return: if Ture else False
    """
    assert isinstance(shape, basestring)

    if not os.path.exists(shape):
        print 'shape %s is not exist' % shape
        sys.exit(1)
    if not os.path.isfile(shape) and shape.endswith('%.shp'):
        print 'shape %s is not shapefile' % shape
        sys.exit(1)

    if shape:
        field = Field(shape)
        field.create('linkid', FIELD_TYPE.LONG, 8)
        field.create('fromnode', FIELD_TYPE.LONG, 8)
        field.create('tonode', FIELD_TYPE.LONG, 8)
        field.create('length', FIELD_TYPE.DOUBLE, 20, 8)
        with arcpy.da.UpdateCursor(shape, ('linkid')) as cursor:
            linkid = 0
            for row in cursor:
                row[0] = linkid + 1000
                cursor.updateRow(row)
                linkid += 1
    else:
        emsg = Exception('error: main shape')
        raise emsg

    node = ftnode(shape, is_nodedir=IS_NODEDIR, nodedir=None)

    if node:
        field = Field(node)
        field.create('nodeid', FIELD_TYPE.LONG, 8)
        field.exclude('nodeid')
        with arcpy.da.UpdateCursor(node, ('nodeid')) as cursor:
            nodeid = 0
            for row in cursor:
                row[0] = nodeid + 1000
                cursor.updateRow(row)
                nodeid += 1
        # curdir = os.path.dirname(node)
        # shepath = os.path.abspath(os.path.join(curdir, 'shelve.db'))
        # shedb = shelve.open(shepath, flag='c', protocol=2, writeback=False)
    else:
        emsg = Exception('error: main node')
        raise emsg

    # start
    with arcpy.da.UpdateCursor(shape, ('fromnode', 'tonode', 'SHAPE@JSON', 'linkid')) as cursor:
        for row in cursor:
            geoms = simplejson.loads(row[2])['paths']
            start = geoms[0][0]
            end = geoms[-1][-1]
            print '--------------%d' % row[3]
            print 'start:', start
            print 'end:', end
            with arcpy.da.UpdateCursor(node, ('nodeid', 'SHAPE@JSON')) as nodecursor:
                for noderow in nodecursor:
                    nodeid = noderow[0]
                    nodegeom = simplejson.loads(nodecursor[1])
                    nodegeom = [nodegeom['x'], nodegeom['y']]

                    if start == nodegeom:
                        row[0] = nodeid
                        print 'start        ', nodeid, nodegeom
                    if end == nodegeom:
                        row[1] = nodeid
                        print 'end        ', nodeid, nodegeom
            cursor.updateRow(row)




if __name__ == '__main__':
    shape = r'E:\data\ty\ty_test\linkgeo_ZZ.shp'
    main(shape)
