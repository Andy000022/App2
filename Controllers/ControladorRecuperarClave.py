from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from .ControladorRecuperarClave_2 import ControladorRecuperarClave_2
class ControladorRecuperarClave:
    
    def __init__(self, vista, modelo):
        
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje() 
        self.recuperarclave2 = ControladorRecuperarClave_2(vista, modelo)
        
        self.vista.recuperarClave_2_ui.pushButton.clicked.connect(self.recuperarclave2.ModificarClave)
        self.vista.recuperarClave_2_ui.btn_regresar.clicked.connect(self.volver)
        
    def SiguienteVentana(self):
        usuario = self.vista.recuperarClave_ui.lineEdit_1.text()
        pregunta1 = self.vista.recuperarClave_ui.lineEdit_2.text()
        pregunta2 = self.vista.recuperarClave_ui.lineEdit_3.text()
        pregunta3 = self.vista.recuperarClave_ui.lineEdit_4.text()
        pregunta4 = self.vista.recuperarClave_ui.lineEdit_5.text()
        
        if len(usuario)== 0 or len(pregunta1)==0 or len(pregunta2)==0 or len(pregunta3)==0 or len(pregunta4)==0:
            self.mensaje.mostrar_mensaje("Error", "Hay campos que estan vacios.")
        else:
            resultado = self.modelo.ModelLogin.validar_usuario(usuario)
            if resultado==False:
                self.mensaje.mostrar_mensaje("Error", "El usuario no exixte")
            else:
                resultado = self.modelo.ModelLogin.verificarDatos(usuario, pregunta1, pregunta2, pregunta3, pregunta4)
                
                if resultado==False:
                    self.mensaje.mostrar_mensaje("Error", "Las preguntas de seguridad son incorrectas")
                else:
                    self.vista.ocultar_recuperarClave()
                    self.vista.mostrar_recuperarClave_2()

    def volver(self):
        
        self.vista.ocultar_recuperarClave_2()
        self.vista.mostrar_recuperarClave()