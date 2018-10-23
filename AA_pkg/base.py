# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/8/5'
"""
import arcpy
import simplejson


try:
    import gdal
    import ogr
except Exception:
    from osgeo import gdal
    from osgeo import ogr

shape = r'E:\data\ty\ty_test\linkgeo_ZZ.shp'
dir = r'E:\data\ty\ty_test'
fields = ['SHAPE@JSON']
with arcpy.da.SearchCursor(shape, fields) as cursor:
    for row in cursor:
        geoms = simplejson.loads(row[0])['paths']
        print type(geoms), geoms[0][0], geoms[-1][-1]

        gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
        gdal.SetConfigOption("SHAPE_ENCODING", "")
        ogr.RegisterAll()
        driver = ogr.GetDriverByName('ESRI Shapefile')
        ds = driver.CreateDataSource(dir)
        shpLayer = ds.CreateLayer('nodenode', geom_type=ogr.wkbPoint)
        defn = shpLayer.GetLayerDefn()
        feature = ogr.Feature(defn)
        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(float(geoms[0][0][0]), float(geoms[0][0][1]))
        feature.SetGeometry(point)
        shpLayer.CreateFeature(feature)

        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(float(geoms[-1][-1][0]), float(geoms[-1][-1][1]))
        feature.SetGeometry(point)
        shpLayer.CreateFeature(feature)

        feature.Destroy()
        ds.Destroy()

