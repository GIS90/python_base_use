# - * - coding: utf-8 - * -




import datetime

import arcpy

# ��һ����Ϊ��ͼ��Ӱ����񻺴洴����Ƭ�����ͱ����ļ��У���Ҫ�õ�CreateMapServerCache_server����


cscs_starttime = datetime.datetime.now()
print "Create Server Cache Scheme Python Tool Executing Start,this time is:", cscs_starttime

workspace = r"D:\map_Services\WZ_Map"
arcpy.env.workspace = workspace

# ���ò����б�


# Ҫ���л���ĵ�ͼ��Ӱ�����
connectionFile = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog"
server = "arcgis on localhost_6080 (admin)"
serviceName = "Map_Server.MapServer"
inputService = connectionFile + "\\" + server + "\\" + serviceName
# ���ڻ���ĸ�Ŀ¼����Ŀ¼��������ע��� ArcGIS Server ����Ŀ¼
service_cache_directory = r"D:\arcgisserver\directories\arcgiscache"
# ѡ����� NEW ���� PREDEFINED ��Ƭ������NEW �½���Ƭ������PREDEFINED ��ָ��һ���������Ѵ��ڵ���Ƭ���� .xml �ļ�
tiling_scheme_type = "NEW"
# ָ����ζ�����Ƭ�ı�����CUSTOM ������������������κ����������STANDARD �����ݱ���������Python �е� num_of_scales�������ж���������Զ����ɱ���
scalesType = "CUSTOM"
# Ҫ�ڻ����д����ı�������
num_of_scales = "4"
# ����豸��ÿӢ�����
dots_per_inch = "96"
# ������Ƭ�Ŀ�Ⱥ͸߶�,������Ϊ��λ
tile_size = "256 x 256"
# Ԥ������Ƭ�����ļ���·����ͨ����Ϊ conf.xml����
predefined_tiling_scheme = ""
# ��Ƭ����ԭ��,���Ͻ�
tile_origin = ""
# ���ڻ���ı�������
scales = "577790.554289;1155581.108577;2311162.217155;4622324.434309"
# Ϊ�����е���Ƭѡ�� PNG��PNG8��PNG24��PNG32��JPEG �� MIXED �ļ���ʽ,PNG8 ΪĬ��ѡ��
cacheTileFormat = "PNG32"
# ��� JPEG ѹ����������һ������ 1 �� 100 ֮���ֵ
tile_compression_quality = "0"
# ȷ����Ƭ�Ĵ洢��ʽ
storage_format = "COMPACT"

print "------------------------------------------------------------------------------------------------"
print "Parameter Set Up OK,Scheme Information is:"
print "input_service is:", input_service
print "service_cache_directory is:", service_cache_directory
print "tiling_scheme_type is:", tiling_scheme_type
print "scalesType is:", scalesType
print "tile_size is:", tile_size
print "predefined_tiling_scheme is:", predefined_tiling_scheme
print "scales is:", scales
print "cacheTileFormat is:", cacheTileFormat
print "tile_compression_quality is:", tile_compression_quality
print "storage_format is:", storage_format
print "------------------------------------------------------------------------------------------------"

print "Executing Scheme,Please waite for me:................"
result = arcpy.CreateMapServerCache_server(input_service,
                                           service_cache_directory,
                                           tiling_scheme_type,
                                           scalesType,
                                           num_of_scales,
                                           dots_per_inch,

                                           tile_size,
                                           predefined_tiling_scheme,
                                           tile_origin,
                                           scales,
                                           cacheTileFormat,
                                           tile_compression_quality,
                                           storage_format)

cscs_endtime = datetime.datetime.now()
print "Scheme Generated,Total time is:", (cscs_endtime - cscs_starttime)
