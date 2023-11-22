from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje

class ControladorLogin():
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()


    #funcion para validar los datos ingresados en el login
    def validar_login(self):
        usuario = self.vista.login_ui.lineEdit.text() 
        password = self.vista.login_ui.lineEdit_2.text()
        if len(usuario)==0 or len(password)==0:
            self.mensaje.mostrar_mensaje("Error", "Ingrese todos los datos")
        else:
            resultado = self.modelo.ModelLogin.usuario_login(usuario, password)
            if resultado:
            
                result = self.modelo.ModelLogin.registrar_sesiones(usuario)
                if result:
                    self.gui_entrar()
                    self.vista.login_ui.lineEdit.setText("")
                    self.vista.login_ui.lineEdit_2.setText("")
                else:
                    self.mensaje.mostrar_mensaje("Error", "Usuario o contraseña incorrectos")



        #funcion para entrar/mostrar a la ventrana entrar, desde la ventana login (login > entrar)
    def gui_entrar(self):
        self.vista.ocultar_login()
        self.vista.mostrar_entrar()
        
