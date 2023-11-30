import sqlite3 as sql
import datetime

class ModelRegistro:
    #recordar que hay que cambiar lo de cedula al id?trabajador y despues se busca el trabajador y se consulta la cedula
    def __init__(self):
        
        pass

    def set_entrada(self, cedula, fecha, hora_entrada):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion_1 ="SELECT id_trabajador FROM Trabajadores WHERE cedula = ?"
        cursor.execute(instruccion_1, (cedula,))
        id_trabajador = cursor.fetchone()[0]
        
        instruccion_2 = f"INSERT INTO asistencia (id_trabajador, fecha, hora_entrada) VALUES (?, ?, ?)"
        cursor.execute(instruccion_2, (id_trabajador, fecha, hora_entrada))
        con.commit()
        con.close()
        
    def actualizar_registro(self, cedula, hora_salida):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion_1 ="SELECT id_trabajador FROM Trabajadores WHERE cedula = ?"
        cursor.execute(instruccion_1, (cedula,))
        resultado = cursor.fetchone()
        id_trabajador = resultado[0]
        
        instruccion_2 = '''UPDATE asistencia SET hora_salida = ? WHERE id_trabajador = ? AND hora_salida IS NULL'''
        cursor.execute(instruccion_2, (hora_salida, id_trabajador))
        con.commit()
        con.close()
    
    def verificar_entrada(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        
        instruccion_1 ="SELECT id_trabajador FROM Trabajadores WHERE cedula = ?"
        cursor.execute(instruccion_1, (cedula,))
        id_trabajador = cursor.fetchone()[0]
        
        instruccion_2 = 'SELECT * FROM asistencia WHERE id_trabajador = ? AND fecha = ?'
        cursor.execute(instruccion_2, (id_trabajador, fecha_actual))
        return cursor.fetchone()
    
    def verificar_salida(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion_1 ="SELECT id_trabajador FROM Trabajadores WHERE cedula = ?"
        cursor.execute(instruccion_1, (cedula,))
        id_trabajador = cursor.fetchone()[0]
        instruccion_2 = 'SELECT * FROM asistencia WHERE id_trabajador = ? AND hora_salida IS NOT NULL'
        cursor.execute(instruccion_2, (id_trabajador,))
        return cursor.fetchone()
    

    def cargar_registros(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from asistencia"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

    def obtener_asistencia(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT Trabajadores.cedula, asistencia.fecha, asistencia.hora_entrada, asistencia.hora_salida FROM asistencia JOIN Trabajadores ON Trabajadores.id_trabajador = asistencia.id_trabajador"
        cursor.execute(instruccion)
        trabajadores = cursor.fetchall()
        return trabajadores
    
    def buscarporfecha(self, fecha_desde, fecha_hasta):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT Trabajadores.cedula, asistencia.fecha, asistencia.hora_entrada, asistencia.hora_salida FROM asistencia JOIN Trabajadores ON Trabajadores.id_trabajador = asistencia.id_trabajador WHERE asistencia.fecha BETWEEN ? AND ?"
        cursor.execute(instruccion, (fecha_desde, fecha_hasta))
        trabajadores = cursor.fetchall()
        return trabajadores

