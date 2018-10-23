# - * - coding : utf-8 - * -



import sys
import arcpy
import datetime
import timer
import string
import traceback

#�ڶ�����Ϊ��ͼ��Ӱ����񴴽�������Ƭ����Ҫ�õ�ManageMapServerCacheTiles_server����



mmsct_starttime=datetime.datetime.now()
print "ManageMapServerCacheTiles_server Python Tool Executing Start,this time is:",mmsct_starttime


workspace=r"D:\map_Services\WZ_Map"
arcpy.env.workspace=workspace


#���ò����б�



#�����»�����Ƭ�����ĵ�ͼ��Ӱ�����
connectionFile = "C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog"
server = "arcgis on localhost_6080 (admin)"
serviceName = "Map_Server.MapServer"
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




                                                
                                               

