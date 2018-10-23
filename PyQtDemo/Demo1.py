# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtCore, QtGui


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('PyQt')
        self.resize(300, 200)
        label = QtGui.QLabel('label')
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(label)
        button = QtGui.QPushButton('b1')


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MyWin = MyWindow()
    MyWin.show()
    app.exec_()
