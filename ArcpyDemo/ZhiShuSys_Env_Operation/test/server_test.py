# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

from ArcpyDemo.ZhiShuSys_Env_Operation.core.server import *

connect_type = GIS_SERVICES_TYPE.administrator
server_url = "http://192.168.2.163:6080/arcgis/admin"
server_type = SERVER_TYPR.arcgis
isuse_stage_folder = True
user = "siteadmin"
pwd = "123456"
issave_user_pwd = True
mapserver = MapServer(connect_type,
                      server_url,
                      server_type,
                      isuse_stage_folder,
                      user,
                      pwd,
                      issave_user_pwd)

service_mxd = r"E:\data\ty\Map2013City_clip_sour\ty_region.mxd"
mxd_path = os.path.dirname(service_mxd)
mxd_name = os.path.basename(service_mxd)
service_name = "ty_region"
service_type = SERVER_TYPR.arcgis
service_folder = "taiyuan"
iscopy_data_to_server = False
summary = "tai yuan server test"
tags = "tai yuan server test"
service_rlt = mapserver.publish_server(service_name,
                                       service_mxd,
                                       server_type,
                                       iscopy_data_to_server,
                                       service_folder,
                                       summary,
                                       tags)
print service_rlt
