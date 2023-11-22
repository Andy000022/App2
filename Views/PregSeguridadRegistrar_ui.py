# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Views\PregSeguridadRegistrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 450)
        Form.setMinimumSize(QtCore.QSize(470, 450))
        Form.setMaximumSize(QtCore.QSize(470, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/logo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-40, -10, 551, 521))
        self.widget.setStyleSheet("QPushButton#pushButton, #btn_regresar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0  #0f2dc2, stop:1 #5c687b);\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover, #btn_regresar:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton:pressed, #btn_regresar:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#c4343c;\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 49, 231, 411))
        self.label.setStyleSheet("border-image: url(:/icon/img/intento2.jpg);\n"
"\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 231, 430))
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 30 ) ;\n"
"border-bottom-left-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(269, 30, 241, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(50, 80, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(50, 140, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 470, 40))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\Views\\../Resources/img/cabecera.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 70, 220, 331))
        self.widget_3.setObjectName("widget_3")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_1.setGeometry(QtCore.QRect(15, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(5, -1, 220, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(15, 260, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(15, 60, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(15, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.btn_regresar = QtWidgets.QPushButton(self.widget)
        self.btn_regresar.setGeometry(QtCore.QRect(270, 80, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.btn_regresar.setFont(font)
        self.btn_regresar.setObjectName("btn_regresar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registrar Nuevo Usuario"))
        self.label_9.setText(_translate("Form", "S.A.M"))
        self.label_10.setText(_translate("Form", "Hola, \n"
"Bienvenido al Sistema \n"
"Automatizado de Monitoreo.\n"
""))
        self.lineEdit_1.setPlaceholderText(_translate("Form", "¿Cuál es tu ciudad de nacimiento?"))
        self.label_8.setText(_translate("Form", "Preguntas de\n"
" Seguridad"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "¿Cuál es tu película favorita?"))
        self.pushButton.setText(_translate("Form", "R e g i s t r a r "))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "¿Cuál es tu color favorito?"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "¿Cuál es tu deporte favorito?"))
        self.btn_regresar.setText(_translate("Form", "<"))
import Resources.resource_rc
