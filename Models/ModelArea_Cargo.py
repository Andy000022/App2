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

    def ObtenerArea(self, id_area):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT nombre_area, descripcion from areas WHERE id_area = ?"
        cursor.execute(instruccion, (id_area,))
        resultados = cursor.fetchall()
        return resultados

    def ObtenerArea1(self):
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

    def ObtenerCargo(self, id_cargo):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT nombre_cargo from cargo WHERE id_cargo = ?"
        cursor.execute(instruccion, (id_cargo,))
        resultados = cursor.fetchall()
        return resultados
    
    def ObtenerCargo1(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT nombre_cargo from cargo"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

    def verificaId(self, id_area):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from areas WHERE id_area=?"
        cursor.execute(instruccion, (id_area,))
        resultado = cursor.fetchone()
        # Si la consulta SQL devolvió al menos un registro y el primer 
        # elemento de ese registro es mayor que 0, devuelve True. De lo contrario, devuelve False.
        return resultado is not None and resultado[0] > 0
    
    def ModificarArea(self, nombre_area, descripcion, id_area):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = '''UPDATE areas SET nombre_area = ?, descripcion = ? WHERE id_area = ? '''
        cursor.execute(instruccion, (nombre_area, descripcion, id_area))
        con.commit()
        con.close()
    
    def verificaId2(self, id_cargo):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from cargo WHERE id_cargo=?"
        cursor.execute(instruccion, (id_cargo,))
        resultado = cursor.fetchone()
        # Si la consulta SQL devolvió al menos un registro y el primer 
        # elemento de ese registro es mayor que 0, devuelve True. De lo contrario, devuelve False.
        return resultado is not None and resultado[0] > 0
    
    def ModificarCargo(self, nombre_cargo, id_cargo):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = '''UPDATE cargo SET nombre_cargo = ? WHERE id_cargo = ? '''
        cursor.execute(instruccion, (nombre_cargo, id_cargo))
        con.commit()
        con.close()
        
    def EliminarArea(self, id_area):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = f"DELETE FROM areas WHERE id_area = ?"
        cursor.execute(instruccion, (id_area,))
        con.commit()
        con.close()

    def EliminarCargo(self, id_cargo):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = f"DELETE FROM cargo WHERE id_cargo = ?"
        cursor.execute(instruccion, (id_cargo,))
        con.commit()
        con.close()