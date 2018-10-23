# -*- coding: utf-8 -*-
import os
import sys

from osgeo import gdal
from osgeo import ogr

gdal.SetConfigOption("SHAPE_ENCODING", "")
gdal.SetConfigOption("GDAL_DISABLE_CPLLOCALEC", "YES")


def main(inShapefile):
    # Get the input Layer

    inDriver = ogr.GetDriverByName("ESRI Shapefile")
    inDataSource = inDriver.Open(inShapefile, 0)
    inLayer = inDataSource.GetLayer()
    # inLayer.SetAttributeFilter("minor = 'HYDR'")

    # Create the output LayerS
    outputName = os.path.splitext(os.path.split(inShapefile)[1])[0] + ".tab"
    print outputName
    outShapefile = os.path.join(os.path.split(inShapefile)[0], outputName)
    outDriver = ogr.GetDriverByName("MapInfo File")

    # Remove output shapefile if it already exists
    if os.path.exists(outShapefile):
        outDriver.DeleteDataSource(outShapefile)

    # Create the output shapefile
    outDataSource = outDriver.CreateDataSource(outShapefile)
    out_lyr_name = os.path.splitext(os.path.split(outShapefile)[1])[0]
    outLayer = outDataSource.CreateLayer(out_lyr_name, geom_type=ogr.wkbPolygon)

    # Add input Layer Fields to the output Layer if it is the one we want
    type = ogr.OFTInteger64
    inLayerDefn = inLayer.GetLayerDefn()
    for i in range(0, inLayerDefn.GetFieldCount()):
        fieldDefn = inLayerDefn.GetFieldDefn(i)
        fieldName = fieldDefn.GetName()
        if fieldName in ("OBJECTID", "FID", "totcnt"):
            fieldDefn = ogr.FieldDefn(fieldName, type)

        outLayer.CreateField(fieldDefn)

    # Get the output Layer's Feature Definition
    outLayerDefn = outLayer.GetLayerDefn()
    j = 1
    # Add features to the ouput Layer
    for inFeature in inLayer:
        # Create output Feature
        outFeature = ogr.Feature(outLayerDefn)

        # Add field values from input Layer
        for i in range(0, outLayerDefn.GetFieldCount()):
            fieldDefn = outLayerDefn.GetFieldDefn(i)
            field = fieldDefn.GetNameRef()
            # ,"score_weak","score_cdfg"
            fieldName = fieldDefn.GetName()
            value = inFeature.GetField(i + 1)
            # print fieldName,i,value

            if fieldName == "score_weak" and value is None:
                value = 0.0
            if fieldName == "city":
                value = value.decode('utf8').encode("gb2312")
            outFeature.SetField(field, value)
        print j
        j = j + 1
        # Set geometry as centroid
        geom = inFeature.GetGeometryRef()
        # print geom.ExportToWkt()
        # newgeo=ogr.CreateGeometryFromWkt(geom.ExportToWkt())
        outFeature.SetGeometryDirectly(geom.Clone())
        # Add new feature to output Layer
        outLayer.CreateFeature(outFeature)
        outLayer.SyncToDisk()

    # Close DataSources
    inDataSource.Destroy()
    outDataSource.Destroy()


if __name__ == '__main__':
    inShapefile = r'E:\data\wz\region\region.shp'
    main(inShapefile)
