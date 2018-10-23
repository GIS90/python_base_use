# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0 Final
# Purpose: This script will iterate through each MXD in a folder and report the
#          name of each map document that contains broken data sources.  The
#          script is intended to run from a script tool that requires two input
#          parameters:
#               1) Browse to a folder that contains MXDs,
#               2) Browse to an specify an output text file ending in txt.
#          The resulting text file will automatically open.

import arcpy, datetime, os

try:
  
  #Read input parameters from GP dialog
  folderPath = arcpy.GetParameterAsText(0)
  output = arcpy.GetParameterAsText(1)

  #Create r/w output file
  outFile = open(output, "w")

  #Report header
  outFile.write("Data Source Report: \n")
  outFile.write(" \n")
  outFile.write("This report summarizes the names of the individual layers within a map document \n")
  outFile.write("that does not have a valid data source. \n")
  outFile.write(" \n")
  outFile.write("Folder location: " + folderPath + "\n")
  outFile.write("\n")
  outFile.write("Date: " + str(datetime.datetime.today().strftime("%B %d, %Y")) + "\n")

  #Loop through each MXD in the folder
  count = 0
  for filename in os.listdir(folderPath):
    fullpath = os.path.join(folderPath, filename)
    if os.path.isfile(fullpath):
      if filename.lower().endswith(".mxd"):
         
        #Reference MXD file
        mxd = arcpy.mapping.MapDocument(fullpath)
              
        #Report broken sources
        if len(arcpy.mapping.ListBrokenDataSources(mxd)) > 0:
          count = 1
          outFile.write("\n")
          outFile.write("\n")
          outFile.write("---------------------------------------------------------------------------------- \n")
          outFile.write(" MAPDOCUMENT: " + os.path.basename(mxd.filePath) + "\n")
          outFile.write("---------------------------------------------------------------------------------- \n")
          outFile.write(" \n")
                  
          for brkLyr in arcpy.mapping.ListBrokenDataSources(mxd):      
            if brkLyr.supports("dataSource"):
              outFile.write("\t Layer name:      " + brkLyr.name + "\n")
              outFile.write("\t Original source: " + brkLyr.dataSource + "\n")

          del mxd

  #Report if no broken sources are found                    
  if count == 0:
    outFile.write("\n")
    outFile.write("\n")
    outFile.write("---------------------------------------------------------------------------------- \n")
    outFile.write("              NO DATA SOURCES FOUND \n")
    outFile.write("---------------------------------------------------------------------------------- \n")

  #Close the file
  outFile.close()

  #Open the resulting output file
  os.startfile(output)

  #Delete all variables that reference data on disk
  del folderPath, output, outFile, fullpath

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
