#- * - coding : utf-8 - * -


#ArcGIS Python Tool生成切片缓存方案
#用到的主要功能函数是ManageTileCache



import os
import sys
import arcpy
import datetime


scheme_starttime=datetime.datetime.now()



print "GenerateTileCacheTilingScheme Python Tool Start Executing,Start Time is:",scheme_starttime

#设置工作空间
workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace




#参数设置
for mxd in arcpy.ListFiles("*.mxd"):
      in_dataset=mxd
      #方案名称及存放路径，一会生成切片用
      out_tiling_scheme="D:/map_Services/Tilingscheme.xml"
      #引用PREDEFINED，新建NEW
      tiling_scheme_generation_method="PREDEFINED"
      number_of_scales="12"
      #引用ArcGIS_Online_Bing_Maps_Google_Maps标准比例尺
      predefined_tiling_scheme=r"D:\map_Services\ArcGIS_Online_Bing_Maps_Google_Maps.xml"
      scales="#"
      scales_type="SCALE"
      #切片方案原点-左上角
      tile_origin="119 29"
      #专用输出设备的每英寸点数
      dpi=96
      #缓存切片的宽度和高度（以像素为单位）
      tile_size="256 x 256"
      #为缓存中的切片选择 PNG、PNG8、PNG24、PNG32、JPEG 或 MIXED 文件格式,默认设置为 MIXED
      tile_format="PNG"
      #针对 JPEG 或 MIXED 压缩质量输入一个介于 1 和 100 之间的值,默认值为 75
      tile_compression_quality="75"
      #确定切片的存储格式,COMPACT&EXPLODED,默认存储格式为紧凑 (COMPACT)
      storage_format="COMPACT"
      
      print "Parameter Set Up OK,Executing，Please Waite For You........."
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


      scheme_endtime=datetime.datetime.now()
      print "GenerateTileCacheTilingScheme Python Tool Executed Time Cost is :",(scheme_endtime-scheme_starttime)

      for i in range(1,10,1):
            print ""
      


      cache_starttime=datetime.datetime.now()
      print "ManageTileCache Python Tool Start Executing,Start Time is:",cache_starttime
    
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
      scales="591657527.591555,295828763.795777,147914381.897889,73957190.948944,36978595.474472,18489297.737236,9244648.868618,4622324.434309,2311162.217155,1155581.108577,577790.554289,288895.277144,144447.638572,72223.819286,36111.909643,18055.954822,9027.977411,4513.988705,2256.994353,1128.497176"
      #定义感兴趣区以对将创建或删除的切片进行约束
      area_of_interest="#"
      max_cellsize = "#"
      #最小缓存比例将决定生成缓存时所使用的比例
      min_cachedscale = "4622324.434309"
      #最大缓存比例将决定生成缓存时所使用的比例
      max_cachedscale = "577790.554289"

      print "Parameter Set Up OK,Executing，Please Waite For You........."
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











