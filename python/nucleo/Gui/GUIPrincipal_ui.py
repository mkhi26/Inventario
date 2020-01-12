# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 361)
        MainWindow.setStyleSheet("background-color: rgb(85, 0, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnVerEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerEditar.setGeometry(QtCore.QRect(100, 140, 271, 41))
        self.btnVerEditar.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    \n"
"    \n"
"    font: 57 italic 14pt \"URW Chancery L\";\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnVerEditar.setObjectName("btnVerEditar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 70, 291, 31))
        self.label.setStyleSheet("    font: 57 italic 25pt \"URW Chancery L\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.btnAgregarInventario = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarInventario.setGeometry(QtCore.QRect(100, 70, 271, 41))
        self.btnAgregarInventario.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    background-image: url(:/cct/Acerca de.png);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 57 italic 14pt \"URW Chancery L\";\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnAgregarInventario.setObjectName("btnAgregarInventario")
        self.btnArbolBinario = QtWidgets.QPushButton(self.centralwidget)
        self.btnArbolBinario.setGeometry(QtCore.QRect(100, 210, 271, 41))
        self.btnArbolBinario.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    font: 57 italic 14pt \"URW Chancery L\";\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnArbolBinario.setObjectName("btnArbolBinario")
        self.btnAcercaDe = QtWidgets.QPushButton(self.centralwidget)
        self.btnAcercaDe.setGeometry(QtCore.QRect(100, 290, 271, 41))
        self.btnAcercaDe.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    font: 57 italic 14pt \"URW Chancery L\";\n"
"    \n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    background-color: rgb(0, 85, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"    }")
        self.btnAcercaDe.setObjectName("btnAcercaDe")
        self.lblContador = QtWidgets.QLabel(self.centralwidget)
        self.lblContador.setGeometry(QtCore.QRect(540, 180, 101, 61))
        self.lblContador.setStyleSheet("font: 75 40pt \"Century Schoolbook L\";\n"
"color: rgb(255, 255, 255);")
        self.lblContador.setObjectName("lblContador")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 130, 241, 171))
        self.label_2.setStyleSheet("image: url(:/cct/circulo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 41, 31))
        self.label_3.setStyleSheet("\n"
"image: url(:/cct/AgregarInventario.png);\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 41, 31))
        self.label_4.setStyleSheet("image: url(:/cct/verLista.png);\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 41, 31))
        self.label_5.setStyleSheet("image: url(:/cct/Active_Directory-80_icon-icons.com_57383.png);\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 300, 41, 31))
        self.label_6.setStyleSheet("image: url(:/cct/Acerca de.png);\n"
"background-color: rgb(255, 255, 127);\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(420, 50, 31, 291))
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3.raise_()
        self.label_2.raise_()
        self.btnVerEditar.raise_()
        self.label.raise_()
        self.btnAgregarInventario.raise_()
        self.btnArbolBinario.raise_()
        self.btnAcercaDe.raise_()
        self.lblContador.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de inventario"))
        self.btnVerEditar.setText(_translate("MainWindow", "Ver y editar inventario"))
        self.label.setText(_translate("MainWindow", "Productos en inventario"))
        self.btnAgregarInventario.setText(_translate("MainWindow", "Agregar a inventario"))
        self.btnArbolBinario.setText(_translate("MainWindow", "Arbol binario de costos"))
        self.btnAcercaDe.setText(_translate("MainWindow", "Acerca de"))
        self.lblContador.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lblContador.setText(_translate("MainWindow", "000"))
#import recursos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
