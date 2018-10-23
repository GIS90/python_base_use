# -*- coding: utf-8 -*-

import arcpy

import createSHP


def funCshp():
    print q
    workspace = str(createSHP.Ui_Dialog.cb_workspace.currentText())
    shpname = str(createSHP.Ui_Dialog.t_shpname.toPlainText())
    shptype = str(createSHP.Ui_Dialog.cb_shptype.currentText())
    shpgcs = str(createSHP.Ui_Dialog.cb_shpgcs.currentText())

    createSHP.Ui_Dialog.verificate()

    if shpgcs == "wgs84":
        gcs = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision"
    elif shpgcs == "xian80":
        gcs = "GEOGCS['GCS_Xian_1980',DATUM['D_Xian_1980',SPHEROID['Xian_1980',6378140.0,298.257]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98314861591033E-09;.001;.001;IsHighPrecision"
    else:
        gcs = "GEOGCS['GCS_Beijing_1954',DATUM['D_Beijing_1954',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.9830007334435E-09;.001;.001;IsHighPrecision"

    name = shpname + ".shp"

    template = ""
    has_m = "DISABLED"
    has_z = "DISABLED"
    arcpy.env.workspace = workspace

    try:
        arcpy.CreateFeatureclass_management(workspace, name, shptype, template, has_m, has_z, gcs)
        print "Create " + name + " Success!"
    except Exception as e:
        print "Occur Exception :" + str(e)
