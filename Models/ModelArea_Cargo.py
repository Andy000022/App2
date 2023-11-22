import sqlite3 as sql

class ModelArea_Cargo:
    
    
    def RegistrarArea(self, nombre_area, descripcion):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = f"INSERT INTO areas (nombre_area, descripcion) VALUES (?, ?)"
        cursor.execute(instruccion, (nombre_area, descripcion))
        con.commit()
        con.close()

    def RegistrarCargo(self, nombre_cargo):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = f"INSERT INTO cargo (nombre_cargo) VALUES (?)"
        cursor.execute(instruccion, (nombre_cargo,))
        con.commit()
        con.close()

    def ObtenerAreas(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from areas"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

    def ObtenerArea(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT nombre_area from areas"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

    def ObtenerCargos(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from cargo"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

    def ObtenerCargo(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT nombre_cargo from cargo"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados