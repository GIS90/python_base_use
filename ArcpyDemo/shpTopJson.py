#coding:utf-8


import arcpy
import datetime
import os


def toJson(filePath_Sour,filePath_Dest):
    arcpy.env.workspace=filePath_Sour
    for shp in arcpy.ListFiles('*.shp'):
        name=os.path.splitext(shp)[0]+'.json'
        JsonDest=os.path.join(filePath_Dest,name)
        if os.path.exists(JsonDest):
            os.remove(JsonDest)
            print '%s Is Exist , Delete !'%JsonDest
        format_json='NOT_FORMATTED'
        include_z_values=''
        include_m_values=''
        result=arcpy.FeaturesToJSON_conversion(shp,
                                               JsonDest,
                                               format_json,
                                               include_z_values,
                                               include_m_values)
        print result




if __name__=='__main__':

    print '***************************************'
    print 'Ihe Python Tool Start Working !'
    startTime=datetime.datetime.now()
    print '*****Start Time : %s'%startTime

    filePath_Sour=r'E:\2015Project\test'
    filePath_Dest=r'E:\2015Project\Json'
    toJson(filePath_Sour,filePath_Dest)


    print 'Ihe Python Tool Worked OK !'
    endTime=datetime.datetime.now()
    costTime=(endTime-startTime).seconds
    print '*****Cost Time : %s'%costTime
    print '***************************************'



















