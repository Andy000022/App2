import sqlite3 as sql
import datetime

class ModelTrabajadores:
    
    def __init__(self):
        pass

    def verificar_cedula(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('SELECT * FROM trabajadores WHERE cedula = ?', (cedula,))
        return cursor.fetchone()

    def registrar_trabajador(self, Nombre, Apellido, Edad, Telefono, sexo, Cedula, Cargo, Area, Correo):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        
        instruccion_1 ="SELECT id_cargo FROM cargo WHERE nombre_cargo = ?"
        cursor.execute(instruccion_1, (Cargo,))
        id_cargo = cursor.fetchone()[0]
        
        instruccion_2 ="SELECT id_area FROM areas WHERE nombre_area = ?"
        cursor.execute(instruccion_2, (Area,))
        id_area = cursor.fetchone()[0]
        
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        instruccion = f"INSERT INTO Trabajadores (nombre, apellido, edad, telefono, sexo, cedula, id_cargo, id_area, correo, fecha) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(instruccion, (Nombre, Apellido, Edad, Telefono, sexo, Cedula, id_cargo, id_area, Correo, fecha_actual))
        con.commit()
        con.close()

    def obtener_trabajador2(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        
        instruccion = "SELECT nombre, apellido, edad, telefono, sexo, cedula, cargo.nombre_cargo, areas.nombre_area, correo FROM Trabajadores JOIN cargo ON Trabajadores.id_cargo = cargo.id_cargo JOIN areas ON Trabajadores.id_area = areas.id_area WHERE cedula = ?"
        cursor.execute(instruccion, (cedula,))
        resultado = cursor.fetchone()
        
        con.close()
        
        return resultado


def obtener_trabajadores():
    con = sql.connect("base_de_datos.db")
    cursor = con.cursor()
    instruccion = "SELECT id_trabajador, nombre, apellido, edad, telefono, sexo, cedula, cargo.nombre_cargo, areas.nombre_area, correo FROM Trabajadores JOIN cargo ON Trabajadores.id_cargo = cargo.id_cargo JOIN areas ON Trabajadores.id_area = areas.id_area"
    cursor.execute(instruccion)
    trabajadores = cursor.fetchall()
    con.close()
    return trabajadores