import csv
from nucleo.LinkedList import *
from nucleo.Producto import Producto
class Memoria:
    def __init__(self):
        self.contenido = ""
        self.lista = self.obtenerLinkedList()

    def setMaximo(self, maximo):
        self.maximo = maximo
        return True

    def getMaximo(self):
        tamanio = self.lista.GetSize()
        if(tamanio ==0):
            return 0
        idProducto = self.lista.LinkedListSearchIndex(tamanio-1)
        obj = self.lista.getObjProducto(idProducto)
        maximo = obj.getIdProducto()
        return maximo+1

    def setLista(self, lista):
        self.lista = lista
        return True
        
    def getLista(self):
        lista = self.lista
        return lista

    def getContenidoLinkedList(self):
        lista = self.lista
        tamanio = lista.GetSize()
        contenido = ""
        if(tamanio ==0):
            return "False"
        for i in range(tamanio):
            if(i ==0):
                idProducto = self.lista.LinkedListSearchIndex(i)

                objProducto = lista.getObjProducto(idProducto)
                
                idProducto = str(objProducto.getIdProducto())
                nombre = objProducto.getNombreProducto()
                moneda = objProducto.getMoneda()
                costo = str(objProducto.getCosto())
                descripcion = objProducto.getDescripcion()
                contenido = "%s,%s,%s,%s,%s\n" %(idProducto,nombre,moneda,costo,descripcion)
            else:
                idProducto = self.lista.LinkedListSearchIndex(i)

                objProducto = lista.getObjProducto(idProducto)
                
                idProducto = str(objProducto.getIdProducto())
                nombre = objProducto.getNombreProducto()
                moneda = objProducto.getMoneda()
                costo = str(objProducto.getCosto())
                descripcion = objProducto.getDescripcion()
                contenido += "%s,%s,%s,%s,%s\n" %(idProducto,nombre,moneda,costo,descripcion)
            
        return contenido

    def obtenerLinkedList(self):
        lista = LinkedList()
        contenido = self.getContenidoCsv().split("\n")
        if(len(contenido)>1):
            for i in range(len(contenido)-1):
                columna = contenido[i].split(",")
                idProducto = columna[0]
                nombreProducto = columna[1]
                moneda = columna[2]
                costo = columna[3]
                descripcion = columna[4]

                objProducto = Producto()
                objProducto.setIdProducto(int(columna[0]))
                objProducto.setNombreProducto(columna[1])
                objProducto.setMoneda(columna[2])
                objProducto.setCosto(float(columna[3]))
                objProducto.setDescripcion(columna[4])

                lista.LinkedListAdd(objProducto)
        self.lista = lista
        return lista
            
        
            



    
    def generarCsv(self):
        contenido = self.getContenidoLinkedList()
        if(isinstance(contenido,bool)):
            return False

        f= open('nucleo/Memoria/CSV.csv','w')
        f.write(contenido)
        f.close()
        return True

    def getContenidoCsv(self):
        f = open("nucleo/Memoria/CSV.csv", "r")
        contenido =f.read()
        f.close()
        return contenido

    




