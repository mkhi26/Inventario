# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from nucleo.Gui.DialogoError_ui import Ui_Dialog
class DialogoError(QDialog):

    def __init__(self, parent = None):

        
        super(DialogoError, self).__init__(parent)
        self.uiDialogoError = Ui_Dialog()
        self.uiDialogoError.setupUi(self)
