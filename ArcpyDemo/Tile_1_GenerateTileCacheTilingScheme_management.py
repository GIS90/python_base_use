#- * - coding : utf-8 - * -


#ArcGIS Python Tool������Ƭ���淽����Ϊ������Ƭ��׼��
#�õ�����Ҫ���ܺ�����GenerateTileCacheTilingScheme



import os
import sys
import arcpy
import datetime


starttime=datetime.datetime.now()



print "GenerateTileCacheTilingScheme Python Tool Start Executing,Start Time is:",starttime

#���ù����ռ�
workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace

#��������
for mxd in arcpy.ListFiles("*.mxd"):
      in_dataset=mxd
      #�������Ƽ����·����һ��������Ƭ��
      out_tiling_scheme="D:/map_Services/Tilingscheme_1.xml"
      #����PREDEFINED���½�NEW
      tiling_scheme_generation_method="NEW"
      number_of_scales="7"
      #����ArcGIS_Online_Bing_Maps_Google_Maps��׼������
      predefined_tiling_scheme="#"
      scales="250000;125000;62499;31249;15624;7812;4000"
      scales_type="SCALE"
      tile_origin="-400 400"
      dpi=96
      tile_size="256 x 256"
      tile_format="PNG32"
      tile_compression_quality="75"
      storage_format="COMPACT"


print "Parameter Set Up OK,Executing��Please Waite For You........."
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





