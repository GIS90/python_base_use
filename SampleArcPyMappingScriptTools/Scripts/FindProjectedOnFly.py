# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will iterate through each MXD in a folder and report the
#          name of each map document and data frame that has layers that are.
#          being projected on the fly.  The script is intended to run from a
#          script tool that requires two input parameters:
#               1) Folder containing MXDs,
#               2) An output text file.
#
#          The resulting text file will automatically open.
#
# Note: This script is simply comparing the data frame's spatial reference name
#       against the individual layer's spatial reference name.  For a more
#       accurate result you may want to include more parameters (e.g., Central
#       Meridian).

import arcpy, datetime, os

try:

  #Read input parameters from GP dialog
  folderPath = arcpy.GetParameterAsText(0)
  output = arcpy.GetParameterAsText(1)

  #Create an output file
  outFile = open(output, "w")

  #Report header
  outFile.write("Data Source Report: \n")
  outFile.write("\n")
  outFile.write("This report summarizes the names of all map documents and data frames within \n")
  outFile.write("a folder that contain layers being projected on the fly. \n")
  outFile.write("\n")
  outFile.write("Folder location: " + folderPath + "\n")
  outFile.write("\n")
  outFile.write("Date: " + str(datetime.datetime.today().strftime("%B %d, %Y")) + "\n")

  #Loop through each MXD file
  mCnt = 0
  for filename in os.listdir(folderPath):
    fullpath = os.path.join(folderPath, filename)
    if os.path.isfile(fullpath):
      if filename.lower().endswith(".mxd"):
      
        #Reference MXD
        mxd = arcpy.mapping.MapDocument(fullpath)
   
        #Determine if the data source exists within the data frames/map document 
        sCnt = 0
        for df in arcpy.mapping.ListDataFrames(mxd):
          layerList = []
          for lyr in arcpy.mapping.ListLayers(mxd, "", df):
            if not lyr.isGroupLayer:
              try:
                desc = arcpy.Describe(lyr.dataSource) #fails with layers with broken data sources
              except:
                desc = None
              if desc and df.spatialReference.name != desc.spatialReference.name:
                mCnt = 1
                sCnt = sCnt + 1
                layerList.append(lyr.name)
                if sCnt == 1:  #Write the MXD header once
                  outFile.write("\n")
                  outFile.write("\n")
                  outFile.write("----------------------------------------------------------------------------- \n")
                  outFile.write(" MAPDOCUMENT: " + os.path.basename(mxd.filePath) + "\n")
                  outFile.write("----------------------------------------------------------------------------- \n")
                  sCnt = sCnt + 1 
          if len(layerList) > 0: #Write the data frame name once
            outFile.write("\n")
            outFile.write("\t Data Frame: " + df.name + "\n")
            for lyr in layerList: #Write each layer name
              outFile.write("\n")
              outFile.write("\t\t Layer: " + lyr + "\n")

        del mxd
        
  if mCnt == 0:
    outFile.write("\n")
    outFile.write("\n")
    outFile.write("--------------------------------------------------------------------------- \n")
    outFile.write("              NO PROJECTED ON THE FLY LAYERS FOUND \n")
    outFile.write("--------------------------------------------------------------------------- \n")
  outFile.close()

  #Open the resulting text file
  os.startfile(output)

  #Delete variable references
  del folderPath, output, outFile, fullpath

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
