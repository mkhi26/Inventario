from nucleo.Node import *

"""
Este es el TDA de la lista enlazada.

"""
class LinkedList:
    def __init__(self):
        self.first = None


    """
        Esta funcion retorna el tamaño de la lista enlazada, en caso de que la lista este vacia entonces retornara falso,
         de lo contrario retornara el tamaño.
    """
    def GetSize(self):
        if(not self.first):
            return 0
        count = 0
        current = self.first
        while(current):
            count = count +1
            current = current.next
            
        return count

    """
    Esta funcion agrega nodos a la lista enlazada.
    Recibe como parametro un valor.
    retortna True en caso de que el nodo se agregue correctamente.

    """



    def LinkedListAdd(self, value):
        if(not self.first):
            self.first = Node(value)
            return True
        else:
            current = self.first
            while(current.next):
                current = current.next
            current.next = Node(value)
            return True

    """
        Esta funcion imprime todos los elementos que hay dentro de la lista enlazada.
        No recibe parametros.
        Retorna una cadena de texto.
    """
    def LinkedListPrint(self):
        current = self.first
        printTableText = ""
        while(current):
            printTableText += current.value.nombreProducto
            printTableText += "-->"
            current = current.next
        printTableText += "Null"
        return printTableText 

    """
        Esta funcion retorna un objeto o valor de la lista.
        Recibe como parametros un valor del objeto en la lista.
        Retorna la posicion objeto que se encuentra en la lista,
        caso contrario retorna -1
        

    """
    def LinkedListSearch(self, id):
        count = 0
        if(not self.first):
            return -1
        else:
            current = self.first
            while(current):
                if(id == current.value.idProducto):
                    return count
                current = current.next
                count +=1
            return -1

    def LinkedListSearchIndex(self, index):
        if(not self.first):
            return -1
        else:
            current = self.first
            count = 0
            while(current):
                if(count == index):
                    return current.value.idProducto
                count+=1
                current = current.next

    def getObjProducto(self, idObj):
        count = 0
        if(not self.first):
            return -1
        else:
            current = self.first
            while(current):
                if(idObj == current.value.idProducto):
                    return current.value
                current = current.next
            return -1


    """
        Esta funcion elimina un elemento en especifico de la lista segun su posicion en la lista.
        Recibe como parametro la posicion del elemento a eliminar.
        Retorna el elemento eliminado.
    """
    
    def LinkedListPop(self, index):
        if(not self.first):
            return False
        else:
            if(index == 0):
                current = self.first
                self.first = self.first.next
                return current.value.nombreProducto
            else:
                prevLast = self.first
                last = self.first.next
                count = 1
                while(last):
                    if(count == index):
                        prevLast.next = last.next
                        return last.value.nombreProducto
                    prevLast = last
                    last = prevLast.next
                    count+=1
                return False

                
            

    def LinkedListEditar(self, objEditado):
        idEditado = objEditado.getIdProducto()
        if(not self.first):
            return False
        else:
            actual = self.first
            while(actual):
                if(actual.value.idProducto == idEditado):
                    actual.value = objEditado
                    return True
                actual = actual.next
            return False







            
            
        