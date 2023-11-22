from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje

class ControladorPreguntasSeguridad():
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()

    
    def RegistrarUsuario(self):
        nombre = self.vista.RegistraUsuario_ui.lineEdit_1.text()
        apellido = self.vista.RegistraUsuario_ui.lineEdit_2.text()
        usuario = self.vista.RegistraUsuario_ui.lineEdit_3.text()
        clave = self.vista.RegistraUsuario_ui.lineEdit_4.text()
        confirmar_clave = self.vista.RegistraUsuario_ui.lineEdit_5.text()
        
        pregunta_1 = self.vista.PreguntasSeguridad_ui.lineEdit_3.text()
        pregunta_2 = self.vista.PreguntasSeguridad_ui.lineEdit_1.text()
        pregunta_3 = self.vista.PreguntasSeguridad_ui.lineEdit_4.text()
        pregunta_4 = self.vista.PreguntasSeguridad_ui.lineEdit_2.text()
        
        if len(pregunta_1) == 0 or len(pregunta_2) == 0 or len(pregunta_3) == 0 or len(pregunta_4) == 0:
            self.mensaje.mostrar_mensaje("Error","Hay campos que estan vacios")
        else:
            self.modelo.ModelLogin.registrarUsuario(nombre, apellido, usuario, clave, pregunta_1, pregunta_2, pregunta_3, pregunta_4)
            self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
            self.volver_login()
            self.vista.RegistraUsuario_ui.lineEdit_1.setText("")
            self.vista.RegistraUsuario_ui.lineEdit_2.setText("")
            self.vista.RegistraUsuario_ui.lineEdit_3.setText("")
            self.vista.RegistraUsuario_ui.lineEdit_4.setText("")
            self.vista.RegistraUsuario_ui.lineEdit_5.setText("")

            self.vista.PreguntasSeguridad_ui.lineEdit_3.setText("")
            self.vista.PreguntasSeguridad_ui.lineEdit_1.setText("")
            self.vista.PreguntasSeguridad_ui.lineEdit_4.setText("")
            self.vista.PreguntasSeguridad_ui.lineEdit_2.setText("")

    def volver_login(self):
        self.vista.ocultar_PreguntasSeguridad()
        self.vista.mostrar_login()
