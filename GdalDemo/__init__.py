from osgeo import ogr
from osgeo import gdal

path_to_shp_data = r'E:\data\nj_js\zq_shp\NJ_ZQ.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(path_to_shp_data, 1)
layer = dataSource.GetLayer()
new_field = ogr.FieldDefn("Area", ogr.OFTReal)
new_field.SetWidth(32)
new_field.SetPrecision(20) #added line to set precision
layer.CreateField(new_field)

for feature in layer:
    geom = feature.GetGeometryRef()
    area = geom.GetArea()
    print area
    feature.SetField("Area", area)
    layer.SetFeature(feature)