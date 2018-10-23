# -*- coding: utf-8 -*-


import os
import os.path
import sys
import arcpy
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
        Dialog.resize(696, 505)

        self.l_source = QtGui.QLabel(Dialog)
        self.l_source.setGeometry(QtCore.QRect(70, 40, 101, 31))
        self.l_source.setObjectName(_fromUtf8("l_source"))
        self.font(self.l_source, "微软雅黑", 12, False, False, False)

        self.cb_source = QtGui.QComboBox(Dialog)
        self.cb_source.setGeometry(QtCore.QRect(190, 40, 301, 31))
        self.cb_source.setObjectName(_fromUtf8("cb_source"))
        self.cb_source.setEditable(True)
        self.cb_source.addItem(QtCore.QDir.currentPath())
        self.font(self.cb_source, "宋体", 12, False, False, False)

        self.b_source = QtGui.QPushButton(Dialog)
        self.b_source.setGeometry(QtCore.QRect(520, 40, 91, 31))
        self.b_source.setObjectName(_fromUtf8("b_source"))
        self.b_source.clicked.connect(self.openDir_source)
        self.font(self.b_source, "楷体", 13, False, True, False)

        self.cb_clip = QtGui.QComboBox(Dialog)
        self.cb_clip.setGeometry(QtCore.QRect(190, 100, 301, 31))
        self.cb_clip.setObjectName(_fromUtf8("cb_clip"))
        self.cb_clip.setEditable(True)
        self.font(self.cb_clip, "宋体", 12, False, False, False)

        self.l_clip = QtGui.QLabel(Dialog)
        self.l_clip.setGeometry(QtCore.QRect(70, 100, 101, 31))
        self.l_clip.setObjectName(_fromUtf8("l_clip"))
        self.font(self.l_clip, "微软雅黑", 12, False, False, False)

        self.b_clip = QtGui.QPushButton(Dialog)
        self.b_clip.setGeometry(QtCore.QRect(520, 100, 91, 31))
        self.b_clip.setObjectName(_fromUtf8("b_clip"))
        self.b_clip.clicked.connect(self.openFile)
        self.font(self.b_clip, "楷体", 13, False, True, False)

        self.l_result = QtGui.QLabel(Dialog)
        self.l_result.setGeometry(QtCore.QRect(70, 160, 101, 31))
        self.l_result.setObjectName(_fromUtf8("l_result"))
        self.font(self.l_result, "微软雅黑", 12, False, False, False)

        self.b_result = QtGui.QPushButton(Dialog)
        self.b_result.setGeometry(QtCore.QRect(520, 160, 91, 31))
        self.b_result.setObjectName(_fromUtf8("b_result"))
        self.b_result.clicked.connect(self.openDir_result)
        self.font(self.b_result, "楷体", 13, False, True, False)

        self.cb_result = QtGui.QComboBox(Dialog)
        self.cb_result.setGeometry(QtCore.QRect(190, 160, 301, 31))
        self.cb_result.setObjectName(_fromUtf8("cb_result"))
        self.cb_result.setEditable(True)
        self.cb_result.addItem(QtCore.QDir.currentPath())
        self.font(self.cb_result, "宋体", 12, False, False, False)

        self.tb_show = QtGui.QTextBrowser(Dialog)
        self.tb_show.setGeometry(QtCore.QRect(70, 270, 541, 211))
        self.tb_show.setObjectName(_fromUtf8("tb_show"))
        # self.tb_show.setText("aaaa")




        self.b_execute = QtGui.QPushButton(Dialog)
        self.b_execute.setGeometry(QtCore.QRect(450, 210, 121, 41))
        self.b_execute.setObjectName(_fromUtf8("b_execute"))
        self.b_execute.clicked.connect(self.execute)
        self.font(self.b_execute, "微软雅黑", 15, True, True, True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Many Vector Later Clip", None))
        self.l_source.setText(_translate("Dialog", "SourceData File：", None))
        self.b_source.setText(_translate("Dialog", "Beowser...", None))
        self.l_clip.setText(_translate("Dialog", "ClipData File：", None))
        self.b_clip.setText(_translate("Dialog", "Beowser...", None))
        self.l_result.setText(_translate("Dialog", "ResultData File：", None))
        self.b_result.setText(_translate("Dialog", "Beowser...", None))
        self.b_execute.setText(_translate("Dialog", "Execute", None))

    # 自定义函数
    def keyPressEvent(self):
        if e.key() == QtCore.Qt.Key_Escape():
            Dialog.close()

    def openDir_source(self):
        directory = QtGui.QFileDialog.getExistingDirectory(None,
                                                           "Find FIles",
                                                           QtCore.QDir.currentPath())
        if self.cb_source.findText(directory) == -1:
            self.cb_source.addItem(directory)
            self.cb_source.setCurrentIndex(self.cb_source.findText(directory))

    def openDir_result(self):
        directory = QtGui.QFileDialog.getExistingDirectory(None,
                                                           "Find FIles",
                                                           QtCore.QDir.currentPath())
        if self.cb_result.findText(directory) == -1:
            self.cb_result.addItem(directory)
            self.cb_result.setCurrentIndex(self.cb_result.findText(directory))

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(None,
                                                     "Open FileName",
                                                     self.cb_source.currentText(),
                                                     "Shp Files (*.shp);;All Files (*)")

        if filename:
            self.cb_clip.addItem(filename)
            self.cb_clip.setCurrentIndex(self.cb_clip.findText(filename))

    def execute(self):
        pass

    def execute1(self):
        sourceName = str(self.cb_source.currentText())
        clipName = str(self.cb_clip.currentText())
        resultName = str(self.cb_result.currentText())
        # print sourceName+clipName+resultName

        arcpy.env.workspace = sourceName
        num = 0

        ClipName = os.path.split(clipName)[1]

        for i in arcpy.ListFiles("*.shp"):
            num = num + 1
            print u"执行次数num=", num, u"被裁剪要素：", i, u"裁剪要素：", ClipName
            # self.tb_show.append(u"执行次数num=",num,u"被裁剪要素：",i,u"裁剪要素：",ClipName)
            # self.tb_show.append(u"执行次数num=")

            # self.tb_show.append(num)
            # self.tb_show.append("被裁剪要素：")
            # self.tb_show.append(i)
            # self.tb_show.append("裁剪要素：")
            # self.tb_show.append(ClipName)

            try:
                arcpy.Clip_analysis(os.path.join(sourceName, i), clipName, os.path.join(resultName, i), '.0000001 DecimalDegrees')
                print "Finish"
            except Exception as e:
                print(e.message)

        self.tb_show("Finish")

    def font(self, com, par1, par2, par3, par4, par5):
        # com代表组件名称
        # par1代表字体类型
        # par2字体大小
        # par3字体加粗
        # par4字体斜体
        # par5字体下划线
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(par1))
        font.setPixelSize(par2)
        font.setBold(par3)
        font.setItalic(par4)
        font.setUnderline(par5)
        com.setFont(font)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
