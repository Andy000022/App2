from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import re
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

from PyQt5.QtWidgets import QFileDialog, QTextEdit
from PyQt5.QtPrintSupport import QPrinter

from PyQt5.QtGui import QTextDocument, QTextCursor
from PyQt5.QtWidgets import QTextEdit

class ControladorEmpleados:
    def __init__(self, vista, modelo):
        
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        
    def RegistrarEmpleado(self):
        # Se crea un diccionario con los valores de los campos de entrada 
        campos = {
            'Nombre': self.vista.entrar_ui.lineEdit.text(),
            'Apellido': self.vista.entrar_ui.lineEdit_2.text(),
            'Edad': self.vista.entrar_ui.lineEdit_3.text(),
            'Telefono': self.vista.entrar_ui.lineEdit_4.text(),
            'sexo': str(self.vista.entrar_ui.comboBox.currentText()),
            'Cedula': self.vista.entrar_ui.lineEdit_5.text(),
            'Cargo': str(self.vista.entrar_ui.comboBox_2.currentText()),
            'Area': str(self.vista.entrar_ui.comboBox_3.currentText()),
            'Correo': self.vista.entrar_ui.lineEdit_11.text()
        }

        # Verificar que todos los campos estén llenos
        # any es una función incorporada en Python que devuelve True si al menos un 
        # elemento de un iterable es verdadero.
        # len(valor) == 0 verifica si el campo está vacío.
        # valor in campos.values() itera sobre todos los valores del diccionario campos.
        if any(len(valor) == 0 for valor in campos.values()):
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese todos los datos")
            return

        # Verificar que los campos Nombre y Apellido solo contengan letras
        # all es una función incorporada en Python que devuelve True si todos
        # los elementos de un iterable son verdaderos.
        # campo.isalpha() verifica si todos los caracteres en campo son letras.
        if not all(campo.isalpha() for campo in [campos['Nombre'], campos['Apellido']]):
            self.mensaje.mostrar_mensaje("Error", "Los campos 'Nombre' y 'Apellido' solo deben contener letras")
            return
        
        # Verificar que los campos Edad, Telefono y Cedula solo contengan números
        # campo.isdigit() verifica si todos los caracteres en 'campo' son números.
        if not all(campo.isdigit() for campo in [campos['Edad'], campos['Telefono'], campos['Cedula']]):
            self.mensaje.mostrar_mensaje("Error", "Los campos 'Edad', 'Telefono' y 'Cedula' solo deben contener números")
            return

        # Verificar longitud de teléfono y edad
        if len(campos['Telefono']) != 11:
            self.mensaje.mostrar_mensaje("Error","El numero de telefono debe contener 11 digitos Ejemplo: 04145525412")
            return
        if len(campos['Edad']) != 2:
            self.mensaje.mostrar_mensaje("Error","La edad debe contener 2 digitos")
            return
        
        # Verificar que el campo Correo sea una dirección de correo válida
        # re.match() es una función de la biblioteca re de Python que busca una coincidencia con una expresión regular.
        if not re.match(r"[^@]+@[^@]+\.[^@]+", campos['Correo']):
            self.mensaje.mostrar_mensaje("Error", "El campo 'Correo' debe ser una dirección de correo válida")
            return

        # Verificar si la cédula ya está registrada
        if self.modelo.ModelTrabajadores.verificar_cedula(campos['Cedula']):
            self.mensaje.mostrar_mensaje("Error", "El trabajador ya se encuentra registrado")
            return

        # not in [7, 8] verifica si la longitud de la cédula no es ni 7 ni 8.
        # Si la cédula no contiene 7 u 8 dígitos, mostrar un mensaje de error
        if len(campos['Cedula']) not in [7, 8]:
            self.mensaje.mostrar_mensaje("Error", "La cedula es incorrecta")
            return

        # Registrar al trabajador
        self.modelo.ModelTrabajadores.registrar_trabajador(**campos)
        self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
        self.vista.entrar_ui.tableWidget_2.setRowCount(0)
        self.MostrarEmpleados()

        # Limpiar los campos
        for lineEdit in [self.vista.entrar_ui.lineEdit, self.vista.entrar_ui.lineEdit_2, self.vista.entrar_ui.lineEdit_3, self.vista.entrar_ui.lineEdit_4, self.vista.entrar_ui.lineEdit_5, self.vista.entrar_ui.lineEdit_11]:
            lineEdit.setText("")

    def mostrarComboBox_3(self):
        
        resultados = self.modelo.ModelArea_Cargo.ObtenerArea1()
        self.vista.entrar_ui.comboBox_3.clear()
        for resultado in resultados:
            self.vista.entrar_ui.comboBox_3.addItem(resultado[0])

    def mostrarComboBox_2(self):
        resultados = self.modelo.ModelArea_Cargo.ObtenerCargo1()
        self.vista.entrar_ui.comboBox_2.clear()
        for resultado in resultados:
            self.vista.entrar_ui.comboBox_2.addItem(resultado[0])

    def MostrarEmpleados(self):
        resultado = self.modelo.ModelTrabajadores.obtener_trabajadores()
        
        i = len(resultado)
        self.vista.entrar_ui.tableWidget_2.setRowCount(i)
        tablerow = 0
        for row in resultado: 
            for j in range(10): # asumiendo que tienes 10 columnas
                item = QtWidgets.QTableWidgetItem(str(row[j]))
                item.setTextAlignment(Qt.AlignCenter) # centra el texto
                self.vista.entrar_ui.tableWidget_2.setItem(tablerow, j, item)
            tablerow += 1

    def ModificarEmpleado(self):

        campos = {
            'id_trabajador': self.vista.entrar_ui.lineEdit_6.text(),
            'Nombre': self.vista.entrar_ui.lineEdit.text(),
            'Apellido': self.vista.entrar_ui.lineEdit_2.text(),
            'Edad': self.vista.entrar_ui.lineEdit_3.text(),
            'Telefono': self.vista.entrar_ui.lineEdit_4.text(),
            'sexo': str(self.vista.entrar_ui.comboBox.currentText()),
            'Cedula': self.vista.entrar_ui.lineEdit_5.text(),
            'Cargo': str(self.vista.entrar_ui.comboBox_2.currentText()),
            'Area': str(self.vista.entrar_ui.comboBox_3.currentText()),
            'Correo': self.vista.entrar_ui.lineEdit_11.text()
        }

        # Verificar que todos los campos estén llenos
        # any es una función incorporada en Python que devuelve True si al menos un 
        # elemento de un iterable es verdadero.
        # len(valor) == 0 verifica si el campo está vacío.
        # valor in campos.values() itera sobre todos los valores del diccionario campos.
        if any(len(valor) == 0 for valor in campos.values()):
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese todos los datos")
            return

        # Verificar que los campos Nombre y Apellido solo contengan letras
        # all es una función incorporada en Python que devuelve True si todos
        # los elementos de un iterable son verdaderos.
        # campo.isalpha() verifica si todos los caracteres en campo son letras.
        if not all(campo.isalpha() for campo in [campos['Nombre'], campos['Apellido']]):
            self.mensaje.mostrar_mensaje("Error", "Los campos 'Nombre' y 'Apellido' solo deben contener letras")
            return
        
        # Verificar que los campos Edad, Telefono y Cedula solo contengan números
        # campo.isdigit() verifica si todos los caracteres en 'campo' son números.
        if not all(campo.isdigit() for campo in [campos['Edad'], campos['Telefono'], campos['Cedula']]):
            self.mensaje.mostrar_mensaje("Error", "Los campos 'Edad', 'Telefono' y 'Cedula' solo deben contener números")
            return

        # Verificar longitud de teléfono y edad
        if len(campos['Telefono']) != 11:
            self.mensaje.mostrar_mensaje("Error","El numero de telefono debe contener 11 digitos Ejemplo: 04145525412")
            return
        if len(campos['Edad']) != 2:
            self.mensaje.mostrar_mensaje("Error","La edad debe contener 2 digitos")
            return
        
        # Verificar que el campo Correo sea una dirección de correo válida
        # re.match() es una función de la biblioteca re de Python que busca una coincidencia con una expresión regular.
        if not re.match(r"[^@]+@[^@]+\.[^@]+", campos['Correo']):
            self.mensaje.mostrar_mensaje("Error", "El campo 'Correo' debe ser una dirección de correo válida")
            return


        # not in [7, 8] verifica si la longitud de la cédula no es ni 7 ni 8.
        # Si la cédula no contiene 7 u 8 dígitos, mostrar un mensaje de error
        if len(campos['Cedula']) not in [7, 8]:
            self.mensaje.mostrar_mensaje("Error", "La cedula es incorrecta")
            return

        # Modificar al trabajador
        self.modelo.ModelTrabajadores.modificar_trabajador(**campos)
        self.mensaje.mostrar_mensaje("Éxito!", "Se ha modificado exitosamente!")
        self.vista.entrar_ui.tableWidget_2.setRowCount(0)
        self.MostrarEmpleados()

        # Limpiar los campos
        for lineEdit in [self.vista.entrar_ui.lineEdit, self.vista.entrar_ui.lineEdit_2, self.vista.entrar_ui.lineEdit_3, self.vista.entrar_ui.lineEdit_4, self.vista.entrar_ui.lineEdit_5, self.vista.entrar_ui.lineEdit_11]:
            lineEdit.setText("")

    def EliminarEmpleado(self):
        id_trabajador= self.vista.entrar_ui.lineEdit_6.text()
        if len(id_trabajador)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el codigo para poder eliminar.")
        else:
            resultado = self.modelo.ModelTrabajadores.verificaId(id_trabajador)
            if resultado:
                self.modelo.ModelTrabajadores.EliminarEmpleado(id_trabajador)
                self.mensaje.mostrar_mensaje("Exito","Se elimino correctamente.")
                self.vista.entrar_ui.lineEdit_6.setText("")
                self.vista.entrar_ui.tableWidget_2.setRowCount(0)
                self.MostrarEmpleados()
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun codigo correspondiente al trabajador, verifique que el codigo sea el correcto.")

    def buscarEmpleado(self):
        id_trabajador = self.vista.entrar_ui.lineEdit_6.text()
        
        resultado = self.modelo.ModelTrabajadores.obtener_trabajador3(id_trabajador)
        if resultado:
            self.vista.entrar_ui.tableWidget_2.setRowCount(0)
            i = len(resultado)
            self.vista.entrar_ui.tableWidget_2.setRowCount(i)
            tablerow = 0
            for row in resultado: 
                for j in range(10): # asumiendo que tienes 10 columnas
                    item = QtWidgets.QTableWidgetItem(str(row[j]))
                    item.setTextAlignment(Qt.AlignCenter) # centra el texto
                    self.vista.entrar_ui.tableWidget_2.setItem(tablerow, j, item)
                tablerow += 1
        else:
            self.mensaje.mostrar_mensaje("Error", "No se encontro ningun trabajador")
        

    def buscarEmpleadoporfecha(self):
        fecha_desde =self.vista.entrar_ui.dateEdit_3.date().toPyDate()
        fecha_hasta = self.vista.entrar_ui.dateEdit_4.date().toPyDate()
        
        resultado = self.modelo.ModelTrabajadores.obtener_trabajadoresporfecha(fecha_desde, fecha_hasta)
        if resultado:
            self.vista.entrar_ui.tableWidget_2.setRowCount(0)
            i = len(resultado)
            self.vista.entrar_ui.tableWidget_2.setRowCount(i)
            tablerow = 0
            for row in resultado: 
                for j in range(10): # asumiendo que tienes 10 columnas
                    item = QtWidgets.QTableWidgetItem(str(row[j]))
                    item.setTextAlignment(Qt.AlignCenter) # centra el texto
                    self.vista.entrar_ui.tableWidget_2.setItem(tablerow, j, item)
                tablerow += 1
        else:
            self.mensaje.mostrar_mensaje("Error", "No se encontro ningun registro")
            
    def SeleccionarEmpleados(self):
        id_trabajador = self.vista.entrar_ui.lineEdit_6.text()
        
        if len(id_trabajador)==0:
            self.mensaje.mostrar_mensaje("Error", "El campo de codigo esta vacio")
        else:
            resul = self.modelo.ModelTrabajadores.verificaId(id_trabajador)
            if resul:
                resultado = self.modelo.ModelTrabajadores.obtener_trabajador2(id_trabajador)
                
                self.vista.entrar_ui.lineEdit.setText(resultado[0][0]) #nombre
                self.vista.entrar_ui.lineEdit_2.setText(resultado[0][1])#apellido
                self.vista.entrar_ui.lineEdit_3.setText(str(resultado[0][2]))#edad
                self.vista.entrar_ui.lineEdit_4.setText(str(resultado[0][3]))#telefono
                self.vista.entrar_ui.comboBox.setCurrentText(str(resultado[0][4]))#sexo
                self.vista.entrar_ui.lineEdit_5.setText(str(resultado[0][5]))#cedula
                self.vista.entrar_ui.comboBox_2.setCurrentText(str(resultado[0][6]))#area
                self.vista.entrar_ui.comboBox_3.setCurrentText(str(resultado[0][7]))#cargo
                self.vista.entrar_ui.lineEdit_11.setText(resultado[0][8])#correo
            else:
                self.mensaje.mostrar_mensaje("Error", "No se encontro al trabajador, verifique el codigo.")

    def generar_reporte_empleadosporfecha(self):
        fecha_desde =self.vista.entrar_ui.dateEdit_3.date().toPyDate()
        fecha_hasta = self.vista.entrar_ui.dateEdit_4.date().toPyDate()
        
        formato, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "PDF files (*.pdf);;Excel files (*.xlsx)")
        registros = self.modelo.ModelTrabajadores.obtener_trabajadoresporfecha(fecha_desde, fecha_hasta)
        
        if registros:
            if formato.endswith('.pdf'):
                self.generar_pdf1(formato, registros)
            elif formato.endswith('.xlsx'):
                self.generar_excel1(formato, registros)
        else:
            self.mensaje.mostrar_mensaje("Error", "No se encontraron registros")

    def generar_reporte_empleados(self):
        formato, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "PDF files (*.pdf);;Excel files (*.xlsx)")
        registros = self.modelo.ModelTrabajadores.obtener_trabajadores()
        
        if formato.endswith('.pdf'):
            self.generar_pdf1(formato, registros)
        elif formato.endswith('.xlsx'):
            self.generar_excel1(formato, registros)

    def generar_pdf1(self, ruta, registros):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(ruta)

        # Crear un nuevo documento
        doc = QTextDocument()

        # Crear una tabla en el documento
        cursor = QTextCursor(doc)
        table = cursor.insertTable(len(registros) + 1, 10)

        # Definir los títulos de las columnas
        titulos = ["Codigo", "Nombre", "Apellido", "Edad", "Telefono", "Sexo", "Cedula", "Cargo", "Area", "Correo"]

        # Agregar los títulos a la tabla
        for i, titulo in enumerate(titulos):
            cell = table.cellAt(0, i)
            cellCursor = cell.firstCursorPosition()
            cellCursor.insertText(titulo)

        # Agregar los registros a la tabla
        for i, registro in enumerate(registros, start=1):
            for j, valor in enumerate(registro):
                cell = table.cellAt(i, j)
                cellCursor = cell.firstCursorPosition()
                cellCursor.insertText(str(valor))

        # Imprimir el documento en el archivo PDF
        doc.print_(printer)

    def generar_excel1(self, ruta, registros):
        # Crear un nuevo libro de trabajo
        libro = Workbook()
        # Obtener la hoja activa
        hoja = libro.active

        # Definir los títulos de las columnas
        titulos = ["Codigo", "Nombre", "Apellido", "Edad", "Telefono", "Sexo", "Cedula", "Cargo", "Area", "Correo"]
        # Agregar los títulos a la hoja
        hoja.append(titulos)

        # Aplicar estilo a los títulos
        for cell in hoja["1:1"]:
            # Hacer que el texto de los títulos sea en negrita
            cell.font = Font(bold=True)
            # Centrar el texto en la celda
            cell.alignment = Alignment(horizontal="center")

        # Agregar los registros a la hoja
        for registro in registros:
            hoja.append(registro)

        # Ajustar el ancho de las columnas según el contenido
        for columna in hoja.columns:
            max_length = 0
            columna = [cell for cell in columna]
            for cell in columna:
                try:
                    # Si la longitud del valor de la celda es mayor que max_length,
                    # actualizar max_length con la longitud del valor de la celda
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            # Ajustar el ancho de la columna al valor de max_length + 2 para dejar un poco de espacio extra
            ajuste_ancho = (max_length + 2)
            hoja.column_dimensions[columna[0].column_letter].width = ajuste_ancho

        # Guardar el libro de trabajo en la ruta especificada
        libro.save(ruta)
