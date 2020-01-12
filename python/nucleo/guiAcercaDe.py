# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from nucleo.Gui.GUIAcercaDe_ui import Ui_MainWindow
class VentanaAcercaDe (QMainWindow):

    def __init__(self, parent = None):

        
        super(VentanaAcercaDe, self).__init__(parent)
        self.uiAcercaDe = Ui_MainWindow()
        self.uiAcercaDe.setupUi(self)