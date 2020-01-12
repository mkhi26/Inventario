"""Esta es la clase principal, mediante ella se ejecuta todo el proyecto.

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from nucleo.Gui.GUIPrincipal_ui import Ui_MainWindow
from nucleo.guiVerEditar import ventanaVerEditar
from nucleo.guiAgregarInventario import VentanaAgregar
from nucleo.guiAcercaDe import VentanaAcercaDe
from nucleo.guiDialogo import DialogoConfirmacion
from nucleo.guiDialogoError import DialogoError


from nucleo.LinkedList import *
from nucleo.Producto import *


from nucleo.Gui.recursos_rc import *

class guiPrincipal(QMainWindow):
    def __init__(self,):
        super(guiPrincipal, self).__init__()

        

        # Se inisializa la ventana principal
        self.uiPrincipal = Ui_MainWindow()
        self.uiPrincipal.setupUi(self)

        # Se crean las instancias de las ventanas secundarias

        """
            Se crean instancias de las ventanas secundarias,
            para gestionarlas desde la ventana principal:
            1. self.uiAgregar: Es la instancia de la ventana Agregar a inventario.
            2. self.uiEditar: Es la instancia de la ventana ver y editar
            3. Falta el arbol binario de costos
            4. self.uiAcercaDe: Es la instancia de la ventana "Acerca de"

        """
        self.uiAgregar = VentanaAgregar()  # Instancia de la ventana "Agregar a inventario"
        self.uiEditar = ventanaVerEditar()  # Instancia de la ventana "ver y editar inventario"
        self.uiAcercaDe = VentanaAcercaDe() # Instancia de la ventana " Acerca de"
        self.uiDialogoConfirmacion = DialogoConfirmacion() # Es una instancia del dialogo de confirmacion
        self.uiDialogoConfirmacionDos = DialogoConfirmacion() # Es una segunda instancia de un dialogo de confirmacion
        self.uiDialogoError = DialogoError() # Es una instancia de un dialogo de error

        # Se crean y declaran variables a utilizar
        self.listaPrincipal = self.uiAgregar.getLista() # Obtiene la lista de productos agregados al inventario
        self.actualizarContador() # Llama a la funcion actualizafContador
        self.actualizarTabla()  # Llama a la funcion actualizarTabla

        # Se declaran las siguientes variables centinelas:

        self.agregar= False # Se vuelve True al momento de querer agregar un producto
        self.editar = False #  Se vuelve True al momento de querer Editar un producto
        self.editando = False # Se vuelve True al momento de estar Editando un producto
        self.eliminando = False # Se vuelve True al momento de estar eliminando un producto


        # Eventos:

        # ***Eventos de botones para la pantalla principal:***

        """
            1. Evento Boton agregar a inventario: 
                Al hacer click en este boton se abrira la ventana para agregar elementos al inventario.
            2.Evento Boton Ver y editar inventario:
                Al hacer click en este boton se abrira la ventana para ver y editar los productos en inventario.
            3. Evento Boton Arbol binario de costos:
                Al hacer click en este boton se abrira la ventana para ver el arbol binario de costo
        
            4. Evento Boton Acerca de:
                Al hacer click en este boton se conectara con la ventana " Acerca de"
        """

        self.uiPrincipal.btnAgregarInventario.clicked.connect(self.eventoBtnAgregarInventario) # 1. Evento del boton "Agregar a inventario"
        self.uiPrincipal.btnVerEditar.clicked.connect(self.eventoBtnEditar) # 2. Evento del boton " Ver y editar inventario"
        self.uiPrincipal.btnAcercaDe.clicked.connect(self.eventoBtnAcercaDe) # 4. Evento del boton " Acerca de"


        # ***Evento para los botones de la ventana Agregar***

        """
        Eventos de los botones de la ventana Agregar
        1. Agregar: Al hacer click en agregar se Abrira un dialogo de confirmacion
        2. Cancelar: Al hacer click en  cancelar se abrira un dialogo de confirmacion
            Eventos de el doalogo de confirmacion:
                aceptar: Confirma la accion elegida.
                cancelar: no realiza ninguna accion

        """
        
        self.uiAgregar.uiAgregar.btnAgregar.clicked.connect(self.eventoBtnAgregar) # Se abre un dialogo para confirmar
        self.uiAgregar.uiAgregar.btnCancelar.clicked.connect(self.eventoBtnCancelar) # Se abre un dialogo para confirmar
        self.uiDialogoConfirmacion.uiDialogo.btnConfirmar.clicked.connect(self.eventosDialogo) # Se guarda el objeto Producto
        self.uiDialogoConfirmacion.uiDialogo.btnCancelar.clicked.connect(self.cerrarDialogo) # Se cierra el Dialogo de confirmacion


        # ***Eventos para los botones de la ventana editar o eliminar***
        self.uiEditar.uiVerEditar.btnEditar.clicked.connect(self.mostrarDialogoDos) # Se abre un dialogo para confirmar si el usuario quiere Editar
        self.uiDialogoConfirmacionDos.uiDialogo.btnConfirmar.clicked.connect(self.eventoDialogoDos) # Si el usuario acepta el dialogo al momento de Editar se realizara el proceso de editar.
        self.uiDialogoConfirmacionDos.uiDialogo.btnCancelar.clicked.connect(self.cerrarDialogoDos) # Se cancelara la accion de editar.
        self.uiEditar.uiVerEditar.btnEliminar.clicked.connect(self.eventoEliminar) # Se mostrara un dialogo para que el usuario confirme.
        self.uiDialogoError.uiDialogoError.btnConfirmar.clicked.connect(self.cerrarDialogoError) # Se cierra dialogo de error


    # Funciones para conectar ventanas:

    # Conectar desde pantalla principal

    """
        nombre: eventoBtnAgregarInventario
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion permite conectar la ventana para Agregar productos desde la ventana principal o desde la ventana Editar.
    """

    def eventoBtnAgregarInventario(self):


        if(self.editar):
            self.setDatosFormulario()
            self.editando= True
        else:
            self.agregar = True

        self.uiDialogoConfirmacionDos.close()
        self.uiAgregar.show()
        
        return True

    """
        nombre: eventoBtnEditar
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion permite conectar la ventana para ver y editar productos desde la ventana principal.
    """
    def eventoBtnEditar(self):   
        self.uiEditar.show()
        return True
    """
        nombre: eventoBtnAcercaDe
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion permite conectar la ventana Acerca de desde la ventana principal.
    """

    def eventoBtnAcercaDe(self):
        self.uiAcercaDe.show()
        return True


    """
    def eventoEditarDesdeAgregar(self):
        idProducto = int(self.uiEditar.uiVerEditar.txtEditar.text())
        self.uiAgregar.editarProducto(idProducto)
    """

    # ** Eventos de los DialogBox***

    """
        nombre: eventoDialogo
        parametros: No recibe parametros
        retorno: Retorna True
        Descripcion: Esta funcion realiza determinadas acciones segun sea el caso:
            si editar = True y Editando = False:
                Muestra Dialogo de confirmacion para confirmar si el usuario desea Editar
                si Editando es == True:
                    Edita el objeto directamente.
            Si Agregar == True:
                Se agrega el elemento a la Lista
    """

    def eventosDialogo(self):
        if(self.editar):
            if(not(self.editando)):
                self.uiDialogoConfirmacionDos.show()
                self.editar = False
            else:
                idProducto = int(self.uiEditar.uiVerEditar.txtEditar.text())
                self.uiAgregar.editarProducto(idProducto)
                self.uiAgregar.getLista()
                self.actualizarTabla()
                self.actualizarContador()
                self.editando = False
                self.editar= False
                self.uiDialogoConfirmacion.close()
                self.uiAgregar.close()
                
            return True


        if(self.agregar):
            self.uiAgregar.agregarProductos()
            self.uiDialogoConfirmacion.close()
            self.listaPrincipal = self.uiAgregar.getLista()
            self.actualizarContador()
            self.actualizarTabla()
            self.agregar = False
            return True
        else:
            self.uiDialogoConfirmacion.close()
            self.uiAgregar.close()
            return True

    def eventoDialogoDos(self):
        if(self.eliminando):
            idEliminar = int(self.uiEditar.uiVerEditar.txtEditar.text())
            self.uiAgregar.eliminarObj(idEliminar)
            self.listaPrincipal = self.uiAgregar.getLista()
            self.actualizarContador()
            self.actualizarTabla()
            self.uiDialogoConfirmacionDos.close()
            self.eliminando = False
            self.editando = False
            self.editar = False
            return True
        else:
            self.editar = True
            idEditar = int(self.uiEditar.uiVerEditar.txtEditar.text())
            obj = self.listaPrincipal.getObjProducto(idEditar)
            if(obj == -1):
                self.uiDialogoError.show()
                self.uiDialogoConfirmacionDos.close()
                self.editar = False
                return False
            self.eventoBtnAgregarInventario()
            return True







    # Funciones para Gestionar Los productos 

    def setEditar(self):
        self.editar = True
        self.setDatosFormulario()
        self.eventoBtnAgregar()
        return True


    def eventoBtnAgregar(self):

        self.agregar = True
        self.uiDialogoConfirmacion.show()
        return True


    def eventoBtnCancelar(self):
        self.agregar = False
        self.uiDialogoConfirmacion.show()
        return True

    def cerrarDialogo(self):
        self.uiDialogoConfirmacion.close()
        return True

    def cerrarDialogoDos(self):
        self.uiDialogoConfirmacionDos.close()
        return True



    def setDatosFormulario(self):
        idEditar = int(self.uiEditar.uiVerEditar.txtEditar.text())
        obj = self.listaPrincipal.getObjProducto(idEditar)
        self.uiAgregar.uiAgregar.txtNombre.setText(obj.getNombreProducto())
        self.uiAgregar.uiAgregar.txtCosto.setText(str(obj.getCosto()))
        self.uiAgregar.uiAgregar.txtDescripcion.setText(obj.getDescripcion())
        moneda = obj.getMoneda()
        if(moneda == "HNL"):
            index = 0
        else:
            index = 1
        self.uiAgregar.uiAgregar.cbxMoneda.setCurrentIndex(index)
        return True


    def eventoEliminar(self):
        self.eliminando = True
        self.mostrarDialogoDos()
        return True

    def mostrarDialogoDos(self):
        if(self.eliminando):
            idEliminar = int(self.uiEditar.uiVerEditar.txtEditar.text())
            obj = self.listaPrincipal.getObjProducto(idEliminar)
            self.uiDialogoConfirmacionDos.uiDialogo.lblTexto.setText("\t¿Eliminar?")
            if(obj == -1):
                self.uiDialogoError.show()
                self.eliminando = False
                return False
            self.uiDialogoConfirmacionDos.show()
            return True
            
        self.uiDialogoConfirmacionDos.uiDialogo.lblTexto.setText("\t¿Editar?")
        self.uiDialogoConfirmacionDos.show()
        return True

    def cerrarDialogoError(self):
        self.uiDialogoError.close()
        return True




            
        

    """
        nombre: actualizarContador
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion actualiza el numero de productos agregados en la lista
    """

    def actualizarContador(self):
        n= self.uiAgregar.listaProductos.GetSize()
        self.uiPrincipal.lblContador.setText(str(n))
        return True

    def actualizarTabla(self):

        tabla = self.uiEditar.crearTabla(self.listaPrincipal)
        self.uiEditar.uiVerEditar.txtTabla.setText(tabla)
        return True
    



        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = guiPrincipal()
    main.show()
    sys.exit(app.exec_())