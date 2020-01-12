# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercaDe.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 436)
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 391, 31))
        self.label.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 201, 131))
        self.label_2.setStyleSheet("image: url(:/cct/logos-UNAH-11.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 180, 391, 31))
        self.label_3.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 310, 231, 31))
        self.label_4.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 340, 291, 31))
        self.label_5.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 127);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 220, 101, 31))
        self.label_6.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 270, 251, 31))
        self.label_7.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Acerca de"))
        self.label.setText(_translate("MainWindow", "Universidad Nacional Autonoma de Honduras"))
        self.label_3.setText(_translate("MainWindow", "ALGORITMOS Y ESTRUCTURAS DE DATOS"))
        self.label_4.setText(_translate("MainWindow", "Por:"))
        self.label_5.setText(_translate("MainWindow", "Amilcar Rodriguez    20172500133"))
        self.label_6.setText(_translate("MainWindow", "Proyecto #1"))
        self.label_7.setText(_translate("MainWindow", "Sistema de inventario simple"))
#import recursos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
