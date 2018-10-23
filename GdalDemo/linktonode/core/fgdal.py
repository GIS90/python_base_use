# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import os

try:
    import gdal
    import ogr
except Exception:
    from osgeo import gdal
    from osgeo import ogr

GDAL_FILENAME_CODE = "GDAL_FILENAME_IS_UTF8"
GDAL_SHAPE_CODE = "SHAPE_ENCODING"
DRIVER = "ESRI Shapefile"


def gdal_init(nodedir):
    assert isinstance(nodedir, basestring)

    try:
        gdal.SetConfigOption(GDAL_FILENAME_CODE, "NO")
        gdal.SetConfigOption(GDAL_SHAPE_CODE, "")
        ogr.RegisterAll()
        driver = ogr.GetDriverByName(DRIVER)
        ds = driver.CreateDataSource(nodedir)
        return ds
    except Exception as e:
        raise Exception('gdal initialize failure')
