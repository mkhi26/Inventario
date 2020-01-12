"""
    Este es el TDA producto, tiene como atributos ID, nombre, moneda, costo, descripcion.
    Tiene las funciones Set para asignar valores a dichos atributos.


"""

class Producto:
    def __init__(self):
        self.idProducto = 0
        self.nombreProducto = ""
        self.moneda = ""
        self.costo = 0.0
        self.descripcionProducto = ""


    """
        Estos son los metodos set de los atributos de la clase Producto.
        Estos metodos reciben como parametro los valores a asignar a cada atributo de la clase Producto.
        Retornan True en caso de agregar correctamente.
    """

    def setIdProducto(self, id):
        self.idProducto = id
        return True
    def setNombreProducto(self, nombre):
        self.nombreProducto = nombre
        return True

    def setMoneda(self, moneda):
        self.moneda = moneda
        return True

    def setCosto(self, costo):
        self.costo = costo
        return True
    def setDescripcion(self, descripcion):
        self.descripcionProducto = descripcion
        return True

    """
        Estos son los metodos Get de la clase producto:
        retorna los valores de los atributos del objeto.
    """

    def getIdProducto(self):
        id= self.idProducto
        return id
    def getNombreProducto(self):
        nombre = self.nombreProducto
        return nombre

    def getMoneda(self):
        moneda = self.moneda
        return moneda

    def getCosto(self):
        costo = self.costo
        return costo
    def getDescripcion(self):
        descripcion= self.descripcionProducto
        return descripcion

    

