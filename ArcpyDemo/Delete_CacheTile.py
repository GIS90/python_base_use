# - * - coding : utf-8 - * -

#Python Tool ɾ��������Ƭ


import sys
import arcpy
import datetime
import timer
import string
import traceback



starttime=datetime.datetime.now()
print "Delete Cache Tile Execute,Start Time is:",starttime


#inputService�����Ĺ̶�ֵ
connectionFile=r"C:\Users\Administrator\AppData\Roaming\ESRI\Desktop10.2\ArcCatalog"
#inputService�������˻�
server = "arcgis on localhost_6080 (admin)"
#inputService�����Ĳ�����������
serviceName = "WZ_Map_Server.MapServer"
#�����������ͷ�������Ϣ���ַ���
inputService = connectionFile + "\\" + server + "\\" + serviceName
#���湤�߷���ʵ��������
numOfCachingServiceInstances = 2


try:
      print "Delete Cache Tile Information is :"
      print "-------------------------------------------------------------------------------------"
      print "inputService is",inputService
      print "numOfCachingServiceInstances is",numOfCachingServiceInstances
      print "-------------------------------------------------------------------------------------"
      print "Tool Executing,Please Waite For ..................."
      arcpy.DeleteMapServerCache_server(inputService,numOfCachingServiceInstances)
      endtime=datetime.datetime.now()
      print "Executed,It Spends Time :",(endtime-starttime)
except Exception as e:
      print e.message



print "All Finish!!!"
