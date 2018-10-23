#- * - coding : utf-8 - * -


#ArcGIS Python Tool������Ƭ���淽��
#�õ�����Ҫ���ܺ�����ManageTileCache



import os
import sys
import arcpy
import datetime


scheme_starttime=datetime.datetime.now()



print "GenerateTileCacheTilingScheme Python Tool Start Executing,Start Time is:",scheme_starttime

#���ù����ռ�
workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace




#��������
for mxd in arcpy.ListFiles("*.mxd"):
      in_dataset=mxd
      #�������Ƽ����·����һ��������Ƭ��
      out_tiling_scheme="D:/map_Services/Tilingscheme.xml"
      #����PREDEFINED���½�NEW
      tiling_scheme_generation_method="PREDEFINED"
      number_of_scales="12"
      #����ArcGIS_Online_Bing_Maps_Google_Maps��׼������
      predefined_tiling_scheme=r"D:\map_Services\ArcGIS_Online_Bing_Maps_Google_Maps.xml"
      scales="#"
      scales_type="SCALE"
      #��Ƭ����ԭ��-���Ͻ�
      tile_origin="119 29"
      #ר������豸��ÿӢ�����
      dpi=96
      #������Ƭ�Ŀ�Ⱥ͸߶ȣ�������Ϊ��λ��
      tile_size="256 x 256"
      #Ϊ�����е���Ƭѡ�� PNG��PNG8��PNG24��PNG32��JPEG �� MIXED �ļ���ʽ,Ĭ������Ϊ MIXED
      tile_format="PNG"
      #��� JPEG �� MIXED ѹ����������һ������ 1 �� 100 ֮���ֵ,Ĭ��ֵΪ 75
      tile_compression_quality="75"
      #ȷ����Ƭ�Ĵ洢��ʽ,COMPACT&EXPLODED,Ĭ�ϴ洢��ʽΪ���� (COMPACT)
      storage_format="COMPACT"
      
      print "Parameter Set Up OK,Executing��Please Waite For You........."
      print "------------------------------------------------------------------------------------"
      print "MapCacheTileScheme Information is:"
      print "Map mxd is:",in_dataset
      print "out_tiling_scheme is:",out_tiling_scheme
      print "tiling_scheme_generation_method is:",tiling_scheme_generation_method
      print "number_of_scales is:",number_of_scales
      print "predefined_tiling_scheme is:",predefined_tiling_scheme
      print "tile_origin is:",tile_origin
      print "dpi is:",dpi
      print "tile_size is:",tile_size
      print "tile_format is:",tile_format
      print "tile_compression_quality is:",tile_compression_quality
      print "storage_format is:",storage_format
      print "------------------------------------------------------------------------------------"


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


      scheme_endtime=datetime.datetime.now()
      print "GenerateTileCacheTilingScheme Python Tool Executed Time Cost is :",(scheme_endtime-scheme_starttime)

      for i in range(1,10,1):
            print ""
      


      cache_starttime=datetime.datetime.now()
      print "ManageTileCache Python Tool Start Executing,Start Time is:",cache_starttime
    
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
      scales="591657527.591555,295828763.795777,147914381.897889,73957190.948944,36978595.474472,18489297.737236,9244648.868618,4622324.434309,2311162.217155,1155581.108577,577790.554289,288895.277144,144447.638572,72223.819286,36111.909643,18055.954822,9027.977411,4513.988705,2256.994353,1128.497176"
      #�������Ȥ���ԶԽ�������ɾ������Ƭ����Լ��
      area_of_interest="#"
      max_cellsize = "#"
      #��С����������������ɻ���ʱ��ʹ�õı���
      min_cachedscale = "4622324.434309"
      #��󻺴�������������ɻ���ʱ��ʹ�õı���
      max_cachedscale = "577790.554289"

      print "Parameter Set Up OK,Executing��Please Waite For You........."
      print "------------------------------------------------------------------------------------"
      print "Cache Information is:"
      print "Map mxd is:",in_dataset
      print "in_cache_location is:",in_cache_location
      print "manage_mode is:",manage_mode
      print "tiling_scheme is:",tiling_scheme
      print "import_tiling_scheme is:",import_tiling_scheme
      print "scales is:",scales
      print "min_cachedscale is:",min_cachedscale
      print "max_cachedscale is:",max_cachedscale
      print "------------------------------------------------------------------------------------"

      arcpy.ManageTileCache_management(in_cache_location,
                                       manage_mode,
                                       in_cache_name,
                                       in_dataset,
                                       tiling_scheme,
                                       import_tiling_scheme,
                                       scales,
                                       area_of_interest,
                                       max_cellsize,
                                       min_cachedscale,
                                       max_cachedscale)



      cache_endtime=datetime.datetime.now()
      print "ManageTileCache Python Tool Executed Time Cost is :",(cache_endtime-cache_starttime)





print "All Success,Time is :",(cache_endtime-scheme_starttime)











