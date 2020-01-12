# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from nucleo.Gui.GUIAgregar_ui import Ui_MainWindow
from nucleo.LinkedList import *
from nucleo.Producto import *
from nucleo.guiDialogo import DialogoConfirmacion
from nucleo.Memoria import *
class VentanaAgregar(QMainWindow):

    def __init__(self, parent = None):

        
        super(VentanaAgregar, self).__init__(parent)
        self.uiAgregar = Ui_MainWindow()
        self.uiAgregar.setupUi(self)
        self.memoria = Memoria()
        self.listaProductos=  self.memoria.getLista()
        self.memoria.setLista(self.listaProductos)
        self.maximo = self.memoria.getMaximo()


    """
        Metodos set y get de la lista de productos.
    """

    def getLista(self):
        lista = self.listaProductos
        return lista

    def setLista(self, lista):
        self.listaProductos = lista
        return True

    def activarAgregando(self):
        self.agregando = True
        return True




    """
    Nombre: agregarProductos
    Parametros: No recibe parametros.
    Retorno: Retorna True en caso de que se agregue correctamente, False en caso contrario.
    Descripcion: Esta funcion agrega objetos de tipo producto a la lista enlazada.

    """

    def agregarProductos(self):
    

        # 1. Primero obtenemos los valores de los textBox y comboBox
        nombreProducto = self.uiAgregar.txtNombre.text()
        costoProducto = float(self.uiAgregar.txtCosto.text())
        tipoMoneda = str(self.uiAgregar.cbxMoneda.currentText())
        descripcionProducto = self.uiAgregar.txtDescripcion.toPlainText()
        idProducto = int(self.maximo)
        """ 
        1.Se crea la instancia del objeto producto:
        2. Se asignan los valores a los atributos mediante los metodos set
         
        """
        agregarObjProducto = Producto() # Se crea la instancia
        # Se asignan valores a las variables mediante los metodos set

        agregarObjProducto.setNombreProducto(nombreProducto)
        agregarObjProducto.setCosto(costoProducto)
        agregarObjProducto.setMoneda(tipoMoneda)
        agregarObjProducto.setDescripcion(descripcionProducto)
        agregarObjProducto.setIdProducto(idProducto)

            
        self.listaProductos.LinkedListAdd(agregarObjProducto) # Se agrega el objeto a la Lista
        self.memoria.setLista(self.listaProductos) # Lista va a Memoria
        self.memoria.generarCsv()
        self.maximo = self.maximo +1
        self.memoria.setMaximo(self.maximo)
        self.limpiarTextBox()
        self.agregando = False


        return True

    def editarProducto(self, idProducto):

        obj = self.listaProductos.getObjProducto(idProducto)
        # 1. Primero obtenemos los valores de los textBox y comboBox
        nombreProductoEdit = self.uiAgregar.txtNombre.text()
        costoProductoEdit = float(self.uiAgregar.txtCosto.text())
        tipoMonedaEdit = str(self.uiAgregar.cbxMoneda.currentText())
        descripcionProductoEdit = self.uiAgregar.txtDescripcion.toPlainText()
        idProducto = obj.getIdProducto()

        obj.setNombreProducto(nombreProductoEdit)
        obj.setCosto(costoProductoEdit)
        obj.setIdProducto(idProducto)
        obj.setMoneda(tipoMonedaEdit)
        obj.setDescripcion(descripcionProductoEdit)

        # Se remplaza el objeto
        self.listaProductos.LinkedListEditar(obj)
        self.memoria.setLista(self.listaProductos) # Lista va a Memoria
        self.memoria.generarCsv()
        self.limpiarTextBox()
        return True

    def eliminarObj(self, idEliminar):
        index = self.listaProductos.LinkedListSearch(idEliminar)
        self.listaProductos.LinkedListPop(index)
        self.memoria.setLista(self.listaProductos) # Lista va a Memoria
        self.memoria.generarCsv()
        return True
        


    def limpiarTextBox(self):
        self.uiAgregar.txtNombre.setText("")
        self.uiAgregar.txtDescripcion.setText("")
        self.uiAgregar.txtCosto.setText("")
        return True
    



