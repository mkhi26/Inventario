# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VerEditar.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VerEditar_ventana(object):
    def setupUi(self, VerEditar_ventana):
        VerEditar_ventana.setObjectName("VerEditar_ventana")
        VerEditar_ventana.resize(681, 415)
        VerEditar_ventana.setStyleSheet("background-color: rgb(218, 214, 205);")
        self.centralwidget = QtWidgets.QWidget(VerEditar_ventana)
        self.centralwidget.setObjectName("centralwidget")
        self.txtTabla = QtWidgets.QTextEdit(self.centralwidget)
        self.txtTabla.setGeometry(QtCore.QRect(10, 20, 651, 261))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.txtTabla.setFont(font)
        self.txtTabla.setMouseTracking(True)
        self.txtTabla.setTabletTracking(False)
        self.txtTabla.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtTabla.setAutoFillBackground(False)
        self.txtTabla.setStyleSheet("background-color: rgb(244, 255, 231);\n"
"font: 25 10pt \"Ubuntu\";")
        self.txtTabla.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtTabla.setObjectName("txtTabla")
        self.txtEditar = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEditar.setGeometry(QtCore.QRect(190, 290, 151, 31))
        self.txtEditar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtEditar.setObjectName("txtEditar")
        self.btnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditar.setGeometry(QtCore.QRect(60, 340, 131, 41))
        self.btnEditar.setStyleSheet("QPushButton {\n"
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
        self.btnEditar.setObjectName("btnEditar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(410, 340, 131, 41))
        self.btnEliminar.setStyleSheet("QPushButton {\n"
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
        self.btnEliminar.setObjectName("btnEliminar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 340, 71, 41))
        self.label.setStyleSheet("image: url(:/cct/btnEditar.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 340, 71, 41))
        self.label_2.setStyleSheet("image: url(:/cct/btnEliminar.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.txtTabla.raise_()
        self.txtEditar.raise_()
        self.btnEditar.raise_()
        self.btnEliminar.raise_()
        self.label_2.raise_()
        VerEditar_ventana.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VerEditar_ventana)
        self.statusbar.setObjectName("statusbar")
        VerEditar_ventana.setStatusBar(self.statusbar)

        self.retranslateUi(VerEditar_ventana)
        QtCore.QMetaObject.connectSlotsByName(VerEditar_ventana)

    def retranslateUi(self, VerEditar_ventana):
        _translate = QtCore.QCoreApplication.translate
        VerEditar_ventana.setWindowTitle(_translate("VerEditar_ventana", "Ver y editar"))
        self.txtEditar.setText(_translate("VerEditar_ventana", "Id a editar o eliminar"))
        self.btnEditar.setText(_translate("VerEditar_ventana", "Editar"))
        self.btnEliminar.setText(_translate("VerEditar_ventana", "Eliminar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VerEditar_ventana = QtWidgets.QMainWindow()
    ui = Ui_VerEditar_ventana()
    ui.setupUi(VerEditar_ventana)
    VerEditar_ventana.show()
    sys.exit(app.exec_())
