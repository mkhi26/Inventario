from nucleo.LinkedList import *
from nucleo.Producto import *
from nucleo.Tree import *
import matplotlib.pyplot as py
import matplotlib.transforms as tr

pro = Producto()
pro.setNombreProducto("Manzana")
pro.setMoneda("HNL")
pro.setIdProducto(1)
pro.setDescripcion("Esta es la descripcion")
pro.setCosto(100.00)

prod = Producto()
prod.setNombreProducto("Pera")
prod.setMoneda("HNL")
prod.setIdProducto(2)
prod.setDescripcion("Esta es la descripcion")
prod.setCosto(98.00)

l = LinkedList()
l.LinkedListAdd(pro)
l.LinkedListAdd(prod)
print(l.LinkedListPrint())

objEditado = Producto()
objEditado.setNombreProducto("Editado")
objEditado.setMoneda("HNL")
objEditado.setIdProducto(1)
objEditado.setDescripcion("Esta es la descripcion")
objEditado.setCosto(100.00)

l.LinkedListEditar(objEditado)
objEditadoa = Producto()
objEditadoa.setNombreProducto("Dos")
objEditadoa.setMoneda("HNL")
objEditadoa.setIdProducto(2)
objEditadoa.setDescripcion("Esta es la descripcion")
objEditadoa.setCosto(100.00)
l.LinkedListAdd(objEditadoa)

objEditadoab = Producto()
objEditadoab.setNombreProducto("Tres")
objEditadoab.setMoneda("HNL")
objEditadoab.setIdProducto(3)
objEditadoab.setDescripcion("Esta es la descripcion")
objEditadoab.setCosto(102.00)
l.LinkedListAdd(objEditadoab)

print(l.LinkedListPrint())



p=l.LinkedListPrint()


print("Los elementos en la lista son: %s"%(p))

print(" Se elimina el objeto: ", l.LinkedListPop(0))
print(l.LinkedListPrint())

