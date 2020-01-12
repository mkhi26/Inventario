# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agregar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 499)
        MainWindow.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(140, 60, 301, 31))
        self.txtNombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNombre.setObjectName("txtNombre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 231, 31))
        self.label.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 231, 31))
        self.label_2.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.txtCosto = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCosto.setGeometry(QtCore.QRect(140, 150, 301, 31))
        self.txtCosto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCosto.setObjectName("txtCosto")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 210, 231, 31))
        self.label_3.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.cbxMoneda = QtWidgets.QComboBox(self.centralwidget)
        self.cbxMoneda.setGeometry(QtCore.QRect(140, 240, 79, 23))
        self.cbxMoneda.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbxMoneda.setObjectName("cbxMoneda")
        self.cbxMoneda.addItem("")
        self.cbxMoneda.addItem("")
        self.txtDescripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDescripcion.setGeometry(QtCore.QRect(140, 330, 311, 70))
        self.txtDescripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescripcion.setObjectName("txtDescripcion")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 290, 281, 31))
        self.label_4.setStyleSheet("font: 14pt \"Padauk Book [SIL ]\";\n"
"    \n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(130, 430, 131, 41))
        self.btnCancelar.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
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
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(360, 430, 131, 41))
        self.btnAgregar.setStyleSheet("QPushButton {\n"
"\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
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
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 430, 59, 41))
        self.label_5.setStyleSheet("image: url(:/cct/agregar.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 430, 59, 41))
        self.label_6.setStyleSheet("image: url(:/cct/cancelar.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 50, 59, 41))
        self.label_7.setStyleSheet("image: url(:/cct/producto.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 140, 59, 41))
        self.label_8.setStyleSheet("image: url(:/cct/costo.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 220, 81, 41))
        self.label_9.setStyleSheet("image: url(:/cct/tipoMoneda.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 340, 81, 41))
        self.label_10.setStyleSheet("image: url(:/cct/tagdescription_102241.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_5.raise_()
        self.txtNombre.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.txtCosto.raise_()
        self.label_3.raise_()
        self.cbxMoneda.raise_()
        self.txtDescripcion.raise_()
        self.label_4.raise_()
        self.btnCancelar.raise_()
        self.btnAgregar.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.txtDescripcion.setText("Descripcion")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agregar producto a inventario"))
        self.txtNombre.setText(_translate("MainWindow", "Nombre"))
        self.label.setText(_translate("MainWindow", "Nombre del producto"))
        self.label_2.setText(_translate("MainWindow", "Costo del producto"))
        self.txtCosto.setText(_translate("MainWindow", "0.00"))
        self.label_3.setText(_translate("MainWindow", "Tipo de moneda"))
        self.cbxMoneda.setItemText(0, _translate("MainWindow", "HNL"))
        self.cbxMoneda.setItemText(1, _translate("MainWindow", "USD"))
        self.txtDescripcion.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Descripcion</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Descripcion de producto"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.btnAgregar.setText(_translate("MainWindow", "Agregar"))
#import recursos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
