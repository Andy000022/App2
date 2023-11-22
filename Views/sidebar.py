# Importa los módulos necesarios para tu aplicación
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream


# Importa la interfaz de usuario que creaste con Qt Designer
from Views.siderbar_ui import Ui_MainWindow

# Define tu propia clase MainWindow que hereda de la clase QMainWindow de PyQt5
class MainWindow(QMainWindow):
    
    # El método __init__ se llama automáticamente cuando creas un nuevo objeto de la clase MainWindow
    def __init__(self):
        # Llama al método __init__ de la clase padre QMainWindow
        super(MainWindow, self).__init__()
        
        # Crea un nuevo objeto de la clase Ui_MainWindow que contiene tu interfaz de usuario
        self.ui = Ui_MainWindow()
        # Configura la interfaz de usuario en tu ventana principal
        self.ui.setupUi(self)
        
        # Oculta el widget que solo muestra iconos
        self.ui.icon_only_widget.hide()
        # Muestra la primera página (índice 0) en el widget apilado
        self.ui.stackedWidget.setCurrentIndex(0)
        # Marca el segundo botón de inicio como seleccionado
        self.ui.home_btn_2.setChecked(True)

    # Define las funciones que se llamarán cuando se haga clic en los botones o se cambie el estado de los botones

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)
    
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
    
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
    
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashboard_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashboard_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


# Este bloque de código se ejecuta si este archivo es el script principal que se está ejecutando
if __name__ == "__main__":
    # Crea una nueva aplicación PyQt5
    app = QApplication(sys.argv)
    
    # # Carga el archivo de estilos para tu aplicación
    # style_file = QFile("Resources/style.qss")
    # style_file.open(QFile.ReadOnly | QFile.Text)
    # style_stream = QTextStream(style_file)
    # app.setStyleSheet(style_stream.readAll())
    
    # Crea una nueva ventana principal y la muestra
    window = MainWindow()
    window.show()
    
    # Inicia el bucle de eventos de la aplicación
    sys.exit(app.exec())