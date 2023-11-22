from PyQt5.QtWidgets import QMessageBox

class ControladorMostrar_Mensaje:
    
    def __init__(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)

        
    def mostrar_mensaje(self, titulo, mensaje):
        self.msg.setText(mensaje)
        self.msg.setWindowTitle(titulo)
        self.msg.exec()