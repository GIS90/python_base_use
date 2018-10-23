#- * - coding : utf-8 - * -


__author__ = 'Administrator'



import os
import arcpy
import datetime

starttime=datetime.datetime.now()
print "Create TPK Package is Executing,this time is:",starttime


workspace=r"D:\map_Services\WZ_Map"

arcpy.env.workspace=workspace

for mxd in arcpy.ListFiles("*.mxd"):
    print "Current mxd is:",mxd
    print "TPK Package Start:.............."
    in_map=mxd
    service_type="EXISTING"
    ifile=r"D:\map_Services\Tilingscheme.xml"
    output_file=os.path.join(workspace,os.path.splitext(mxd)[0])
    format_type="PNG32"
    level_of_detail=""
    summary="Map TPK Package"
    tags="Map,TPK,Package"
    arcpy.CreateMapTilePackage_management(in_map,
                                          service_type,
                                          
                                          output_file+".tpk",
                                          format_type,
                                          level_of_detail)                                         
    print "TPK Package End:.............."


endtime=datetime.datetime.now()
print "Executing Success,this time is:",endtime



print "Total program execution time is:",(endtime-starttime)







