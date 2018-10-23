# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import os

import arcpy

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/11"


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

    @staticmethod
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
