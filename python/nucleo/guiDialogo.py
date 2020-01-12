"""
    Esta es la clase que gestiona la GUI del QDialog
"""
# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from nucleo.Gui.DialogoConfirmacion_ui import Ui_Dialog
class DialogoConfirmacion(QDialog):

    def __init__(self, parent = None):

        
        super(DialogoConfirmacion, self).__init__(parent)
        self.uiDialogo = Ui_Dialog()
        self.uiDialogo.setupUi(self)


"""if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = DialogoConfirmacion()
    main.show()
    sys.exit(app.exec_()) """