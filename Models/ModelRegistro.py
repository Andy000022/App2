import sqlite3 as sql
import datetime

class ModelRegistro:
    #recordar que hay que cambiar lo de cedula al id?trabajador y despues se busca el trabajador y se consulta la cedula
    def __init__(self):
        
        pass

    def set_entrada(self, cedula, fecha, hora_entrada):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('''INSERT INTO asistencia (cedula, fecha, hora_entrada) VALUES (?, ?, ?)''', (cedula, fecha, hora_entrada))
        con.commit()
        con.close()
        
    def actualizar_registro(self, hora_salida, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('''UPDATE asistencia SET hora_salida = ? WHERE cedula = ? AND hora_salida IS NULL''', (hora_salida, cedula))
        con.commit()
        con.close()
    
    def verificar_entrada(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        cursor.execute('SELECT * FROM asistencia WHERE cedula = ? AND fecha = ?', (cedula, fecha_actual))
        return cursor.fetchone()
    
    def verificar_salida(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        cursor.execute('SELECT * FROM asistencia WHERE cedula = ? AND fecha = ?', (cedula, fecha_actual))
        return cursor.fetchone()
    

    def cargar_registros(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from asistencia"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

