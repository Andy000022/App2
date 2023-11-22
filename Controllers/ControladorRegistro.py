from PyQt5 import QtWidgets
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


    def Registros(self):
        resultado_registros = self.modelo.ModelRegistro.cargar_registros()
        
        i = len(resultado_registros)##numero de columnas obtenidas
        self.vista.verreg.tableWidget.setRowCount(i)##configurar la cantidad de columnas en la tableWidget
        tablerow = 0 ##primera fila
        for row in resultado_registros: ##aqui se recorren los resultados de la consulta, cada row es un registro diferente
            self.vista.verreg.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[0]))) #se asigna la row[0] (cedula) a la primera columna
            self.vista.verreg.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1])) #se asigna la row[1] (entrada) a la segunda columna
            self.vista.verreg.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2])) #se asigna la row[2] (salida) a la tercera columna
            tablerow=tablerow+1 #se pasa a la siguiente fila de resultados


    def generar_reporte(self):
        formato, _ = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "PDF files (*.pdf);;Excel files (*.xlsx)")
        registros = self.modelo.ModelRegistro.cargar_registros()
        
        if formato.endswith('.pdf'):
            self.generar_pdf(formato, registros)
        elif formato.endswith('.xlsx'):
            self.generar_excel(formato, registros)


    def generar_pdf(self, ruta, registros):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(ruta)

        # Crear un nuevo documento
        doc = QTextDocument()

        # Crear una tabla en el documento
        cursor = QTextCursor(doc)
        table = cursor.insertTable(len(registros) + 1, 3)

        # Definir los títulos de las columnas
        titulos = ["Cedula", "Hora_Entrada", "Hora_Salida"]

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



    def generar_excel(self, ruta, registros):
        # Crear un nuevo libro de trabajo
        libro = Workbook()
        # Obtener la hoja activa
        hoja = libro.active

        # Definir los títulos de las columnas
        titulos = ["Cedula", "Fecha_Entrada", "Fecha_Salida"]
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

