from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje


class ControladorNuevoEmpleado:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()


    def RegistrarEmpleado(self):
        Nombre =self.vista.forma.line_nombre.text()
        Apellido = self.vista.forma.line_ap.text()
        Edad = self.vista.forma.line_edad.text()
        box = str(self.vista.forma.comboBox.currentText())
        Telefono= self.vista.forma.line_cel.text()
        Area = str(self.vista.forma.comboBox_2.currentText())
        Cedula = self.vista.forma.line_cedula.text() 
        Correo = self.vista.forma.line_correo.text()
        Cedular = Cedula
                
        # Se compara que los labels contengan datos,...
        # de lo contrario mostrará un mensaje notificando al usuario
        if len(Nombre)==0 or len(Apellido)==0 or len(Correo)==0 or len(Edad)==0 or len(Telefono)==0 or len(Cedula)==0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese todos los datos")
        #Se comprueba que teléfono contenga 11 dígitos
        elif len (str(Telefono)) !=11:
            self.mensaje.mostrar_mensaje("Error","El numero de telefono debe contener 11 digitos")
        #Se comprueba que edad tenga 2 dígitos
        elif len (str(Edad)) !=2:
            self.mensaje.mostrar_mensaje("Error","La edad debe contener 2 digitos")
        elif len (str(Edad)) ==2: 
            resultado= self.modelo.ModelTrabajadores.verificar_cedula(Cedula)
            if resultado:
                self.mensaje.mostrar_mensaje("Error", "El trabajador ya se encuentra registrado")
            # Se comprueba que la cédula contega 8 dígitos
            elif len (str(Cedula)) ==8:
                self.modelo.ModelTrabajadores.registrar_trabajador(Nombre, Apellido, Edad, box, Telefono, Area, Cedula, Correo)
                self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente! Con su cedula va a marcar entrada y salida")
                self.volver_a_entrada()
                # Cuando se realiza el registro, se eliminan los datos de los labels
                self.vista.forma.line_nombre.setText("")
                self.vista.forma.line_ap.setText("")
                self.vista.forma.line_edad.setText("")
                self.vista.forma.line_cel.setText("")
                self.vista.forma.line_cedula.setText("")
                self.vista.forma.line_correo.setText("")
                # Se comprueba que la cédula contega 7 dígitos
            elif len (str(Cedula)) ==7:
                self.modelo.ModelTrabajadores.registrar_trabajador(Nombre, Apellido, Edad, box, Telefono, Area, Cedula, Correo)
                self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente! Con su cedula va a marcar entrada y salida")
                self.volver_a_entrada()
                # Cuando se realiza el registro, se eliminan los datos de los labels
                self.vista.forma.line_nombre.setText("")
                self.vista.forma.line_ap.setText("")
                self.vista.forma.line_edad.setText("")
                self.vista.forma.line_cel.setText("")
                self.vista.forma.line_area.setText("")
                self.vista.forma.line_cedula.setText("")
                self.vista.forma.line_correo.setText("")
                # Verifica que la cédula sea correcta
            elif len (str(Cedula)) !=8:
                self.mensaje.mostrar_mensaje("Error", "La cedula es incorrecta")

    #funcion para volver/regresar a la ventrana entrada, desde la ventana registrar empleado  (forma > entrar)
    def volver_a_entrada(self):
        self.vista.ocultar_forma()
        self.vista.mostrar_entrar()
