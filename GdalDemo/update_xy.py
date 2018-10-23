# - * - coding: utf-8 -
import datetime
import time

from osgeo import gdal
from osgeo import ogr

start = time.time()
gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
gdal.SetConfigOption("SHAPE_ENCODING", "")


# Add x,y filed
def createFiled(Layer, filed, type):
    fd = ogr.FieldDefn(filed, type)
    Layer.CreateField(fd)


def updateXY(inLayer, inShapefile):
    # Add input Layer Fields to the output Layer if it is the one we want
    count = 0
    for inFeature in inLayer:
        geom = inFeature.GetGeometryRef()
        centroid = geom.Centroid()
        centroid_x = centroid.GetX()
        centroid_y = centroid.GetY()
        inFeature.SetField(xfiled, centroid_x)
        inFeature.SetField(yfiled, centroid_y)
        inLayer.SetFeature(inFeature)
        count += 1
        print count, centroid_x, centroid_y
    print count
    # Close DataSources
    inDataSource.Destroy()


# Get the input Layer
file = r'E:\data\json\Export_Output.shp'
inDriver = ogr.GetDriverByName("ESRI Shapefile")
inDataSource = inDriver.Open(file, 1)
inLayer = inDataSource.GetLayer()
xfiled = "centroid_x"
yfiled = "centroid_y"
type = ogr.OFTReal
createFiled(inLayer, xfiled, type)
createFiled(inLayer, yfiled, type)
updateXY(inLayer, file)
end = time.time()
usingtime = end - start
print(datetime.timedelta(seconds=usingtime))
