# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from nucleo.Gui.GUIVerEditar_ui import Ui_VerEditar_ventana
from nucleo.LinkedList import *
from nucleo.Producto import *
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QInputEvent, QMouseEvent


class ventanaVerEditar (QMainWindow):

    def __init__(self, parent = None):

        
        super(ventanaVerEditar, self).__init__(parent)
        self.uiVerEditar = Ui_VerEditar_ventana()
        self.uiVerEditar.setupUi(self)



    def crearTabla(self, listaProductos ):
        tamanio = listaProductos.GetSize()
        renglones = "-"*200
        titulo =renglones + "\n"
        titulo += " "*90
        
        titulo += "Inventario de productos\n"
        titulo += renglones
        
        if(tamanio ==0):
            encabezado = titulo + "\nid\t|\tNombre\t|\tCosto\t|\tDescripcion "
            encabezado += "\n"+renglones
            return encabezado

        maximos = self.getMaximosTabla(listaProductos)


        nId=maximos[0]
        nNombre = maximos[1]
        nCosto = 4 + maximos[2]
        nDescripcion = maximos[3]
    
        espaciosId = " "*(nId - len("ID"))
        espaciosNombre = " "*(nNombre- len("Nombre"))
        espaciosCostos = " "*(nCosto -len("Costo"))
        espaciosDescripcion = " "*(nDescripcion - len("descripcion"))
        encabezado = "\nId%s\t|\tNombre%s\t|\tCosto%s\t|\tDescripcion%s\t\n"%(espaciosId,espaciosNombre,espaciosCostos,espaciosDescripcion)
        renglones= "-" * 200
        contenido = titulo + encabezado

        for i in range(tamanio):
            getId = listaProductos.LinkedListSearchIndex(i)
    
            objProducto = listaProductos.getObjProducto(getId)

            idProducto = str(objProducto.getIdProducto())
            nombre= str(objProducto.getNombreProducto())
            moneda = str(objProducto.getMoneda())
            costo= moneda +" " + str(objProducto.getCosto())
            descripcion= str(objProducto.getDescripcion())
            
            espaciosId = " "*(nId - len(idProducto))
            espaciosNombre = " "*(nNombre- len(nombre))
            espaciosCostos = " "*(nCosto -len(costo))
            espaciosDescripcion = " "*(nDescripcion - len(descripcion))


            contenido += renglones
            contenido += "\n%s%s\t|\t%s%s\t \t%s%s\t \t%s%s\t \n"%(idProducto,espaciosId,nombre,espaciosNombre,costo,espaciosCostos, descripcion,espaciosDescripcion)
            contenido += renglones


        return contenido

    def getMaximosTabla(self, lista):
        tamanioLista =  lista.GetSize()
        # ID mas grande
        nId=2
        nNombre = 6
        nCosto = 0
        nDescripcion = 11
        for i in range(tamanioLista):
            objProducto = lista.getObjProducto(i)
            if(objProducto != -1):

                # Se obtienen los datos del producto i
                idProducto = str(objProducto.getIdProducto())
                nombre= str(objProducto.getNombreProducto())
                moneda = str(objProducto.getMoneda())
                costo= str(objProducto.getCosto())
                descripcion= str(objProducto.getDescripcion())
                if(len(idProducto)> nId):
                    nId = len(idProducto)
                if(len(nombre)>nNombre):
                    nNombre = len(nombre)
                if(len(costo)>nCosto):
                    nCosto = len(costo)
                if(len(descripcion)>nDescripcion):
                    nDescripcion = len(descripcion)
        maximos =[nId,nNombre,nCosto,nDescripcion] 
        return maximos # Se retorna una lista con los tamaños de las cadenas mas grandes




        