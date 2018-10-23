#- * - coding : utf-8 - * -


#ArcGIS Python Tool生成切片缓存方案，为生成切片做准备
#用到的主要功能函数是GenerateTileCacheTilingScheme



import os
import sys
import arcpy
import datetime


starttime=datetime.datetime.now()



print "GenerateTileCacheTilingScheme Python Tool Start Executing,Start Time is:",starttime

#设置工作空间
workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace

#参数设置
for mxd in arcpy.ListFiles("*.mxd"):
      in_dataset=mxd
      #方案名称及存放路径，一会生成切片用
      out_tiling_scheme="D:/map_Services/Tilingscheme_1.xml"
      #引用PREDEFINED，新建NEW
      tiling_scheme_generation_method="NEW"
      number_of_scales="7"
      #引用ArcGIS_Online_Bing_Maps_Google_Maps标准比例尺
      predefined_tiling_scheme="#"
      scales="250000;125000;62499;31249;15624;7812;4000"
      scales_type="SCALE"
      tile_origin="-400 400"
      dpi=96
      tile_size="256 x 256"
      tile_format="PNG32"
      tile_compression_quality="75"
      storage_format="COMPACT"


print "Parameter Set Up OK,Executing，Please Waite For You........."
arcpy.GenerateTileCacheTilingScheme_management(in_dataset,
                                               out_tiling_scheme,
                                               tiling_scheme_generation_method,
                                               number_of_scales,
                                               predefined_tiling_scheme,
                                               scales,
                                               scales_type,
                                               tile_origin,
                                               dpi,
                                               tile_size,
                                               tile_format,
                                               tile_compression_quality,
                                               storage_format)


endtime=datetime.datetime.now()
print "GenerateTileCacheTilingScheme Python Tool Executed Time Cost is :",(endtime-starttime)





