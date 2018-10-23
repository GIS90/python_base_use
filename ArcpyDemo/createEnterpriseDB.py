# -*- coding: utf-8 -*-



import datetime
import sys

import arcpy

reload(sys)
sys.setdefaultencoding("utf-8")


def createEnGeodb():
    # Oralce,PostgreSQL,SQL_Server
    db_platform = u"SQL_Server"
    # IP
    instance_name = u"localhost"
    # 新建的数据库名称
    db_name = u"QD_Project"
    # OPERATING_SYSTEM_AUTH或者DATABASE_AUTH
    account_auth = u"DATABASE_AUTH"
    db_admin = u"sa"
    db_admin_pw = u"123456"
    # SDE_SCHEMA —地理数据库资料档案库存储在名为 sde 的用户方案中并归该用户所有。这是默认设置
    # DBO_SCHEMA —地理数据库资料档案库存储在数据库的 dbo 方案中
    sde_schema = u"SDE_SCHEMA"
    # 使用的是 SQL Server 并指定了一个 sde 方案地理数据库，则该值必须为 sde。
    # 此工具将创建 sde 登录、数据库用户和方案，并授予其创建地理数据库以及删除与 SQL Server 实例之间连接所需的权限。
    # 如果指定了 dbo 方案，则不要为该参数提供值
    gdb_admin_name = u"sde"
    # 为地理数据库管理员用户提供密码
    gdb_admin_password = u"sde"
    # 该参数只对 Oracle 和 PostgreSQL DBMS 类型有效
    tablespace_name = u""
    # 提供授权企业级 ArcGIS for Server 时创建的密钥代码文件的路径和文件名
    authorization_file = r"E:\SoftWare_Package\ArcGIS10.2SDE\arcgisproduct.ecp"
    # authorization_file=r"E:\gml_File\Software_package\ArcGIS10.2\arcgisproduct.ecp"
    print "Connect To SQLServer Info:"
    print "                     db_platform:", db_platform
    print "                     instance_name:", instance_name
    print "                     db_name:", db_name
    print "                     account_auth:", account_auth
    print "                     db_admin:", db_admin
    print "                     db_admin_pw:", db_admin_pw
    print "                     sde_schema:", sde_schema
    print "                     gdb_admin_name:", gdb_admin_name
    print "                     gdb_admin_password:", gdb_admin_password
    print "                     tablespace_name:", tablespace_name
    print "                     authorization_file:", authorization_file
    print "Working...................................................."
    try:
        arcpy.CreateEnterpriseGeodatabase_management(db_platform,
                                                     instance_name,
                                                     db_name,
                                                     account_auth,
                                                     db_admin,
                                                     db_admin_pw,
                                                     sde_schema,
                                                     gdb_admin_name,
                                                     gdb_admin_password,
                                                     tablespace_name,
                                                     authorization_file)
        endTime = datetime.datetime.now()
        Time = (endTime - startTime).seconds
        print db_name + "DataBase Create Success.......Cost Time Is:", Time
    except Exception as e:
        print "Occur Exception:", e.message


if __name__ == "__main__":
    startTime = datetime.datetime.now()
    print "Python Connect To SQLServer:"
    createEnGeodb()
