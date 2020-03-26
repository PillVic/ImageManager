# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImageShower = QtWidgets.QGraphicsView(self.centralwidget)
        self.ImageShower.setGeometry(QtCore.QRect(-10, -50, 851, 631))
        self.ImageShower.setObjectName("ImageShower")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAlgorithm = QtWidgets.QMenu(self.menubar)
        self.menuAlgorithm.setObjectName("menuAlgorithm")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRecover = QtWidgets.QAction(MainWindow)
        self.actionRecover.setObjectName("actionRecover")
        self.actionAffine = QtWidgets.QAction(MainWindow)
        self.actionAffine.setObjectName("actionAffine")
        self.actionEdge_Detect = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detect.setObjectName("actionEdge_Detect")
        self.actionSelect = QtWidgets.QAction(MainWindow)
        self.actionSelect.setObjectName("actionSelect")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionRecover)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect)
        self.menuAlgorithm.addAction(self.actionAffine)
        self.menuAlgorithm.addAction(self.actionEdge_Detect)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAlgorithm.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Manager"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAlgorithm.setTitle(_translate("MainWindow", "Algorithm"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRecover.setText(_translate("MainWindow", "Recover"))
        self.actionAffine.setText(_translate("MainWindow", "Affine"))
        self.actionEdge_Detect.setText(_translate("MainWindow", "Edge Detect"))
        self.actionSelect.setText(_translate("MainWindow", "Select"))
