# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(656, 358)
        self.cb_workspace = QtGui.QComboBox(Dialog)
        self.cb_workspace.setGeometry(QtCore.QRect(170, 80, 311, 31))
        self.cb_workspace.setObjectName(_fromUtf8("cb_workspace"))
        self.cb_workspace.setEditable(True)
        self.cb_workspace.addItem(QtCore.QDir.currentPath())


        self.t_shpname = QtGui.QTextEdit(Dialog)
        self.t_shpname.setGeometry(QtCore.QRect(170, 130, 271, 31))
        self.t_shpname.setObjectName(_fromUtf8("t_shpname"))



        self.cb_shptype = QtGui.QComboBox(Dialog)
        self.cb_shptype.setGeometry(QtCore.QRect(170, 180, 271, 31))
        self.cb_shptype.setObjectName(_fromUtf8("cb_shptype"))
        self.cb_shptype.addItem(_fromUtf8(""))
        self.cb_shptype.addItem(_fromUtf8(""))
        self.cb_shptype.addItem(_fromUtf8(""))
        self.cb_shptype.addItem(_fromUtf8(""))



        self.l_workspace = QtGui.QLabel(Dialog)
        self.l_workspace.setGeometry(QtCore.QRect(70, 80, 71, 31))
        self.l_workspace.setObjectName(_fromUtf8("l_workspace"))


        self.l_shpname = QtGui.QLabel(Dialog)
        self.l_shpname.setGeometry(QtCore.QRect(70, 130, 71, 31))
        self.l_shpname.setObjectName(_fromUtf8("l_shpname"))



        self.l_shptype = QtGui.QLabel(Dialog)
        self.l_shptype.setGeometry(QtCore.QRect(70, 180, 71, 31))
        self.l_shptype.setObjectName(_fromUtf8("l_shptype"))


        self.l_shpgcs = QtGui.QLabel(Dialog)
        self.l_shpgcs.setGeometry(QtCore.QRect(70, 230, 71, 31))
        self.l_shpgcs.setObjectName(_fromUtf8("l_shpgcs"))



        self.b_browser = QtGui.QPushButton(Dialog)
        self.b_browser.setGeometry(QtCore.QRect(510, 80, 75, 31))
        self.b_browser.setObjectName(_fromUtf8("b_browser"))
        self.b_browser.clicked.connect(self.browse)



        self.b_verificate = QtGui.QPushButton(Dialog)
        self.b_verificate.setGeometry(QtCore.QRect(490, 140, 91, 41))
        self.b_verificate.setObjectName(_fromUtf8("b_verificate"))
        self.b_verificate.clicked.connect(self.verificate)


        self.b_execute = QtGui.QPushButton(Dialog)
        self.b_execute.setGeometry(QtCore.QRect(490, 200, 91, 41))
        self.b_execute.setObjectName(_fromUtf8("b_execute"))
        self.b_execute.clicked.connect(self.execute)


        self.cb_shpgcs = QtGui.QComboBox(Dialog)
        self.cb_shpgcs.setGeometry(QtCore.QRect(170, 230, 271, 31))
        self.cb_shpgcs.setObjectName(_fromUtf8("cb_shpgcs"))
        self.cb_shpgcs.addItem(_fromUtf8(""))
        self.cb_shpgcs.addItem(_fromUtf8(""))
        self.cb_shpgcs.addItem(_fromUtf8(""))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create_ShpFile", None))
        self.cb_shptype.setItemText(0, _translate("Dialog", "POINT", None))
        self.cb_shptype.setItemText(1, _translate("Dialog", "POLYLINE", None))
        self.cb_shptype.setItemText(2, _translate("Dialog", "POLYGON", None))
        self.cb_shptype.setItemText(3, _translate("Dialog", "MULTPOINT", None))
        self.l_workspace.setText(_translate("Dialog", "workSpace:", None))
        self.l_shpname.setText(_translate("Dialog", "shpName:", None))
        self.l_shptype.setText(_translate("Dialog", "shpType:", None))
        self.l_shpgcs.setText(_translate("Dialog", "shpGcs:", None))
        self.b_browser.setText(_translate("Dialog", "Browser...", None))
        self.b_verificate.setText(_translate("Dialog", "Verificate", None))
        self.b_execute.setText(_translate("Dialog", "Execute", None))
        self.cb_shpgcs.setItemText(0, _translate("Dialog", "wgs84", None))
        self.cb_shpgcs.setItemText(1, _translate("Dialog", "beijing54", None))
        self.cb_shpgcs.setItemText(2, _translate("Dialog", "xian80", None))



    def browse(self):
        directory=QtGui.QFileDialog.getExistingDirectory(None,"Find FIles",QtCore.QDir.currentPath())
        if self.cb_workspace.findText(directory)==-1:
            self.cb_workspace.addItem(directory)
            self.cb_workspace.setCurrentIndex(self.cb_workspace.findText(directory))

    def verificate(self):
        workspace=str(self.cb_workspace.currentText())
        shpname=str(self.t_shpname.toPlainText())

        if workspace=="":
            print "Occur Exception :workSpace Not Allowed Null"
        elif shpname=="":
            print "Occur Exception :shpName Not Allowed Null"
        else:
            print "Verificate Pass@"

    def execute(self):
        workspace=str(self.cb_workspace.currentText())
        shpname=str(self.t_shpname.toPlainText())
        shptype=str(self.cb_shptype.currentText())
        shpgcs=str(self.cb_shpgcs.currentText())

        self.verificate()

        if shpgcs=="wgs84":
            gcs="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;.001;.001;IsHighPrecision"
        elif shpgcs=="xian80":
            gcs="GEOGCS['GCS_Xian_1980',DATUM['D_Xian_1980',SPHEROID['Xian_1980',6378140.0,298.257]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98314861591033E-09;.001;.001;IsHighPrecision"
        else:
            gcs="GEOGCS['GCS_Beijing_1954',DATUM['D_Beijing_1954',SPHEROID['Krasovsky_1940',6378245.0,298.3]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.9830007334435E-09;.001;.001;IsHighPrecision"

        name=shpname+".shp"

        template=""
        has_m="DISABLED"
        has_z="DISABLED"
        #arcpy.env.workspace=workspace
        my_dir=os.path.dirname(sys.argv[0])
        try:
            os.system('%s %s %s %s %s %s %s %s %s'%(sys.executable,os.path.join(my_dir,'createShpFun.py'),workspace,name,shptype,template,has_m,has_z,gcs))
            # createShpFun.createShp(workspace,name,shptype,template,has_m,has_z,gcs)
            #arcpy.CreateFeatureclass_management(workspace,name,shptype,template,has_m,has_z,gcs)
            #print "Create "+name+" Success!"
        except Exception as e:
            print "Occur Exception :" + str(e)


    def keyPressEvent(self,e):
        if e.key()==QtCore.Qt.Key_Escape:
            Dialog.close()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

