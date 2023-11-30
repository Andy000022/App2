from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje

class ControladorRecuperarClave_2:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        
    def ModificarClave(self):
        usuario = self.vista.recuperarClave_ui.lineEdit_1.text()
        clave = self.vista.recuperarClave_2_ui.lineEdit_1.text()
        confirmar_clave = self.vista.recuperarClave_2_ui.lineEdit_2.text()
        
        if len(clave) == 0 or len(confirmar_clave) == 0:
            self.mensaje.mostrar_mensaje("Error", "Las contraseña no coinciden")
        else:
            self.modelo.ModelLogin.ActualizarClave(usuario, clave)
            self.mensaje.mostrar_mensaje("Exito", "Has modificado tu contraseña, ya puedes iniciar sesión")
            self.vista.recuperarClave_ui.lineEdit_1.setText("")
            self.vista.recuperarClave_ui.lineEdit_2.setText("")
            self.vista.recuperarClave_ui.lineEdit_3.setText("")
            self.vista.recuperarClave_ui.lineEdit_4.setText("")
            self.vista.recuperarClave_ui.lineEdit_5.setText("")
            self.vista.recuperarClave_2_ui.lineEdit_1.setText("")
            self.vista.recuperarClave_2_ui.lineEdit_2.setText("")
            
            self.vista.ocultar_recuperarClave_2()
            self.vista.mostrar_login()