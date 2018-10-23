# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import sys
reload(sys)
sys.setdefaultencoding("utf8")

try:
    import ogr
    import gdal
except ImportError:
    from osgeo import ogr
    from osgeo import gdal

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/1/4"
__method__ = ["generator"]

gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "NO")
gdal.SetConfigOption("SHAPE_ENCODING", "")
ogr.RegisterAll()

driver = ogr.GetDriverByName('ESRI Shapefile')
shape = r"E:\data\qd_shp\train_station\3Mstation.shp"
ds = driver.Open(shape, 0)
if ds is None:
    print "could not open and over"
    sys.exit(1)

layer = ds.GetLayer(0)
lyrcount = layer.GetFeatureCount()
print 'feature count:', lyrcount

extent = layer.GetExtent()
print 'extent:', extent
print 'ul:', extent[0], extent[3]
print 'lr:', extent[1], extent[2]

feature = layer.GetNextFeature()
while feature is not None:
    name = feature.GetFieldAsString('name')
    print type(name)
    geom = feature.GetGeometryRef()
    x = str(geom.GetX())
    y = str(geom.GetY())
    print (name + ' ' + x + ' ' + y)

    # destroy the feature and get a new one
    feature.Destroy()
    feature = layer.GetNextFeature()


#
# json_file = os.path.abspath(os.path.join(os.path.dirname(shape), "qdxqcoord.js"))
# fw = codecs.open(json_file, mode="w", encoding="utf8", errors="strict", buffering=1)
# fw.write("var coords={")
#
# fields = ["name", "SHAPE@XY"]
# count = 1
# with arcpy.da.SearchCursor(shape, fields) as cursor:
#     for row in cursor:
#         name = row[0]
#         geom = list(row[1])
#         line = '"%s": %s' % (name, geom)
#         print line
#         fw.write("\n\t")
#         fw.write(line)
#         fw.write(",") if count < lyrcount else 0
#         count += 1
#     fw.write("\n")
#     fw.write("}")
#     fw.close()
#
# ds.Destroy()
# print "end"
#
