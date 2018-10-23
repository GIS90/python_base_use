#- * - coding : utf-8 - * -


#ArcGIS Python Tool生成切片缓存方案
#用到的主要功能函数是ManageTileCache



import os
import sys
import arcpy
import datetime


starttime=datetime.datetime.now()



print "ManageTileCache Python Tool Start Executing,Start Time is:",starttime

#设置工作空间
workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace


#参数设置
for mxd in arcpy.ListFiles("*.mxd"):
      in_datasource=mxd





      
      #缓存存放路径
      in_cache_location=r"D:\arcgisserver\directories\arcgiscache"
      #缓存的三种管理模式：RECREATE_ALL_TILES，RECREATE_EMPTY_TILES，DELETE_TILES 
      manage_mode="RECREATE_ALL_TILES"
      #缓存的名称，与发布的服务保持一致
      in_cache_name="WZ_Map_Server"
      #切片方案：标准切片方案ARCGISONLINE_SCHEME，或者指定引入IMPORT_SCHEME
      tiling_scheme="IMPORT_SCHEME"
      #引入切片方案的路径，就是上面生成的切片方案
      import_tiling_scheme="D:/map_Services/Tilingscheme.xml"
      scales="591657527.591555,295828763.795777,147914381.897889,73957190.948944,36978595.474472,18489297.737236,9244648.868618,4622324.434309,2311162.217155,1155581.108577,577790.554289,288895.277144"
      area_of_interest="#"
      max_cellsize = "#"
      min_cachedscale = "591657527.591555"
      max_cachedscale = "288895.277144"

print "Parameter Set Up OK,Executing，Please Waite For You........."
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









