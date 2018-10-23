# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from ArcpyDemo.ZhiShuSys_Env_Operation.core.sde import *

sde = SDEOpr()
target_sdename = "target"
target_db_type = DBType.SQL_SERVER
target_server = "localhost"
target_db_name = "ccsde"
target_db_user = "sa"
target_db_pwd = "123456"

source_sdename = "source"
source_db_type = DBType.SQL_SERVER
source_server = "localhost"
source_db_name = "sde"
source_db_user = "sa"
source_db_pwd = "123456"

try:
    source_sde = sde.create_sde_conndb(source_sdename, source_db_type, source_server, source_db_user, source_db_pwd, source_db_name)
    target_sde = sde.create_sde_conndb(target_sdename, target_db_type, target_server, target_db_user, target_db_pwd, target_db_name)
except Exception as e:
    print e.message

# # test sdefeature_copy_sdefeature
# suclist, failist = sde.sdefeature_copy_sdefeature(source_sde, target_sde)
# print suclist
# print failist

# # test create_dataset
# ds_name = "test"
# ds_sde = target_sde
# ds_sf = ""
# print sde.create_dataset(ds_name, ds_sde, ds_sf)

# test ftdataset_copy_ftdataset
# try:
#     print sde.ftdataset_copy_ftdataset(source_sde, "sde.DBO.basicdata", target_sde, "ccsde.DBO.ds")
# except Exception as e:
#     print e.message

# # test del_element
# import arcpy
# arcpy.env.workspace = target_sde
# for fc in arcpy.ListFeatureClasses():
#     del_fc = target_sde + "\\" + fc
#     sde.del_element(del_fc)
#     print del_fc

# test feature_copy_dataset
# src_fc = "sde.DBO.detail"
# tar_ds = "testds1"
# try:
#     print sde.feature_copy_dataset(source_sde, src_fc, target_sde, tar_ds)
# except Exception as e:
#     print e.message

# test copy_sde_table
# print sde.copy_sde_table(source_sde, target_sde, True)

# test copy_table_one
# src_table = "sde.DBO.test"
# tar_table = "ccsde.DBO.test111"
# print sde.copy_table_one(src_table, source_sde, tar_table, target_sde, True)


