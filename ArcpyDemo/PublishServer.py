# - * - coding : utf-8 - * -
# -*- coding: UTF-8 -*-



import datetime
import os
import os.path

import arcpy
import arcpy.mapping

starttime = datetime.datetime.now()

print "ArcGIS Publish Server Python Start Execute，Now Time is：", starttime

# 设置发布服务文件的mxd路径
workspace = r"D:\map_Services\Wu_Map"

# PublishServer为Python脚本功能函数，创建Server共分为5步




# 第一步，先得到站点连接文件，主要用到CreateGISServerConnectionFile (arcpy.mapping)函数

print "Creating .ags File，Please waite for 'it':........."

connection_type = "ADMINISTER_GIS_SERVICES"
out_folder_path = r"E:\connectToSDE"
con_filename = "conFile.ags"
server_url = r"http://192.168.2.108:6080/arcgis/admin"
server_type = "ARCGIS_SERVER"
use_arcgis_desktop_staging_folder = False
staging_folder_path = r"E:\connectToSDE"
username = "siteadmin"
password = "123456"
save_username_password = "SAVE_USERNAME"
arcpy.mapping.CreateGISServerConnectionFile(connection_type,
                                            out_folder_path,
                                            con_filename,
                                            server_url,
                                            server_type,
                                            use_arcgis_desktop_staging_folder,
                                            staging_folder_path,
                                            username,
                                            password,
                                            save_username_password
                                            )
print con_filename, " File Created Success!!!"

# 第二步，打开指定workspace下的mxd文件,并创建的输出是服务定义草稿 (.sddraft) 文件
# 主要用到arcpy.mapping.MapDocument打开mxd，CreateMapSDDraft创建地图草稿
arcpy.env.workspace = workspace
filepath = r"D:\map_Services"
for mxd in arcpy.ListFiles("*.mxd"):
    print "Current mxd name is:", mxd
    mappath = os.path.join(workspace, mxd)
    mapdoc = arcpy.mapping.MapDocument(mappath)
    print mxd, "Contains Layers:"
    for ly in arcpy.mapping.ListLayers(mapdoc):
        print ly.name
    out_sddraft = os.path.join(filepath, "mapFile.sddraft")
    sd = os.path.join(filepath, "mapFile.sd")
    # 在此修改服务名称
    service_name = "Wu_Map"
    server_type = "ARCGIS_SERVER"
    connection_file_path = os.path.join(out_folder_path, con_filename)
    copy_data_to_server = False
    # 服务文件夹
    # folder_name="None"
    summary = "Map Server"
    tags = "Map,Server"
    print "Creating Map SDDraft File:..............."
    analyse = arcpy.mapping.CreateMapSDDraft(mapdoc,
                                             out_sddraft,
                                             service_name,
                                             server_type,
                                             connection_file_path,
                                             copy_data_to_server,
                                             None,
                                             summary,
                                             tags
                                             )
    print "SDDraft File Created Success!!!"

    # 第三步，分析文档错误，警告，信息，
    for key in ('messages', 'warnings', 'errors'):
        print "----" + key.upper() + "---"
        vars = analyse[key]
        for ((message, code), layerlist) in vars.iteritems():
            print "    ", message, " (CODE %i)" % code
            print "       applies to:",
            for layer in layerlist:
                print layer.name,
            print


            # 第四步，使用过渡服务工具将服务定义草稿转换为完全合并的服务定义 (.sd) 文件
    print "out_sddraft File Transferring sd File:............"
    if analyse['errors'] == {}:
        arcpy.StageService_server(out_sddraft, sd)
        print "sd File Transferring Success!!！"

        # 第五步，发布服务，主要用到UploadServiceDefinition_server函数
        print "Map is Publishing:..........."
        arcpy.UploadServiceDefinition_server(sd, connection_file_path)
        endtime = datetime.datetime.now()
        print "Map Publishing Success,Now Time is:", endtime

print "Python Execute Success,Total spending time:", (endtime - starttime).seconds
print "w    o    z    h    e    n    s    h   u   a   i"
