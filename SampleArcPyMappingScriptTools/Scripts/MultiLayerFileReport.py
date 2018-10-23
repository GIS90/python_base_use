# Author:  ESRI
# Date:    July 5, 2010
# Version: ArcGIS 10.0
# Purpose: This script will iterate through each layer file in a folder and report information
#          about the layer or layers it contains.  The script will report information based on
#          the type of layer it is.  For example, if the layer is an SDE service, it will report
#          the connection information.  The script is intended to run from a script
#          tool that requires two input parameters:
#               1) folder containing layer files,
#               2) an output text file.
#
#          The resulting text file will automatically open.

import arcpy, datetime, os

try:

    #Read input parameters from GP dialog
    folderPath = arcpy.GetParameterAsText(0)
    output = arcpy.GetParameterAsText(1)

    #Create an output file
    outFile = open(output, "w")

    #Report header
    outFile.write("Layer REPORT: \n")
    outFile.write(" \n")
    outFile.write("This report is for all layer (lyr) files in a system folder.  It lists relevant layer\n")
    outFile.write("and group layer information.\n")
    outFile.write(" \n")
    outFile.write("Date:     " + str(datetime.datetime.today().strftime("%B %d, %Y")) + "\n")
    outFile.write("Location: " + folderPath + "\n")

    #Loop through each "LYR" file
    count = 0
    for filename in os.listdir(folderPath):
        fullpath = os.path.join(folderPath, filename)
        if os.path.isfile(fullpath):
            if filename.lower().endswith(".lyr"):
                
                #Reference LYR
                layerFile = arcpy.mapping.Layer(fullpath)
                
                #Write layer info to a file
                outFile.write("\n")
                outFile.write("\n")
                outFile.write("----------------------------------------------------------------------------------\n")
                outFile.write("Layer File: " + fullpath + "\n")
                outFile.write("----------------------------------------------------------------------------------\n")
                outFile.write("\n")

                #Reference each layer in a layer file
                count = 1
                for lyr in arcpy.mapping.ListLayers(layerFile):
                    outFile.write("\n")
                    outFile.write("\t Name:         " + lyr.name + "\n")
                    outFile.write("\t Long name:    " + lyr.longName + "\n")
                    outFile.write("\t Visible:      " + str(lyr.visible) + "\n")
                    if lyr.supports("DESCRIPTION"):
                        outFile.write("\t Description:  " + lyr.description + "\n")
                    if lyr.supports("SHOWLABELS"):
                        outFile.write("\t Labels on:    " + str(lyr.showLabels) + "\n")
                        if lyr.showLabels == True:
                            for labelClass in lyr.labelClasses:
                                outFile.write("\t\t Class name:   " + str(labelClass.className) + "\n")
                                outFile.write("\t\t Expression:   " + str(labelClass.expression) + "\n")
                                outFile.write("\t\t SQL Query:    " + str(labelClass.SQLQuery) + "\n")
                    if lyr.supports("DEFINITIONQUERY"):
                        outFile.write("\t Def query:    " + lyr.definitionQuery + "\n")
                    if lyr.supports("TRANSPARENCY"):
                        outFile.write("\t Transparency: " + str(lyr.transparency) + "\n")
                    if lyr.supports("BRIGHTNESS"):
                        outFile.write("\t Brightness:   " + str(lyr.brightness) + "\n")
                    if lyr.supports("CONTRAST"):
                        outFile.write("\t Contrast:     " + str(lyr.contrast) + "\n")
                    if lyr.supports("DATASOURCE"):
                        outFile.write("\t Data source:  " + str(lyr.dataSource) + "\n")
                        
                    #Write out Web and SDE services differently
                    if lyr.supports("SERVICEPROPERTIES"):
                        if lyr.serviceProperties["ServiceType"] != "SDE":
                            outFile.write("\t Service Type: " + lyr.serviceProperties.get('ServiceType', 'N/A') + "\n")
                            outFile.write("\t\t URL:          " + lyr.serviceProperties.get('URL', 'N/A') + "\n")
                            outFile.write("\t\t Connection:   " + lyr.serviceProperties.get('Connection', 'N/A') + "\n")
                            outFile.write("\t\t Server:       " + lyr.serviceProperties.get('Server', 'N/A') + "\n")
                            outFile.write("\t\t Cache:        " + str(lyr.serviceProperties.get('Cache', 'N/A')) + "\n")
                            outFile.write("\t\t Password:     " + lyr.serviceProperties.get('Password', 'N/A') + "\n")
                        else:
                            outFile.write("\t Service Type: " + lyr.serviceProperties.get('ServiceType', 'N/A') + "\n")
                            outFile.write("\t\t Database:       " + lyr.serviceProperties.get('Database', 'N/A') + "\n")
                            outFile.write("\t\t Server:         " + lyr.serviceProperties.get('Server', 'N/A') + "\n")
                            outFile.write("\t\t Service:        " + lyr.serviceProperties.get('Instance', 'N/A') + "\n")
                            outFile.write("\t\t Version:        " + lyr.serviceProperties.get('Version', 'N/A') + "\n")
                            outFile.write("\t\t User name:      " + lyr.serviceProperties.get('UserName', 'N/A') + "\n")
                            outFile.write("\t\t Authentication: " + lyr.serviceProperties.get('AuthenticationMode', 'N/A') + "\n")
                    outFile.write("\n")

                del layerFile
    if count ==0:
        outFile.write("\n")
        outFile.write("\n")
        outFile.write("---------------------------------------------------------------------------------- \n")
        outFile.write("                            NO LAYER FILES FOUND \n")
        outFile.write("---------------------------------------------------------------------------------- \n")
    outFile.close()

    #Open the resulting text file
    os.startfile(output)

    #Delete variables that reference data on disk
    del outFile
    
except Exception, e:
  import traceback
  map(arcpy.AddError, traceback.format_exc().split("\n"))
  arcpy.AddError(str(e))

