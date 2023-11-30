from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtWidgets
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

from PyQt5.QtWidgets import QFileDialog, QTextEdit
from PyQt5.QtPrintSupport import QPrinter

from PyQt5.QtGui import QTextDocument, QTextCursor
from PyQt5.QtWidgets import QTextEdit

class ControladorArea_Cargo:
    
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()

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
            self.vista.entrar_ui.tableWidget_3.setRowCount(0)
            self.mostrarAreas()

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

    def ModificarArea(self):
        id_area = self.vista.entrar_ui.lineEdit_12.text()
        nombre_area = self.vista.entrar_ui.area.text()
        descripcion = self.vista.entrar_ui.texto.text()
        
        if len(id_area)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el id del area de trabajo para poder mofificar.")
        else:
            resultado = self.modelo.ModelArea_Cargo.verificaId(id_area)
            if resultado:
                if len(nombre_area)==0 or len(descripcion)==0:
                    self.mensaje.mostrar_mensaje("Error","El campo nombre o descripcion estan vacios.")
                else:
                    self.modelo.ModelArea_Cargo.ModificarArea(nombre_area, descripcion, id_area)
                    self.mensaje.mostrar_mensaje("Exito","Se a Modificado correctamente.")
                    self.vista.entrar_ui.lineEdit_12.setText("")
                    self.vista.entrar_ui.area.setText("")
                    self.vista.entrar_ui.texto.setText("")
                    self.vista.entrar_ui.tableWidget_3.setRowCount(0)
                    self.mostrarAreas()
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun id, verifique que el id sea el correcto.")

    def EliminarArea(self):
        id_area = self.vista.entrar_ui.lineEdit_12.text()
        if len(id_area)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el id del area de trabajo para poder eliminar.")
        else:
            resultado = self.modelo.ModelArea_Cargo.verificaId(id_area)
            if resultado:
                self.modelo.ModelArea_Cargo.EliminarArea(id_area)
                self.mensaje.mostrar_mensaje("Exito","Se elimino correctamente.")
                self.vista.entrar_ui.lineEdit_12.setText("")
                self.vista.entrar_ui.tableWidget_3.setRowCount(0)
                self.mostrarAreas()
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun id, verifique que el id sea el correcto.")

    def SeleccionarArea(self):
        id_area = self.vista.entrar_ui.lineEdit_12.text()
        if len(id_area)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el id del area de trabajo.")
        else:
            resultado = self.modelo.ModelArea_Cargo.verificaId(id_area)
            if resultado:
                resul= self.modelo.ModelArea_Cargo.ObtenerArea(id_area)
                if resul:
                    self.vista.entrar_ui.area.setText(resul[0][0])
                    self.vista.entrar_ui.texto.setText(resul[0][1])
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun id, verifique que el id sea el correcto.")
            

    def RegistrarCargo(self):
        nombre_cargo = self.vista.entrar_ui.cargo.text()
        
        if len(nombre_cargo) == 0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese el nombre del cargo")
        else:
            self.modelo.ModelArea_Cargo.RegistrarCargo(nombre_cargo)
            self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
            self.vista.entrar_ui.cargo.setText("")
            self.vista.entrar_ui.tableWidget_4.setRowCount(0)
            self.mostrarCargos()

    def mostrarCargos(self):
        resultado = self.modelo.ModelArea_Cargo.ObtenerCargos()
        
        i = len(resultado)
        self.vista.entrar_ui.tableWidget_4.setRowCount(i)
        tablerow = 0
        for row in resultado: ##aqui se recorren los resultados de la consulta, cada row es un registro diferente
            self.vista.entrar_ui.tableWidget_4.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0]))) #se asigna la row[0] (cedula) a la primera columna
            self.vista.entrar_ui.tableWidget_4.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1])) #se asigna la row[1] (entrada) a la segunda columna
            tablerow=tablerow+1 #se pasa a la siguiente fila de resultados
    
    def ModificarCargo(self):
        id_cargo = self.vista.entrar_ui.lineEdit_13.text()
        nombre_cargo = self.vista.entrar_ui.cargo.text()
        
        if len(id_cargo)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el id del cargo de trabajo para poder mofificar.")
        else:
            resultado = self.modelo.ModelArea_Cargo.verificaId2(id_cargo)
            if resultado:
                if len(nombre_cargo)==0:
                    self.mensaje.mostrar_mensaje("Error","El campo nombre estan vacios.")
                else:
                    self.modelo.ModelArea_Cargo.ModificarCargo(nombre_cargo, id_cargo)
                    self.mensaje.mostrar_mensaje("Exito","Se a Modificado correctamente.")
                    self.vista.entrar_ui.lineEdit_13.setText("")
                    self.vista.entrar_ui.cargo.setText("")
                    self.vista.entrar_ui.tableWidget_4.setRowCount(0)
                    self.mostrarCargos()
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun id, verifique que el id sea el correcto.")
                
    def EliminarCargo(self):
        id_cargo = self.vista.entrar_ui.lineEdit_13.text()
        if len(id_cargo)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el id del cargo de trabajo para poder eliminar.")
        else:
            resultado = self.modelo.ModelArea_Cargo.verificaId2(id_cargo)
            if resultado:
                self.modelo.ModelArea_Cargo.EliminarCargo(id_cargo)
                self.mensaje.mostrar_mensaje("Exito","Se elimino correctamente.")
                self.vista.entrar_ui.lineEdit_12.setText("")
                self.vista.entrar_ui.tableWidget_4.setRowCount(0)
                self.mostrarCargos()
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun id, verifique que el id sea el correcto.")

    def SeleccionarCargo(self):
        id_cargo = self.vista.entrar_ui.lineEdit_13.text()
        if len(id_cargo)==0:
            self.mensaje.mostrar_mensaje("Error","Tiene que ingresar el id del cargo de trabajo.")
        else:
            resultado = self.modelo.ModelArea_Cargo.verificaId2(id_cargo)
            if resultado:
                resul= self.modelo.ModelArea_Cargo.ObtenerCargo(id_cargo)
                if resul:
                    self.vista.entrar_ui.cargo.setText(resul[0][0])
            else:
                self.mensaje.mostrar_mensaje("Error","No se encontro ningun id, verifique que el id sea el correcto.")
            

    def generar_reporte_area(self):
        # Abre un cuadro de diálogo para guardar el archivo y devuelve el formato seleccionado y el nombre del archivo
        formato, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "PDF files (*.pdf);;Excel files (*.xlsx)")
        registros = self.modelo.ModelArea_Cargo.ObtenerAreas()
        
        # Verifica si el formato seleccionado es PDF
        if formato.endswith('.pdf'):
            # Si es PDF, genera un reporte en formato PDF
            self.generar_pdf1(formato, registros)
        elif formato.endswith('.xlsx'):# Verifica si el formato seleccionado es Excel
            self.generar_excel1(formato, registros)# Si es Excel, genera un reporte en formato Excel


    def generar_pdf1(self, ruta, registros):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(ruta)

        # Crear un nuevo documento
        doc = QTextDocument()

        # Crear una tabla en el documento
        cursor = QTextCursor(doc)
        table = cursor.insertTable(len(registros) + 1, 3)

        # Definir los títulos de las columnas
        titulos = ["Id", "Area", "Descripcion"]

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
        titulos = ["Id", "Area", "Descripcion"]
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


    def generar_reporte_cargo(self):
        formato, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "PDF files (*.pdf);;Excel files (*.xlsx)")
        registros = self.modelo.ModelArea_Cargo.ObtenerCargos()
        
        if formato.endswith('.pdf'):
            self.generar_pdf2(formato, registros)
        elif formato.endswith('.xlsx'):
            self.generar_excel2(formato, registros)


    def generar_pdf2(self, ruta, registros):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(ruta)

        # Crear un nuevo documento
        doc = QTextDocument()

        # Crear una tabla en el documento
        cursor = QTextCursor(doc)
        table = cursor.insertTable(len(registros) + 1, 2)

        # Definir los títulos de las columnas
        titulos = ["Id", "Cargo"]

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



    def generar_excel2(self, ruta, registros):
        # Crear un nuevo libro de trabajo
        libro = Workbook()
        # Obtener la hoja activa
        hoja = libro.active

        # Definir los títulos de las columnas
        titulos = ["Id", "Cargo"]
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

