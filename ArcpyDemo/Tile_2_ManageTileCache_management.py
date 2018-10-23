#- * - coding : utf-8 - * -


#ArcGIS Python Tool������Ƭ���淽��
#�õ�����Ҫ���ܺ�����ManageTileCache



import os
import sys
import arcpy
import datetime


starttime=datetime.datetime.now()



print "ManageTileCache Python Tool Start Executing,Start Time is:",starttime

#���ù����ռ�
workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace


#��������
for mxd in arcpy.ListFiles("*.mxd"):
      in_datasource=mxd





      
      #������·��
      in_cache_location=r"D:\arcgisserver\directories\arcgiscache"
      #��������ֹ���ģʽ��RECREATE_ALL_TILES��RECREATE_EMPTY_TILES��DELETE_TILES 
      manage_mode="RECREATE_ALL_TILES"
      #��������ƣ��뷢���ķ��񱣳�һ��
      in_cache_name="WZ_Map_Server"
      #��Ƭ��������׼��Ƭ����ARCGISONLINE_SCHEME������ָ������IMPORT_SCHEME
      tiling_scheme="IMPORT_SCHEME"
      #������Ƭ������·���������������ɵ���Ƭ����
      import_tiling_scheme="D:/map_Services/Tilingscheme.xml"
      scales="591657527.591555,295828763.795777,147914381.897889,73957190.948944,36978595.474472,18489297.737236,9244648.868618,4622324.434309,2311162.217155,1155581.108577,577790.554289,288895.277144"
      area_of_interest="#"
      max_cellsize = "#"
      min_cachedscale = "591657527.591555"
      max_cachedscale = "288895.277144"

print "Parameter Set Up OK,Executing��Please Waite For You........."
print "------------------------------------------------------------------------------------"
print "Cache Information is:"
print "Map mxd is:",in_datasource
print "in_cache_location is:",in_cache_location
print "manage_mode is:",manage_mode
print "tiling_scheme mxd is:",tiling_scheme
print "import_tiling_scheme is:",import_tiling_scheme
print "scales is:",scales
print "min_cachedscalemxd is:",min_cachedscale
print "max_cachedscale is:",max_cachedscale
print "------------------------------------------------------------------------------------"

arcpy.ManageTileCache_management(in_cache_location,
                                 manage_mode,
                                 in_cache_name,
                                 in_datasource,
                                 tiling_scheme,
                                 import_tiling_scheme,
                                 scales,
                                 area_of_interest,
                                 max_cellsize,
                                 min_cachedscale,
                                 max_cachedscale)



endtime=datetime.datetime.now()
print "ManageTileCache Python Tool Executed Time Cost is :",(endtime-starttime)



print "OK-------------MapCacheTile Success!!!!!"









