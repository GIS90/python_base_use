##- * - coding: utf-8 - * -

import arcpy


def importToSdeDB(inputSpace, sdeFile):
    print "ShpFiles Import To ", sdeFile
    arcpy.env.workspace = inputSpace
    num = 1
    for shp in arcpy.ListFiles("*.shp"):
        try:

            result = arcpy.FeatureClassToGeodatabase_conversion(shp, sdeFile)
            print "num=", num, "---------", shp, "finish"

            num = num + 1
            print result
        except Exception as e:
            print e.message

    print "All ShpFile DataImport To SQLServer Finish"


if __name__ == '__main__':
    inputSpace = r'E:\2015Project\长春项目\cc_BaseData(wgs84)'

    sdeFile = r'E:\connectToSDE\connectionToSDE.sde\sde.DBO.CC_BaseData'
    importToSdeDB(inputSpace, sdeFile)
