# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findfp.ui'
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
        Dialog.resize(795, 366)
        self.b_open = QtGui.QPushButton(Dialog)
        self.b_open.setGeometry(QtCore.QRect(500, 70, 81, 41))
        self.b_open.setObjectName(_fromUtf8("b_open"))
        self.b_open.clicked.connect(self.browse)



        self.c_filepath = QtGui.QComboBox(Dialog)
        self.c_filepath.setGeometry(QtCore.QRect(130, 70, 311, 41))
        self.c_filepath.setObjectName(_fromUtf8("c_filepath"))
        self.c_filepath.setEditable(True)
        self.c_filepath.addItem(QtCore.QDir.currentPath())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.b_open.setText(_translate("Dialog", "打开。。。", None))


    def browse(self):
        fileName = QtGui.QFileDialog.getOpenFileName(None,
                "QFileDialog.getOpenFileName()",
                self.c_filepath.currentText(),
                "All Files (*);;Text Files (*.shp)")
        if fileName:
            self.c_filepath.addItem(fileName)
            self.c_filepath.setCurrentIndex(self.c_filepath.findText(fileName))

    # def browse(self):
    #     directory=QtGui.QFileDialog.getExistingDirectory(None,"Find Files",QtCore.QDir.currentPath())
    #     self.c_filepath.addItem(directory)
    #     self.c_filepath.setCurrentIndex(self.c_filepath.findText(directory))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

