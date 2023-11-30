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
            self.mensaje.mostrar_mensaje("Error", "Ingrese todos los datos.")
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
        
    def ayuda(self):
        self.mensaje.mostrar_mensaje("Ayuda", """Registrar usuario e Iniciar Sesión
Esta es la vista principal del sistema, lo primero que tenemos que hacer es ir a registras un nuevo usuario presionando el botón +, rellenamos la información necesaria. Luego de haberse registrado iniciaremos sesión, con los datos que registramos, cuando presionemos el botón iniciar sesión se validaran esos datos si son correctos se iniciara al sistema de lo contrario saldrá un mensaje de error.

Olvide mi contraseña.
En caso tal de olvidarse la clave presionaremos olvide mi contraseña, llenaremos los campos con la información solicitada se validad que esos datos concuerden con los que existe en la base de datos si no hay problema recuperaras tu usuario.

Marcar Asistencia.
Si eres algún trabajador y quieres marcar tu entrada o salida laboral solo presiona el botón de marcar asistencia, coloca tu cedula y te registraras.
""")
