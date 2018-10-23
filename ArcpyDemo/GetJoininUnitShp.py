# coding:utf-8


import datetime
import os

import arcpy


def JoinInUnitToShp(FilePath, TargetFeature, JoinFeature):
    try:
        arcpy.env.workspace = FilePath
        DestFeature = os.path.join(FilePath, os.path.splitext(TargetFeature)[0] + '_join.shp')
        JoinOperation = 'JOIN_ONE_TO_ONE'
        Jointype = 'KEEP_ALL'
        arcpy.SpatialJoin_analysis(TargetFeature,
                                   JoinFeature,
                                   DestFeature,
                                   JoinOperation,
                                   Jointype)

        return DelShpNoAvailFields(DestFeature)
    except Exception as e:
        print e.message


def DelShpNoAvailFields(DestFeature):
    arcpy.env.workspace = os.path.split(DestFeature)[0]
    fields = 'Join_Count;TARGET_FID'
    try:
        arcpy.DeleteField_management(DestFeature, fields)
        return 1
    except Exception as e:
        print e.message
        return -1


if __name__ == '__main__':
    print '*************************************************'
    print 'Ihe Python Tool Start Working !'
    startTime = datetime.datetime.now()
    print '*****Start Time : %s*****' % startTime
    FilePath = r'E:\region'
    TargetFeature = r'E:\region\QD.shp'
    JoinFeature = r'E:\region\QD_JTXQ.shp'
    if JoinInUnitToShp(FilePath, TargetFeature, JoinFeature):
        print 'Program Is Execute Success !'
    else:
        print 'Program Is End , Occur Error !'
    endTime = datetime.datetime.now()
    costTime = (endTime - startTime).seconds
    print '*****Cost Time : %s s.*****' % costTime
    print '*************************************************'
