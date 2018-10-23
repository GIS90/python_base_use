# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(454, 274)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.user_but = QtGui.QPushButton(self.centralwidget)
        self.user_but.setGeometry(QtCore.QRect(70, 60, 111, 41))
        self.user_but.setObjectName(_fromUtf8("user_but"))
        self.user_fcb = QtGui.QFontComboBox(self.centralwidget)
        self.user_fcb.setGeometry(QtCore.QRect(200, 60, 191, 41))
        self.user_fcb.setObjectName(_fromUtf8("user_fcb"))
        self.passwd_but = QtGui.QPushButton(self.centralwidget)
        self.passwd_but.setGeometry(QtCore.QRect(70, 130, 111, 41))
        self.passwd_but.setObjectName(_fromUtf8("passwd_but"))
        self.passwd_le = QtGui.QLineEdit(self.centralwidget)
        self.passwd_le.setGeometry(QtCore.QRect(200, 130, 191, 41))
        self.passwd_le.setObjectName(_fromUtf8("passwd_le"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 454, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.user_but.setText(_translate("MainWindow", "用户名：", None))
        self.passwd_but.setText(_translate("MainWindow", "密  码：", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
