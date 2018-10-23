# - * - coding : utf-8 - * -



import arcpy


def createFS(sdeFile):
    print "Create FeatureSet in ", sdeFile
    wgs1984 = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984'," \
              "6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision"
    # FeatureSet Name
    fsName = "test1"

    arcpy.CreateFeatureDataset_management(sdeFile, fsName, wgs1984)

    print "Create ", fsName, " In ", sdeFile, "Success......."
    return fsName


