from .ControladorLogin import ControladorLogin
from .ControladorRegistrarUsuario import ControladorRegistrarUsuario
from .ControladorEntradaSalida import ControladorEntradaSalida
from .ControladorRecuperarClave import ControladorRecuperarClave
from .ControladorSiderbar import ControladorSiderbar
# from .ControladorHomeAdmin import ControladorHomeAdmin

class Controlador:

    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.login = ControladorLogin(vista, modelo)
        self.NuevoUsuario = ControladorRegistrarUsuario(vista, modelo)
        self.EntradaSalida = ControladorEntradaSalida(vista, modelo)
        self.RecuperarClave = ControladorRecuperarClave(vista, modelo)
        self.HomeAdmin = ControladorSiderbar(vista, modelo)
        
            # Botones de ventana de inicio de sesion (login)
        self.vista.login_ui.pushButton.clicked.connect(self.login.validar_login)
        self.vista.login_ui.btn_registrar_usuario.clicked.connect(self.VerVentana_RegistrarNuevoUsuario)
        self.vista.login_ui.btn_recuperar_clave.clicked.connect(self.VerVentana_RecuperarClave)
        self.vista.login_ui.btn_asistencia.clicked.connect(self.VerVentana_Asistencia)

    #         # Botones de la ventana registrar un nuevo usurio (contra)
        self.vista.RegistraUsuario_ui.btn_regresar.clicked.connect(self.Volver_al_login2) 
        self.vista.RegistraUsuario_ui.pushButton.clicked.connect(self.NuevoUsuario.SiguienteVentana)


    #         # Botones de la ventana marcar entrada y salidad (usuario)
        self.vista.EntraSali_ui.pushButton.clicked.connect(self.EntradaSalida.regi_entra)
        self.vista.EntraSali_ui.pushButton_2.clicked.connect(self.EntradaSalida.regi_sali)
        self.vista.EntraSali_ui.btn_regresar.clicked.connect(self.Volver_al_login1)
        
    #         # Botones de la ventana recuperar clave
        self.vista.recuperarClave_ui.btn_regresar.clicked.connect(self.Volver_al_login3) 
        self.vista.recuperarClave_ui.pushButton.clicked.connect(self.RecuperarClave.SiguienteVentana)
        
        
        self.vista.entrar_ui.btn_guardar1.clicked.connect(self.HomeAdmin.RegistrarArea)
        self.vista.entrar_ui.btn_guardar2.clicked.connect(self.HomeAdmin.RegistrarCargo)
        self.vista.entrar_ui.btn_registrar.clicked.connect(self.HomeAdmin.RegistrarEmpleado)
        
        self.vista.entrar_ui.products_btn_1.clicked.connect(lambda: (self.HomeAdmin.mostrarAreas(), self.HomeAdmin.mostrarCargos()))
        self.vista.entrar_ui.products_btn_2.clicked.connect(lambda: (self.HomeAdmin.mostrarAreas(), self.HomeAdmin.mostrarCargos()))
        self.vista.entrar_ui.customers_btn_1.clicked.connect(lambda: (self.HomeAdmin.mostrarComboBox_3(), self.HomeAdmin.mostrarComboBox_2()))
        self.vista.entrar_ui.customers_btn_2.clicked.connect(lambda: (self.HomeAdmin.mostrarComboBox_3(), self.HomeAdmin.mostrarComboBox_2()))


    


    # #funcion para ventrar/mostrar la ventrana registrar nuevo usuario, desde la ventana login (login > contra)
    def VerVentana_RegistrarNuevoUsuario(self):
        self.vista.ocultar_login()
        self.vista.mostrar_RegistraUsuario()


    # #funcion para entrar/mostrar la ventrana de recuperar clave, desde la ventana login  (login > recuperar clave)
    def VerVentana_RecuperarClave(self):
        self.vista.ocultar_login()
        self.vista.mostrar_recuperarClave()

    # #funcion para entrar/mostrar la ventrana de asistencia , desde la ventana login  (login > asistencia )
    def VerVentana_Asistencia(self):
        self.vista.ocultar_login()
        self.vista.mostrar_EntraSali()

    def Volver_al_login3(self):
        self.vista.ocultar_recuperarClave()
        self.vista.mostrar_login()
        
    def Volver_al_login2(self):
        self.vista.ocultar_RegistraUsuario()
        self.vista.mostrar_login()

    def Volver_al_login1(self):
        self.vista.ocultar_EntraSali()
        self.vista.mostrar_login()