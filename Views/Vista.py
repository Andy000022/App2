from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from Views import login_ui, sidebar_ui, RegistrarUsuario_ui, PregSeguridadRegistrar_ui, MarcarEntradaSalida_ui, RecuperarContraseña_ui, RecuperarContraseña_2_ui

class Vista:

    def __init__(self):
        # Cargar archivos .py (ventanas)
        self.login = QtWidgets.QMainWindow()
        self.login_ui = login_ui.Ui_Form()
        self.login_ui.setupUi(self.login)
        
        self.entrar = QMainWindow()
        self.entrar_ui = sidebar_ui.Ui_MainWindow()
        self.entrar_ui.setupUi(self.entrar)
        
        self.RegistraUsuario = QtWidgets.QMainWindow()
        self.RegistraUsuario_ui = RegistrarUsuario_ui.Ui_Form()
        self.RegistraUsuario_ui.setupUi(self.RegistraUsuario)
        
        self.PreguntasSeguridad = QtWidgets.QMainWindow()
        self.PreguntasSeguridad_ui = PregSeguridadRegistrar_ui.Ui_Form()
        self.PreguntasSeguridad_ui.setupUi(self.PreguntasSeguridad)
        
        self.EntraSali = QtWidgets.QMainWindow()
        self.EntraSali_ui = MarcarEntradaSalida_ui.Ui_Form()
        self.EntraSali_ui.setupUi(self.EntraSali)
        
        self.recuperarClave = QtWidgets.QMainWindow()
        self.recuperarClave_ui = RecuperarContraseña_ui.Ui_Form()
        self.recuperarClave_ui.setupUi(self.recuperarClave)
        
        self.recuperarClave_2 = QtWidgets.QMainWindow()
        self.recuperarClave_2_ui = RecuperarContraseña_2_ui.Ui_Form()
        self.recuperarClave_2_ui.setupUi(self.recuperarClave_2) 

    def mostrar_login(self):
        self.login.show()

    def ocultar_login(self):
        self.login.hide()

    def mostrar_entrar(self):
        self.entrar.show()

    def ocultar_entrar(self):
        self.entrar.hide()

    def mostrar_RegistraUsuario(self):
        self.RegistraUsuario.show()

    def ocultar_RegistraUsuario(self):
        self.RegistraUsuario.hide()
        
    def mostrar_recuperarClave(self):
        self.recuperarClave.show()
    
    def ocultar_recuperarClave(self):
        self.recuperarClave.hide()

    def mostrar_recuperarClave_2(self):
        self.recuperarClave_2.show()
    
    def ocultar_recuperarClave_2(self):
        self.recuperarClave_2.hide()


    def mostrar_PreguntasSeguridad(self):
        self.PreguntasSeguridad.show()

    def ocultar_PreguntasSeguridad(self):
        self.PreguntasSeguridad.hide()

    def mostrar_EntraSali(self):
        self.EntraSali.show()

    def ocultar_EntraSali(self):
        self.EntraSali.hide()