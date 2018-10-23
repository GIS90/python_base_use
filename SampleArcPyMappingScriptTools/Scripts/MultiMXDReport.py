# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will iterate through each MXD in a folder and report information about each
#          map document, it's data frames and layers.  The script is intended to run from a script
#          tool that requires two input parameters:
#               1) folder containing MXDs,
#               2) an output text file.
#
#          The resulting text file will automatically open.

import arcpy, datetime, os

try:

    arcpy.gp.overwriteOutput = True

    #Read input parameters from GP dialog
    folderPath = arcpy.GetParameterAsText(0)
    output = arcpy.GetParameterAsText(1)

    #Create an output file
    outFile = open(output, "w")

    #Report header
    outFile.write("MXD REPORT: \n")
    outFile.write("\n")
    outFile.write("This report is for all MXDs in a folder.  It lists relevant information about\n")
    outFile.write("map document properties, data frame, layer, and table information for each MXD\n")
    outFile.write("in a system folder\n")
    outFile.write("\n")
    outFile.write("Date: " + str(datetime.datetime.today().strftime("%B %d, %Y")) + "\n")

    #Loop through each MXD file
    count = 0
    for filename in os.listdir(folderPath):
        fullpath = os.path.join(folderPath, filename)
        if os.path.isfile(fullpath):
            if filename.lower().endswith(".mxd"):

                #Reference MXD
                mxd = arcpy.mapping.MapDocument(fullpath)
                count = 1

                #Format output value
                if mxd.author =="": authorValue = "None"
                else: authorValue = mxd.author
                if mxd.summary =="": summaryValue = "None"
                else: summaryValue = mxd.summary
                BDS = arcpy.mapping.ListBrokenDataSources(mxd)
                if len(BDS) == 0: BDSValue = "None"
                else: BDSValue = "A total of " + str(len(BDS)) + " broken data source(s)."
                
                #Write MXD data to file
                outFile.write("\n")
                outFile.write("\n")
                outFile.write("------------------------------------------------------------------- \n")
                outFile.write("MAPDOCUMENT: " + os.path.basename(mxd.filePath) + "\n")
                outFile.write("------------------------------------------------------------------- \n")
                outFile.write("\n")
                outFile.write("\t Path:                 " + mxd.filePath + "\n")
                outFile.write("\t Last Saved:           " + str(mxd.dateSaved) + "\n")
                outFile.write("\t Author:               " + authorValue + "\n")
                outFile.write("\t Summary:              " + summaryValue + "\n")
                outFile.write("\t Relative Paths:       " + str(mxd.relativePaths) + "\n")
                outFile.write("\t Broken Data Sources:  " + BDSValue + "\n")

                #Reference each data frame and report data
                DFList = arcpy.mapping.ListDataFrames(mxd)
                for df in DFList:
                    #Format output values
                    if df.description == "": descValue = "None"
                    else: descValue = df.description

                    #Write data frame data to file
                    outFile.write("\n")
                    outFile.write("\n")
                    outFile.write("\t DATA FRAME: " + df.name + "\n")
                    outFile.write("\n")
                    outFile.write("\t\t Description:        " + descValue + "\n")
                    outFile.write("\t\t Spatial Reference:  " + df.spatialReference.name + "\n")
                    outFile.write("\t\t Transformation(s):  " + str(df.geographicTransformations) + "\n")
                    outFile.write("\t\t Map Units:          " + df.mapUnits + "\n")
                    try:
                        outFile.write("\t\t Scale:              " + str(df.scale) + "\n")
                    except:
                        outFile.write("\t\t Scale:              Unknown \n")
                    outFile.write("\t\t Rotation:           " + str(df.rotation) + "\n")
                  
                    #Reference each layer in a data frame
                    lyrList = arcpy.mapping.ListLayers(mxd, "", df)
                    for lyr in lyrList:
                        outFile.write("\n")
                        outFile.write("\t\t LAYER: " + lyr.name + "\n")
                        outFile.write("\t\t\t Group Layer Path:  " + lyr.longName + "\n")
                        if lyr.supports("dataSource"):
                            outFile.write("\t\t\t Data Source:       " + lyr.dataSource + "\n")
                            try:
                                outFile.write("\t\t\t Dataset type:      " + arcpy.Describe(lyr.dataSource).datasettype + "\n")
                            except:
                                outFile.write("\t\t\t Dataset type:     Unknown (could be a broken data source) \n")
                        else: outFile.write("\t\t\t Data Source:       N/A \n")
                        if lyr.supports("definitionQuery"):
                            if lyr.definitionQuery == "":
                                outFile.write("\t\t\t Query Definition:  None \n" )
                            else: outFile.write("\t\t\t Query Definition:  " + lyr.definitionQuery + "\n")
                        else: outFile.write("\t\t\t Query Definition:  N/A \n")
                        
                    #Reference each table in a data frame 
                    tableList = arcpy.mapping.ListTableViews(mxd, df, "")
                    for table in tableList:
                        outFile.write("\n")
                        outFile.write("\n")
                        outFile.write("\t\t TABLEVIEW: " + table.name + "\n")
                        outFile.write("\n")
                        outFile.write("\t\t\t Data Source:           " + table.dataSource + "\n")
                        if table.definitionQuery == "":
                            outFile.write("\t\t\t Query Definition:      None \n")
                        else: outFile.write("\t\t\t Query Definition:      " + table.definitionQuery + "\n")

                del mxd
            
    if count ==0:
        outFile.write("\n")
        outFile.write("\n")
        outFile.write("---------------------------------------------------------------------------------- \n")
        outFile.write("                            NO MXD FILES FOUND \n")
        outFile.write("---------------------------------------------------------------------------------- \n")                          

    outFile.close()

    #Open resulting text file
    os.startfile(output)

    #Delete variables that reference data on disk
    del folderPath, output, outFile, fullpath

except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))
