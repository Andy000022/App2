from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from .ControladorArea_Cargo import ControladorArea_Cargo
from .ControladorEmpleados import ControladorEmpleados
from .ControladorRegistro import ControladorRegistro
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5 import QtWidgets, QtCore

class ControladorSiderbar:
    
    def __init__(self, vista, modelo):
        
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        self.area_cargo = ControladorArea_Cargo(vista, modelo)
        self.empleados = ControladorEmpleados(vista, modelo)
        self.registro =  ControladorRegistro(vista, modelo)
        
        self.vista.entrar_ui.icon_only_widget.hide()
        #Muestra la primera página (índice 0) en el widget apilado
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(0)
        # Marca el segundo botón de inicio como seleccionado
        self.vista.entrar_ui.home_btn_2.setChecked(True)
        
        # Conecta las señales de los botones a las ranuras
        #self.vista.entrar_ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.vista.entrar_ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.vista.entrar_ui.stackedWidget.currentChanged.connect(self.on_stackedWidget_currentChanged)
        self.vista.entrar_ui.home_btn_1.toggled.connect(self.on_home_btn_1_toggled)
        self.vista.entrar_ui.home_btn_2.toggled.connect(self.on_home_btn_2_toggled)
        #self.vista.entrar_ui.dashboard_btn_1.toggled.connect(self.on_dashboard_btn_1_toggled)
        #self.vista.entrar_ui.dashboard_btn_2.toggled.connect(self.on_dashboard_btn_2_toggled)
        self.vista.entrar_ui.orders_btn_1.toggled.connect(self.on_orders_btn_1_toggled)
        self.vista.entrar_ui.orders_btn_2.toggled.connect(self.on_orders_btn_2_toggled)
        self.vista.entrar_ui.products_btn_1.toggled.connect(self.on_products_btn_1_toggled)
        self.vista.entrar_ui.products_btn_2.toggled.connect(self.on_products_btn_2_toggled)
        
        self.vista.entrar_ui.customers_btn_1.toggled.connect(self.on_customers_btn_1_toggled)
        self.vista.entrar_ui.customers_btn_2.toggled.connect(self.on_customers_btn_2_toggled)
        
        self.vista.entrar_ui.orders_btn_1.clicked.connect(self.registro.mostrarAsistencia)
        self.vista.entrar_ui.orders_btn_2.clicked.connect(self.registro.mostrarAsistencia)
        
        
        self.vista.entrar_ui.btn_buscar.clicked.connect(self.registro.buscarporfecha)
        self.vista.entrar_ui.btn_exportar.clicked.connect(self.registro.generar_reporte_asistencia)
        
        #Botones de area y cargo laboral
        self.vista.entrar_ui.btn_guardar1.clicked.connect(self.area_cargo.RegistrarArea)
        self.vista.entrar_ui.btn_guardar2.clicked.connect(self.area_cargo.RegistrarCargo)
        self.vista.entrar_ui.btn_modificar1.clicked.connect(self.area_cargo.ModificarArea)
        self.vista.entrar_ui.btn_modificar2.clicked.connect(self.area_cargo.ModificarCargo)
        self.vista.entrar_ui.btn_eliminar1.clicked.connect(self.area_cargo.EliminarArea)
        self.vista.entrar_ui.btn_eliminar2.clicked.connect(self.area_cargo.EliminarCargo)
        self.vista.entrar_ui.btn_exportar_1.clicked.connect(self.area_cargo.generar_reporte_area)
        self.vista.entrar_ui.btn_exportar_2.clicked.connect(self.area_cargo.generar_reporte_cargo)
        self.vista.entrar_ui.btn_buscar_1.clicked.connect(self.area_cargo.SeleccionarArea)
        self.vista.entrar_ui.btn_buscar_2.clicked.connect(self.area_cargo.SeleccionarCargo)

        #Botones de Empleados
        self.vista.entrar_ui.btn_registrar.clicked.connect(self.empleados.RegistrarEmpleado)
        self.vista.entrar_ui.btn_selec.clicked.connect(self.empleados.SeleccionarEmpleados)
        self.vista.entrar_ui.btn_modificar_3.clicked.connect(self.empleados.ModificarEmpleado)
        self.vista.entrar_ui.btn_eliminar_3.clicked.connect(self.empleados.EliminarEmpleado)
        self.vista.entrar_ui.btn_buscar_3.clicked.connect(self.empleados.buscarEmpleado)
        self.vista.entrar_ui.btn_exportar_3.clicked.connect(self.empleados.generar_reporte_empleados)
        self.vista.entrar_ui.btn_buscar_4.clicked.connect(self.empleados.buscarEmpleadoporfecha)
        self.vista.entrar_ui.btn_exportar_4.clicked.connect(self.empleados.generar_reporte_empleadosporfecha)
        self.vista.entrar_ui.btn_ayuda_1.clicked.connect(self.ayuda)
        self.vista.entrar_ui.btn_ayuda_2.clicked.connect(self.ayuda)
        
        self.vista.entrar_ui.customers_btn_1.clicked.connect(lambda: (self.empleados.MostrarEmpleados(), self.empleados.mostrarComboBox_3(), self.empleados.mostrarComboBox_2()))
        self.vista.entrar_ui.customers_btn_2.clicked.connect(lambda: (self.empleados.MostrarEmpleados(), self.empleados.mostrarComboBox_3(), self.empleados.mostrarComboBox_2()))
        self.vista.entrar_ui.products_btn_1.clicked.connect(lambda: (self.area_cargo.mostrarAreas(), self.area_cargo.mostrarCargos()))
        self.vista.entrar_ui.products_btn_2.clicked.connect(lambda: (self.area_cargo.mostrarAreas(), self.area_cargo.mostrarCargos()))
        
        current_date = datetime.now()
        qdate = QtCore.QDate(current_date.year, current_date.month, current_date.day)
        self.vista.entrar_ui.dateEdit.setDate(qdate)
        self.vista.entrar_ui.dateEdit_2.setDate(qdate)
        self.vista.entrar_ui.dateEdit_3.setDate(qdate)
        self.vista.entrar_ui.dateEdit_4.setDate(qdate)

    # Define las funciones que se llamarán cuando se haga clic en los botones o se cambie el estado de los botones

    #def on_search_btn_clicked(self):
        #   self.vista.entrar_ui.stackedWidget.setCurrentIndex(5)
        #  search_text = self.vista.entrar_ui.search_input.text().strip()
        # if search_text:
        #    self.vista.entrar_ui.label_9.setText(search_text)
    
    def on_user_btn_clicked(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(6)
    
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.vista.entrar_ui.icon_only_widget.findChildren(QPushButton) \
                    + self.vista.entrar_ui.full_menu_widget.findChildren(QPushButton)
    
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
    
    def on_home_btn_1_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(0)

    #def on_dashboard_btn_1_toggled(self):
    #   self.vista.entrar_ui.stackedWidget.setCurrentIndex(1)

    #def on_dashboard_btn_2_toggled(self):
    #   self.vista.entrar_ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(4)
        

    def on_customers_btn_2_toggled(self):
        self.vista.entrar_ui.stackedWidget.setCurrentIndex(4)

    def ayuda(self):
        self.mensaje.mostrar_mensaje("Ayuda","""Primeros pasos.
Lo primero que hay que hacer al iniciar el sistema es ir al apartado de Áreas y Cargos de trabajo donde se comenzara a registrar las distintas áreas y cargos que tendrán los empleados. En este apartado podremos registrar, modificar, eliminar, seleccionar y exportar. Si quieres seleccionar algún dato de la tabla, ingresaras el código de la fila el cual vayas a seleccionar y presionas el botón seleccionar. Para poder modificar o eliminar se tiene que colocar el código de la fila del dato que queremos modificar o eliminar de la tabla. Si presionas el botón de exportar, podrás guardar en un pdf o xlsx el registro tanto de la tabla áreas de trabajo como la tabla cargo de trabajo. 

Empleados.
Una vez registrado las áreas y cargos de trabajo, podremos comenzar a registrar a los empleados, nos iremos al apartado Empleados donde podremos registrar, modificar, seleccionar, eliminar, buscar o exportar. En este apartado tenemos dos maneras de buscar una por el código de la fila en la tabla y el otro por fecha el cual mostrara todos los registros o datos que se hallan registrados ese día.

Marcar Asistencia.
Si eres algún trabajador y quieres marcar tu entrada o salida laboral solo presiona el botón de marcar asistencia, coloca tu cedula y te registraras.

Ver Asistencia.
Para poder ver las asistencias laborales, iras al apartado de Ver Asistencia donde podrás realizar una búsqueda por fecha  y exportar esos datos.
""")
