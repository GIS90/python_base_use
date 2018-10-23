# - * - coding : utf-8 - * -



import os

import arcpy


def iteratorFeatureClass(sdeFile):
    print "Iterator ShpFiles To ", sdeFile
    arcpy.env.workspace = sdeFile
    fcnum2 = fcnum1 = fsnum = 1

    for fc in arcpy.ListFeatureClasses():
        print 'SDE DataBase FeatureClass : '
        print fc
        fcnum1 = fcnum1 + 1
    for fs in arcpy.ListDatasets():
        arcpy.env.workspace = fs
        fsnum = fsnum + 1
        for fc in arcpy.ListFeatureClasses():
            print 'SDE DataBase %s FeatureClass : ' % fc
            fcnum2 = fcnum2 + 1
            print os.path.join(sdeFile, fc)

    print "FeatureSet SUM Is ", fsnum
    print "FeatureClass SUM Is ", (fcnum1 + fcnum2)


if __name__ == '__main__':
    filePath = r'F:'
    fileName = r'ConnectionToSQL.sde'
    sdeFile = os.path.join(filePath, fileName)
    iteratorFeatureClass(sdeFile)
