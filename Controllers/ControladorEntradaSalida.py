from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
import datetime

class ControladorEntradaSalida:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        

    # funcion para registrar la entrada del empleado en la ventana de registrar entrada y salida
    def regi_entra(self):
        
        cedula = self.vista.EntraSali_ui.lineEdit_1.text()

        if len(cedula)==0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese la cedula")
        else:
            resultado = self.modelo.ModelTrabajadores.verificar_cedula(cedula)
            if resultado:
                resultado = self.modelo.ModelRegistro.verificar_entrada(cedula)
                if resultado is None:
                    ahora = datetime.now()
                    fecha = ahora.strftime('%Y-%m-%d')
                    hora_entrada = ahora.strftime('%H:%M:%S')
                    entrada = self.modelo.ModelRegistro.set_entrada(cedula, fecha,  hora_entrada)
                    self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
                    self.vista.usuario.line_entrada.setText("")
                else:
                    self.mensaje.mostrar_mensaje("Error", "El trabajador ya marco la Entrada")
                    self.vista.usuario.line_entrada.setText("")
            else:
                self.mensaje.mostrar_mensaje("Error", "El trabajador no se encuentra registrado")
                self.vista.usuario.line_entrada.setText("")
    
    # funcion para registrar la salida del empleado en la ventana de registrar entrada y salida
    def regi_sali(self):
        cedula = self.vista.EntraSali_ui.lineEdit_2.text()

        if len(cedula)==0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese la cedula")
        else:
            resultado = self.modelo.ModelTrabajadores.verificar_cedula(cedula)

            if resultado:
                resultado = self.modelo.ModelRegistro.verificar_salida(cedula)
                if resultado is None:
                    ahora = datetime.now()
                    fecha = ahora.strftime('%Y-%m-%d')
                    hora_salida = ahora.strftime('%H:%M:%S')
                    salida = self.modelo.ModelRegistro.actualizar_registro(fecha, hora_salida, cedula)
                    self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
                    self.vista.usuario.line_salida.setText("")                
                else:
                    self.mensaje.mostrar_mensaje("Error", "El trabajador ya marco la Salida")
                    self.vista.usuario.line_salida.setText("")
            else:
                self.mensaje.mostrar_mensaje("Error", "El trabajador no se encuentra registrado")
                self.vista.usuario.line_salida.setText("")
