# -*-coding:utf-8-*-


import os
try:
    import arcpy
except ImportError as e:
    msg = "arcpy module import error: %s" % e.message
    raise Exception(msg)


def connSdeDB(connSdePath, connSdeName, database_platform, instance, authentication, accountName, accountPw, save_user_pass, database, schema, version_type, version, date, sdeFile):
    print "Is Checking SdeFile The Existence Of The File"

    if not os.path.exists(sdeFile):
        print "SdeFile Is Not Exist,Creating..........."
        # arcpy.CreateArcSDEConnectionFile_management
        arcpy.CreateDatabaseConnection_management(connSdePath,
                                                  connSdeName,
                                                  database_platform,
                                                  instance,
                                                  authentication,
                                                  accountName,
                                                  accountPw,
                                                  save_user_pass,
                                                  database,
                                                  schema,
                                                  version_type,
                                                  version,
                                                  date)
        print "Create Connection....................Success"
    else:
        print "SdeFile Is Existing..........."

    print "Test ConnectionDateBase................SQL Server"
    print "ConnectionDateBase Success"


if __name__ == "__main__":

    print "Python Tool ShpFiles Operator SDE DataBase FeatureClass!"

    # shpfile file path
    inputSacpe = r'E:\connectToSDE'
    # conn to db paras
    connSdePath = r'E:\connectToSDE'
    connSdeName = "sqlserver_localhost_sde.sde"
    # SQL_SERVER    ORACLE    DB2     POSTGRESQL
    database_platform = 'SQL_SERVER'
    instance = 'localhost'
    # DATABASE_AUTH     OPERATING_SYSTEM_AUTH
    authentication = 'DATABASE_AUTH'
    accountName = 'sa'
    accountPw = '123456'
    # SAVE_USERNAME    DO_NOT_SAVE_USERNAME
    save_user_pass = 'SAVE_USERNAME'
    database = 'sde'
    schema = ''
    # TRANSACTIONAL   HISTORICAL     POINT_IN_TIME
    version_type = 'TRANSACTIONAL'
    version = ''
    date = ''

    sdeFile = os.path.join(connSdePath, connSdeName)

    try:
        print "Connection SDE DataBase ing..........."
        connSdeDB(connSdePath,
                  connSdeName,
                  database_platform,
                  instance,
                  authentication,
                  accountName,
                  accountPw,
                  save_user_pass,
                  database,
                  schema,
                  version_type,
                  version,
                  date,
                  sdeFile)
    except Exception as e:
        print e.message




        # fsName= createFeatureSet.createFS(sdeFile)
        # print fsName

        # ImportToSdeDB.importToSdeDB(inputSacpe,sdeFile)

        # IteratorSdeFeatyreClass.iteratorFeatureClass(sdeFile)
