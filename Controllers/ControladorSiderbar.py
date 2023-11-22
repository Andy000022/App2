from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets

class ControladorSiderbar:
    
    def __init__(self, vista, modelo):
        
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        
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


    def RegistrarEmpleado(self):
        
        Nombre =self.vista.entrar_ui.lineEdit.text()
        Apellido = self.vista.entrar_ui.lineEdit_2.text()
        Edad = self.vista.entrar_ui.lineEdit_3.text()
        Telefono= self.vista.entrar_ui.lineEdit_4.text()
        sexo = str(self.vista.entrar_ui.comboBox.currentText())
        Cedula = self.vista.entrar_ui.lineEdit_5.text() 
        Cargo = str(self.vista.entrar_ui.comboBox_2.currentText())
        Area = str(self.vista.entrar_ui.comboBox_3.currentText())
        Correo = self.vista.entrar_ui.lineEdit_11.text()
        
        # Se compara que los labels contengan datos,...
        # de lo contrario mostrará un mensaje notificando al usuario
        if len(Nombre)==0 or len(Apellido)==0 or len(Edad)==0 or len(Telefono)==0 or len(Cedula)==0:
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
                self.modelo.ModelTrabajadores.registrar_trabajador(Nombre, Apellido, Edad, Telefono, sexo, Cedula, Cargo, Area, Correo)
                self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente! Con su cedula va a marcar entrada y salida")
                # Cuando se realiza el registro, se eliminan los datos de los labels
                self.vista.entrar_ui.lineEdit.setText("")
                self.vista.entrar_ui.lineEdit_2.setText("")
                self.vista.entrar_ui.lineEdit_3.setText("")
                self.vista.entrar_ui.lineEdit_4.setText("")
                self.vista.entrar_ui.lineEdit_5.setText("")
                self.vista.entrar_ui.lineEdit_11.setText("")
                
                # Se comprueba que la cédula contega 7 dígitos
            elif len (str(Cedula)) ==7:
                self.modelo.ModelTrabajadores.registrar_trabajador(Nombre, Apellido, Edad, Telefono, sexo, Cedula, Cargo, Area, Correo)
                self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente! Con su cedula va a marcar entrada y salida")
                # Cuando se realiza el registro, se eliminan los datos de los labels
                self.vista.entrar_ui.lineEdit.setText("")
                self.vista.entrar_ui.lineEdit_2.setText("")
                self.vista.entrar_ui.lineEdit_3.setText("")
                self.vista.entrar_ui.lineEdit_4.setText("")
                self.vista.entrar_ui.lineEdit_5.setText("")
                self.vista.entrar_ui.lineEdit_11.setText("")
                # Verifica que la cédula sea correcta
            elif len (str(Cedula)) !=8:
                self.mensaje.mostrar_mensaje("Error", "La cedula es incorrecta")

    def RegistrarArea(self):
        
        nombre_area = self.vista.entrar_ui.area.text()
        descripcion = self.vista.entrar_ui.texto.text()
        
        if len(nombre_area) == 0 or len(descripcion)== 0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese todos los datos")
        else:
            self.modelo.ModelArea_Cargo.RegistrarArea(nombre_area, descripcion)
            self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
            self.vista.entrar_ui.area.setText("")
            self.vista.entrar_ui.texto.setText("")


    def RegistrarCargo(self):
        nombre_cargo = self.vista.entrar_ui.cargo.text()
        
        if len(nombre_cargo) == 0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese el nombre del cargo")
        else:
            self.modelo.ModelArea_Cargo.RegistrarCargo(nombre_cargo)
            self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
            self.vista.entrar_ui.cargo.setText("")

    def mostrarAreas(self):
        resultado = self.modelo.ModelArea_Cargo.ObtenerAreas()
        
        i = len(resultado)
        self.vista.entrar_ui.tableWidget_3.setRowCount(i)
        tablerow = 0
        for row in resultado: ##aqui se recorren los resultados de la consulta, cada row es un registro diferente
            self.vista.entrar_ui.tableWidget_3.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0]))) #se asigna la row[0] (cedula) a la primera columna
            self.vista.entrar_ui.tableWidget_3.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1])) #se asigna la row[1] (entrada) a la segunda columna
            self.vista.entrar_ui.tableWidget_3.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2])) #se asigna la row[2] (salida) a la tercera columna
            tablerow=tablerow+1 #se pasa a la siguiente fila de resultados 


    def mostrarCargos(self):
        resultado = self.modelo.ModelArea_Cargo.ObtenerCargos()
        
        i = len(resultado)
        self.vista.entrar_ui.tableWidget_4.setRowCount(i)
        tablerow = 0
        for row in resultado: ##aqui se recorren los resultados de la consulta, cada row es un registro diferente
            self.vista.entrar_ui.tableWidget_4.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0]))) #se asigna la row[0] (cedula) a la primera columna
            self.vista.entrar_ui.tableWidget_4.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1])) #se asigna la row[1] (entrada) a la segunda columna
            tablerow=tablerow+1 #se pasa a la siguiente fila de resultados

    def mostrarComboBox_3(self):
        
        resultados = self.modelo.ModelArea_Cargo.ObtenerArea()
        self.vista.entrar_ui.comboBox_3.clear()
        for resultado in resultados:
            self.vista.entrar_ui.comboBox_3.addItem(resultado[0])

    def mostrarComboBox_2(self):
        resultados = self.modelo.ModelArea_Cargo.ObtenerCargo()
        self.vista.entrar_ui.comboBox_2.clear()
        for resultado in resultados:
            self.vista.entrar_ui.comboBox_2.addItem(resultado[0])

    def MostrarEmpleados(self):
        pass