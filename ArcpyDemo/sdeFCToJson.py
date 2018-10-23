


import os
import arcpy



def toJson(filePath,sdeFile):

    arcpy.env.workspace=sdeFile
    for i in arcpy.ListDatasets():
        try:
            in_Feature=i
            out_FeatureName=i.split('.')[0]+'.json'
            out_Feature=os.path.join(filePath,out_FeatureName)
            if os.path.exists(out_Feature):
                del out_Feature
                print out_Feature
            result=arcpy.FeaturesToJSON_conversion(in_Feature,
                                                out_Feature)

            print '%s Info : %s'%(out_FeatureName,result)
        except Exception as e:
            print e.message



if __name__=='__main__':
    filePath=r'F:\Project'
    sdeFile=r'F:\ConnectionToSQL.sde'
    toJson(filePath,sdeFile)