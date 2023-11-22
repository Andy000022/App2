from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from .ControladorPreguntasSeguridad import ControladorPreguntasSeguridad


class ControladorRegistrarUsuario:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        self.segunda_vista = ControladorPreguntasSeguridad(vista, modelo)

        #         # Botones de la ventana registrar(Preguntas de seguridad)
        
        self.vista.PreguntasSeguridad_ui.pushButton.clicked.connect(self.segunda_vista.RegistrarUsuario)
        self.vista.PreguntasSeguridad_ui.btn_regresar.clicked.connect(self.Volver)

    def SiguienteVentana(self):
        nombre = self.vista.RegistraUsuario_ui.lineEdit_1.text()
        apellido = self.vista.RegistraUsuario_ui.lineEdit_2.text()
        usuario = self.vista.RegistraUsuario_ui.lineEdit_3.text()
        clave = self.vista.RegistraUsuario_ui.lineEdit_4.text()
        confirmar_clave = self.vista.RegistraUsuario_ui.lineEdit_5.text()
        
        if len(nombre) == 0 or len(apellido) == 0 or len(usuario) == 0 or len(clave) == 0 or len(confirmar_clave) == 0:
            self.mensaje.mostrar_mensaje("Error","Hay campos que estan vacios")
        else:
            resultado = self.modelo.ModelLogin.validar_usuario(usuario)
            
            if resultado :
                self.mensaje.mostrar_mensaje("Error", "El usuario ya existe")
            else:
                if clave != confirmar_clave:
                    self.mensaje.mostrar_mensaje("Error", "Las contraseña no coinciden")
                else:
                    self.vista.mostrar_PreguntasSeguridad()
                    self.vista.ocultar_RegistraUsuario()


    def Volver(self):
        self.vista.ocultar_PreguntasSeguridad()
        self.vista.mostrar_RegistraUsuario()
