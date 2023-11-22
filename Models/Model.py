from .ModelLogin import ModelLogin
from .ModelTrabajadores import ModelTrabajadores
from .ModelRegistro import ModelRegistro
from .ModelArea_Cargo import ModelArea_Cargo
import sqlite3 as sql

class Model:

    def __init__(self):
        
        self.ModelLogin = ModelLogin()
        self.ModelTrabajadores = ModelTrabajadores()
        self.ModelRegistro = ModelRegistro()
        self.ModelArea_Cargo = ModelArea_Cargo()


        self.crear_tablas()

    def ejecutar_consulta(self, instruccion):
        # Conectar a la base de datos
        con = sql.connect('base_de_datos.db', isolation_level=None )
        cursor = con.cursor()
        # Ejecutar la consulta
        cursor.execute(instruccion)
        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()


    def crear_tabla_usuario(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "usuario" (
                            "id_usuario"	INTEGER,
                            "nombre"	TEXT,
                            "apellido"	TEXT,
                            "usuario"	TEXT UNIQUE,
                            "contraseña"	BLOB,
                            "id_pregunta"	INTEGER,                            
                            PRIMARY KEY("id_usuario" AUTOINCREMENT),
                            FOREIGN KEY("id_pregunta") REFERENCES "preguntas"("id_pregunta")
                        );'''
        self.ejecutar_consulta(instruccion)

    def crear_tabla_report_usuario(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "sesion_usuario" (
                            "id" INTEGER,
                            "id_usuario" INTEGER,
                            "fecha" DATE,
                            "hora" TIME,
                            PRIMARY KEY ("id" AUTOINCREMENT),
                            FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario")
        );'''
        self.ejecutar_consulta(instruccion)
        
    def crear_tabla_preguntas(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "preguntas" (
                            "id_pregunta"	INTEGER,
                            "pregunta_1"	TEXT,
                            "pregunta_2"	TEXT,
                            "pregunta_3"	TEXT,
                            "pregunta_4"	TEXT,
                            PRIMARY KEY("id_pregunta" AUTOINCREMENT)
                        );'''
        self.ejecutar_consulta(instruccion)


    def crear_tabla_asistencia(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "asistencia" (
                            "id_asistencia"	INTEGER,
                            "id_trabajador"	INTEGER,
                            "fecha"	DATE,
                            "hora_entrada"	TIME,
                            "hora_salida"	TIME,
                            FOREIGN KEY("id_trabajador") REFERENCES "trabajadores"("id_trabajador"),
                            PRIMARY KEY("id_asistencia" AUTOINCREMENT)
                        );'''
        self.ejecutar_consulta(instruccion)

    def crear_tabla_trabajadores(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "trabajadores" (
                            "id_trabajador"	INTEGER,
                            "nombre"	TEXT,
                            "apellido"	TEXT,
                            "edad"	INTEGER,
                            "telefono"	INTEGER,
                            "sexo"	TEXT,
                            "cedula"	INTEGER UNIQUE,
                            "id_cargo"	INTEGER,
                            "id_area"	INTEGER,
                            "correo"	TEXT,
                            "fecha" DATE,
                            FOREIGN KEY("id_cargo") REFERENCES "cargo"("id_cargo"),
                            FOREIGN KEY("id_area") REFERENCES "areas"("id_area"),
                            PRIMARY KEY("id_trabajador" AUTOINCREMENT)
                        );'''
        self.ejecutar_consulta(instruccion)

    def crear_tabla_cargo(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "cargo" (
                            "id_cargo"	INTEGER,
                            "nombre_cargo"	TEXT,
                            PRIMARY KEY("id_cargo" AUTOINCREMENT)
                        );'''
        self.ejecutar_consulta(instruccion)

    def crear_tabla_area(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "areas" (
                            "id_area"	INTEGER,
                            "nombre_area"	TEXT,
                            "descripcion"	TEXT,
                            PRIMARY KEY("id_area" AUTOINCREMENT)
                        );'''
        self.ejecutar_consulta(instruccion)


    def crear_tablas(self):
        self.crear_tabla_preguntas()
        self.crear_tabla_usuario()
        self.crear_tabla_report_usuario()
        self.crear_tabla_cargo()
        self.crear_tabla_area()
        self.crear_tabla_trabajadores()
        self.crear_tabla_asistencia()
