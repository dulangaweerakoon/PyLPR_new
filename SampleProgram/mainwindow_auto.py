# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(479, 320)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnOn = QtWidgets.QPushButton(self.centralWidget)
        self.btnOn.setGeometry(QtCore.QRect(10, 210, 121, 41))
        self.btnOn.setObjectName("btnOn")
        self.imageLabel = QtWidgets.QLabel(self.centralWidget)
        self.imageLabel.setGeometry(QtCore.QRect(10, 0, 451, 181))
        self.imageLabel.setObjectName("imageLabel")
        self.LPRlabel = QtWidgets.QLabel(self.centralWidget)
        self.LPRlabel.setGeometry(QtCore.QRect(170, 220, 241, 31))
        self.LPRlabel.setObjectName("LPRlabel")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 479, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOn.setText(_translate("MainWindow", "Capture"))
        self.imageLabel.setText(_translate("MainWindow", "Image "))
        self.LPRlabel.setText(_translate("MainWindow", "LPR"))

