from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

from PyQt5.QtWidgets import QFileDialog, QTextEdit
from PyQt5.QtPrintSupport import QPrinter

from PyQt5.QtGui import QTextDocument, QTextCursor
from PyQt5.QtWidgets import QTextEdit


class ControladorRegistro:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        self.mensaje = ControladorMostrar_Mensaje()


    def mostrarAsistencia(self):
        resultado = self.modelo.ModelRegistro.obtener_asistencia()
        
        i = len(resultado)
        self.vista.entrar_ui.tableWidget.setRowCount(i)
        tablerow = 0
        for row in resultado: 
            for j in range(4): # asumiendo que tienes 10 columnas
                item = QtWidgets.QTableWidgetItem(str(row[j]))
                item.setTextAlignment(Qt.AlignCenter) # centra el texto
                self.vista.entrar_ui.tableWidget.setItem(tablerow, j, item)
            tablerow += 1

    def buscarporfecha(self):
        fecha_desde =self.vista.entrar_ui.dateEdit.date().toPyDate()
        fecha_hasta = self.vista.entrar_ui.dateEdit_2.date().toPyDate()
        
        resultado = self.modelo.ModelRegistro.buscarporfecha(fecha_desde, fecha_hasta)
        if resultado:
            self.vista.entrar_ui.tableWidget.setRowCount(0)
            i = len(resultado)
            self.vista.entrar_ui.tableWidget.setRowCount(i)
            tablerow = 0
            for row in resultado: 
                for j in range(4): # asumiendo que tienes 10 columnas
                    item = QtWidgets.QTableWidgetItem(str(row[j]))
                    item.setTextAlignment(Qt.AlignCenter) # centra el texto
                    self.vista.entrar_ui.tableWidget.setItem(tablerow, j, item)
                tablerow += 1
        else:
            self.mensaje.mostrar_mensaje("Error", "No se encontro ningun registro")

    def generar_reporte_asistencia(self):
        formato, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "PDF files (*.pdf);;Excel files (*.xlsx)")
        registros = self.modelo.ModelRegistro.obtener_asistencia()
        
        if registros:
            if formato.endswith('.pdf'):
                self.generar_pdf3(formato, registros)
            elif formato.endswith('.xlsx'):
                self.generar_excel3(formato, registros)
        else:
            self.mensaje.mostrar_mensaje("Error", "No se encontraron registros")

    def generar_pdf3(self, ruta, registros):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(ruta)

        # Crear un nuevo documento
        doc = QTextDocument()

        # Crear una tabla en el documento
        cursor = QTextCursor(doc)
        table = cursor.insertTable(len(registros) + 1, 4)

        # Definir los títulos de las columnas
        titulos = ["Cedula", "Fecha", "Hora_Entrada", "Hora_Salida"]

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



    def generar_excel3(self, ruta, registros):
        # Crear un nuevo libro de trabajo
        libro = Workbook()
        # Obtener la hoja activa
        hoja = libro.active

        # Definir los títulos de las columnas
        titulos = ["Cedula", "Fecha", "Hora_Entrada", "Hora_Salida"]
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

