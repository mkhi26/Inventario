# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoError.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 176)
        Dialog.setStyleSheet("")
        self.btnConfirmar = QtWidgets.QPushButton(Dialog)
        self.btnConfirmar.setGeometry(QtCore.QRect(300, 130, 101, 31))
        self.btnConfirmar.setStyleSheet("image: url(:/cct/confirm.png);\n"
"background-color: rgb(0, 85, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConfirmar.setIcon(icon)
        self.btnConfirmar.setIconSize(QtCore.QSize(30, 20))
        self.btnConfirmar.setObjectName("btnConfirmar")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 191))
        self.label_2.setStyleSheet("image: url(:/cct/error.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.txtError = QtWidgets.QLabel(Dialog)
        self.txtError.setGeometry(QtCore.QRect(90, 40, 321, 41))
        self.txtError.setStyleSheet("font: 75 10pt \"Tlwg Typo\";")
        self.txtError.setObjectName("txtError")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Error"))
        self.btnConfirmar.setText(_translate("Dialog", "Aceptar"))
        self.txtError.setText(_translate("Dialog", "No existe producto registrado con ese ID"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
