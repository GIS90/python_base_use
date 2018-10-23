# - * - coding: utf-8 - * -

import sys

try:
    from osgeo import ogr
except ImportError as e:
    import ogr

driver = ogr.GetDriverByName('ESRI ShapeFile')
shpFile = r'E:\data\wz\Linkgeo_new\LinkGeo_SDE.shp'
dataSource = driver.Open(shpFile, 0)
if dataSource is None:
    print 'Could Not Open .'
    sys.exit(1)

layer = dataSource.GetLayer()
print dataSource.GetLayer().GetFeatureCount()
n = layer.GetFeatureCount()
print n
extent = layer.GetExtent()
print 'extent : ', extent

# feat = layer.GetFeature(5)
# print feat
# fieldValue =  feat.GetField('ID')
# print fieldValue
# # for i in range(1,layer.GetFeatureCount(),1):
#     # print layer.GetNextFeature().GetField('ID')
# layer.ResetReading()
#
# geom = feat.GetGeometryRef()
# # print geom.GetX()
# # print geom.GetY()
# print geom
# feat.Destroy()
# dataSource.Destroy()
