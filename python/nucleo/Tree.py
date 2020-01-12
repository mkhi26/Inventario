from nucleo.NodeTree import *
from nucleo.Producto import *
from nucleo.LinkedList import *
import matplotlib.transforms as tr
class Tree:
    def __init__(self):
        self.root = None

    def BSTAdd(self, value):
        return self.BSTAddInner(value, self.root)

    def BSTSearch(self, value):
        return self.BSTSearchInner(value, self.root)

    def BSTAddInner(self, value, current):
        if(not self.root):
            print("Se agrego en la raiz")
            self.root = NodeTree(value)
        else:
            if(current.value.getCosto() == value.getCosto()):
                current= NodeTree(value)
                print("Los nodos son iguales, se remplaza el nodo")
            else:
                if(current.value.getCosto()>value.getCosto()):
                    if(not current.left):
                        print("Se agrego el nodo a la izquierda")
                        current.left= NodeTree(value)
                    else:
                        return self.BSTAddInner(value, current.left)
                else:
                    if(not current.right):
                        print("Se agrego el nodo a la derecha")
                        current.right = NodeTree(value)
                    else:
                        return self.BSTAddInner(value, current.right)
        return False

    def BSTSearchInner(self,value, current):
        if(not self.root):
            return False
        else:
            if(self.root.value.getCosto == value.getCosto()):
                return self.root
            else:
                if(current.value.getCosto() == value.getCosto()):
                    return current
                else:
                    if(current.value.getCosto()> value.getCosto()):
                        return self.BSTSearchInner(value, current.left)
                    else:
                        return self.BSTSearchInner(value, current.right)
        return False

    def preOrder(self, current):
        if( current):
            print(current.value.getCosto())
            self.preOrder(current.right)
            self.preOrder(current.left)

    def postOden(self, current):
        if(current):
            self.postOden(current.right)
            self.postOden(current.left)
            print(current.value)

    def inOrden(self, current):
        if(current):
            self.inOrden(current.right)
            print(current.value)
            self.inOrden(current.left)

    def printTree(self, current, count = 0):
        
        if(not current):
            return
        else:
            self.printTree(current.right, count= count+1)
            for i in range(count):
                print("   ",end="")
            print(current.value.getCosto())
            self.printTree(current.left, count = count +1)

    def linkedlistToTree(self, lista= LinkedList()):
        tamanio = lista.GetSize()
        for i in range(tamanio):
            idProducto = lista.LinkedListSearchIndex(i)
            obj = lista.getObjProducto(idProducto)
            self.BSTAdd(obj)
        return True
    def graficarArbol(self, arbol):
        nombrePadre = self.root.value.getNombreProducto()
        tr.TransformNode(nombrePadre)
        


    


        


    def getRoot(self):
        return self.root


