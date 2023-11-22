from .ControladorRegistro import ControladorRegistro
from .ControladorNuevoEmpleado import ControladorNuevoEmpleado

class ControladorHomeAdmin:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.Registro = ControladorRegistro(vista, modelo)
        self.NuevoEmpleado = ControladorNuevoEmpleado (vista, modelo)
        
        # Botones de la ventana de ver registro (verreg)
        self.vista.verreg.btn_regresar.clicked.connect(self.volver_a_entrada)
        self.vista.verreg.btn_guardar_como.clicked.connect(self.Registro.generar_reporte)
        
        # Botones de la ventana de de registrar un nuevo empleado forma
        self.vista.forma.btn_regresar.clicked.connect(self.NuevoEmpleado.volver_a_entrada)
        self.vista.forma.btn_registrar.clicked.connect(self.NuevoEmpleado.RegistrarEmpleado)

    #funcion para entrar/mostrar la ventana ver registro  (entrar>verreg)
    def ver_registro(self):
        self.vista.ocultar_entrar()
        self.Registro.Registros()
        self.vista.mostrar_verreg()

    #funcion para entrar/mostrar la ventrana registrar nuevo empleado, cuando el cliente de click en la ventana entrada (entra>forma)
    def regis_empleado(self):
        self.vista.ocultar_entrar()
        self.vista.mostrar_forma()

    #funcion para cerrar sesion 
    def cerrar_sesion(self):
        self.vista.ocultar_entrar()
        # Se elimina la información ingresada en los labels
        self.vista.login.label_5.setText("")
        self.vista.mostrar_login()

    #funcion para volver/regresar a la ventrana entrada, desde la ventana ver registro  (verreg > entrar)
    def volver_a_entrada(self):
        self.vista.ocultar_verreg()
        self.vista.mostrar_entrar()

