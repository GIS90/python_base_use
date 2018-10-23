# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will take all layers in a map documentpointing to a single personal
#          GDB and update them to point to a file GDB.  The script also has an option
#          to update SQL Expressions for all definition queries.  The script is intended
#          to run from a script tool that requires five input parameters:
#               1) Browse to an input personal GDB
#               2) Browse to an output file GDB
#               3) Browse to an existing MXD (that has layers pointing the the personal GDB)
#               4) Specifiy the path/name of a new MXD
#               5) Option to fix SQL expressions on definition queries
#
#          The resulting map document will automatically be opened.

import arcpy, os

try:

    #Read parameters from dialog
    inputGDB = arcpy.GetParameterAsText(0)
    outputGDB = arcpy.GetParameterAsText(1)
    inputMXD = arcpy.GetParameterAsText(2)
    outputMXD = arcpy.GetParameterAsText(3)
    updateSQL = arcpy.GetParameter(4)

    #Update pGDB TO fGDB
    mxd = arcpy.mapping.MapDocument(inputMXD)
    mxd.replaceWorkspaces(inputGDB, "ACCESS_WORKSPACE", outputGDB, "FILEGDB_WORKSPACE")

    #Update query definitions
    if updateSQL:
        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.supports("definitionQuery"):
                lyr.definitionQuery = lyr.definitionQuery.replace("[","\"")
                lyr.definitionQuery = lyr.definitionQuery.replace("]","\"")
            if lyr.supports("labelClasses"):
                for lblClass in lyr.labelClasses:
                    lblClass.SQLQuery = lblClass.SQLQuery.replace("[", "\"")
                    lblClass.SQLQuery = lblClass.SQLQuery.replace("]", "\"")

    #Save and open resulting MXD
    mxd.saveACopy(outputMXD)
    os.startfile(outputMXD)

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
