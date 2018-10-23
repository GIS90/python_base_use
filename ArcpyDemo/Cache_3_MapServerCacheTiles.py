# - * - coding : utf-8 - * -




import sys
import arcpy
import datetime
import timer
import string
import traceback


#��һ����Ϊ��ͼ��Ӱ����񻺴洴����Ƭ�����ͱ����ļ��У���Ҫ�õ�CreateMapServerCache_server����


cscs_starttime=datetime.datetime.now()
print "Create Server Cache Scheme Python Tool Executing Start,this time is:",cscs_starttime


workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace



#���ò����б�


#Ҫ���л���ĵ�ͼ��Ӱ�����
input_service="GIS ������/arcgis on localhost_6080 (admin)/WZ_Map_Server.MapServer"
#���ڻ���ĸ�Ŀ¼����Ŀ¼��������ע��� ArcGIS Server ����Ŀ¼
service_cache_directory=r"D:\arcgisserver\directories\arcgiscache"
#ѡ����� NEW ���� PREDEFINED ��Ƭ������NEW �½���Ƭ������PREDEFINED ��ָ��һ���������Ѵ��ڵ���Ƭ���� .xml �ļ�
tiling_scheme_type="NEW"
#ָ����ζ�����Ƭ�ı�����CUSTOM ������������������κ����������STANDARD �����ݱ���������Python �е� num_of_scales�������ж���������Զ����ɱ���
scalesType="CUSTOM"
#Ҫ�ڻ����д����ı�������
num_of_scales="4"
#����豸��ÿӢ�����
dots_per_inch="96"
#������Ƭ�Ŀ�Ⱥ͸߶�,������Ϊ��λ
tile_size="256 x 256"
#Ԥ������Ƭ�����ļ���·����ͨ����Ϊ conf.xml����
predefined_tiling_scheme=""
#��Ƭ����ԭ��,���Ͻ�
tile_origin=""
#���ڻ���ı�������
scales="577790.554289;1155581.108577;2311162.217155;4622324.434309"
#Ϊ�����е���Ƭѡ�� PNG��PNG8��PNG24��PNG32��JPEG �� MIXED �ļ���ʽ,PNG8 ΪĬ��ѡ��
cacheTileFormat = "PNG32"
#��� JPEG ѹ����������һ������ 1 �� 100 ֮���ֵ
tile_compression_quality = "0"
#ȷ����Ƭ�Ĵ洢��ʽ
storage_format = "COMPACT"


print "------------------------------------------------------------------------------------------------"
print "Parameter Set Up OK,Scheme Information is:"
print "input_service is:",input_service
print "service_cache_directory is:",service_cache_directory
print "tiling_scheme_type is:",tiling_scheme_type
print "scalesType is:",scalesType
print "tile_size is:",tile_size
print "predefined_tiling_scheme is:",predefined_tiling_scheme
print "scales is:",scales
print "cacheTileFormat is:",cacheTileFormat
print "tile_compression_quality is:",tile_compression_quality
print "storage_format is:",storage_format
print "------------------------------------------------------------------------------------------------"

print "Executing Scheme,Please waite for me:................"
arcpy.CreateMapServerCache_server(input_service,
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



cscs_endtime=datetime.datetime.now()
print "Scheme Generated,Total time is:",(cscs_endtime-cscs_starttime)





#�ڶ�����Ϊ��ͼ��Ӱ����񴴽�������Ƭ����Ҫ�õ�ManageMapServerCacheTiles_server����



mmsct_starttime=datetime.datetime.now()
print "ManageMapServerCacheTiles_server Python Tool Executing Start,this time is:",mmsct_starttime


workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace


#���ò����б�



#input_server�����»�����Ƭ�����ĵ�ͼ��Ӱ�����
#inputService�����Ĺ̶�ֵ
connectionFile=r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog"
#inputService�������˻�
server = "arcgis on localhost_6080 (admin)"
#inputService�����Ĳ�����������
serviceName = "WZ_Map_Server.MapServer"
inputService = connectionFile + "\\" + server + "\\" + serviceName
#��������
scales = "4622324.434309;2311162.217155;1155581.108577;577790.554289"
#����ĸ���ģʽ
update_mode="RECREATE_ALL_TILES"
#���иù��ߵ�ϵͳ/���湤�߷���ʵ��������
num_of_caching_service_instances=3
#������ɾ����Ƭʱ�����յľ��η�Χ
update_extent=""
#�������Ȥ���ԶԽ�������ɾ������Ƭ����Լ��
area_of_interest=""
#����ͨ���ò����鿴�ڷ����������еĻ�����ҵ�Ľ��ȣ�WAIT&DO_NOT_WAIT
wait_for_job_completion="WAIT"


print "------------------------------------------------------------------------------------------------"
print "Parameter Set Up OK,CacheTile Information is:"
print "input_service is:",input_service
print "scales is:",scales
print "update_mode is:",update_mode
print "num_of_caching_service_instances is:",num_of_caching_service_instances
print "tile_sizeupdate_extentis:",update_extent
print "area_of_interest is:",area_of_interest
print "wait_for_job_completion is:",wait_for_job_completion
print "------------------------------------------------------------------------------------------------"



print "Executing Cache,Please waite for me:................"
arcpy.ManageMapServerCacheTiles_server(input_service,
                                       scales,
                                       update_mode,
                                       num_of_caching_service_instances,
                                       update_extent,
                                       area_of_interest,
                                       wait_for_job_completion)
                                              
                                              
                                          

mmsct_endtime=datetime.datetime.now()
print "MapTileCache Generated,Total time is:",(mmsct_endtime-mmsct_starttime)




                                                
                                               


print "All Success,Total Time is :",(cache_endtime-scheme_starttime)
print "             g o n g x i , h a h a              "


















