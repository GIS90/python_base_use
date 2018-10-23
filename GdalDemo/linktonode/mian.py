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
import sys

import arcpy
import simplejson

try:
    import gdal
    import ogr
except Exception:
    from osgeo import gdal
    from osgeo import ogr

from core.define import *
from core.feature import *
from core.fgdal import *
from core.field import *



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
