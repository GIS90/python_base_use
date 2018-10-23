# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myTextBrowser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Dialog.resize(813, 570)

        self.l_title = QtGui.QLabel(Dialog)
        self.l_title.setGeometry(QtCore.QRect(300, 10, 191, 31))
        self.l_title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.l_title.setTextFormat(QtCore.Qt.AutoText)
        self.l_title.setObjectName(_fromUtf8("l_title"))

        self.te_content = QtGui.QTextEdit(Dialog)
        self.te_content.setGeometry(QtCore.QRect(10, 100, 631, 401))
        self.te_content.setObjectName(_fromUtf8("te_content"))

        self.te_info = QtGui.QTextEdit(Dialog)
        self.te_info.setGeometry(QtCore.QRect(10, 520, 450, 30))
        self.te_info.setObjectName(_fromUtf8("te_info"))

        self.cb_pathName = QtGui.QComboBox(Dialog)
        self.cb_pathName.setGeometry(QtCore.QRect(10, 50, 631, 41))
        self.cb_pathName.setObjectName(_fromUtf8("cb_pathName"))
        self.cb_pathName.setEditable(True)
        self.cb_pathName.addItem(QtCore.QDir.currentPath())

        self.pb_create = QtGui.QPushButton(Dialog)
        self.pb_create.setGeometry(QtCore.QRect(670, 50, 111, 41))
        self.pb_create.setObjectName(_fromUtf8("pb_create"))
        self.pb_create.clicked.connect(self.createFile)

        self.dateTimeEdit = QtGui.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(550, 520, 250, 30))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))

        self.pb_save = QtGui.QPushButton(Dialog)
        self.pb_save.setGeometry(QtCore.QRect(670, 160, 111, 41))
        self.pb_save.setObjectName(_fromUtf8("pb_save"))

        self.pb_delete = QtGui.QPushButton(Dialog)
        self.pb_delete.setGeometry(QtCore.QRect(670, 270, 111, 41))
        self.pb_delete.setObjectName(_fromUtf8("pb_delete"))

        self.pb_open = QtGui.QPushButton(Dialog)
        self.pb_open.setGeometry(QtCore.QRect(670, 380, 111, 41))
        self.pb_open.setObjectName(_fromUtf8("pb_open"))
        self.pb_open.clicked.connect(self.openFile)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.l_title.setText(_translate("Dialog", "My Text Browser", None))
        self.pb_create.setText(_translate("Dialog", "Create", None))
        self.pb_save.setText(_translate("Dialog", "Save", None))
        self.pb_delete.setText(_translate("Dialog", "Delete", None))
        self.pb_open.setText(_translate("Dialog", "Open", None))


    def createFile(self):
        dirCreateFile=QtGui.QFileDialog.getSaveFileName(None,'Create File',QtCore.QDir.currentPath())
        open(dirCreateFile,'w')
    def openFile(self):
        dirOpenFile=QtGui.QFileDialog.getOpenFileName(None,'Open File',QtCore.QDir.currentPath())
        if self.cb_pathName.findText(dirOpenFile)==-1:
            self.cb_pathName.addItem(dirOpenFile)
            self.cb_pathName.setCurrentIndex(self.cb_pathName.findText(dirOpenFile))
        fOpen=open(dirOpenFile,'r')
        fContent=fOpen.read()
        self.te_content.setText(fContent)





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

