# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoConfirmacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 151)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.lblTexto = QtWidgets.QLabel(Dialog)
        self.lblTexto.setGeometry(QtCore.QRect(100, 50, 181, 31))
        self.lblTexto.setObjectName("lblTexto")
        self.btnConfirmar = QtWidgets.QPushButton(Dialog)
        self.btnConfirmar.setGeometry(QtCore.QRect(210, 110, 101, 23))
        self.btnConfirmar.setStyleSheet("image: url(:/cct/confirm.png);\n"
"background-color: rgb(0, 85, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfirmar.setIcon(icon)
        self.btnConfirmar.setIconSize(QtCore.QSize(30, 20))
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        self.btnCancelar.setGeometry(QtCore.QRect(90, 110, 91, 23))
        self.btnCancelar.setStyleSheet("background-color: rgb(0, 85, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon1)
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 59, 41))
        self.label_2.setStyleSheet("image: url(:/cct/cuestion.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btnConfirmar, self.btnCancelar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTexto.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lblTexto.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">¿Esta seguro?</span></p></body></html>"))
        self.btnConfirmar.setText(_translate("Dialog", "Confirmar"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
#import recursos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
