import pyodbc
import os

class db:
    def __init__(self, server_name, username, password,database):
        self.server_name = server_name
        self.username = username
        self.password =  password
        self.database = database
        pass
    
    def print_details(self):
        print('Severname: ' + self.server_name)
        print('Username: ' + self.username)
        print('Contrasena: ##############')
        print(f'Base de datos: {self.database}')
        pass
    
    def connect(self):
        try:
            cnxn =  pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server_name + ';UID=' + self.username + ';PWD=' + self.password, autocommit=True)
            self.cursor = cnxn.cursor()
            print("Conexion Completa")
            
            self.use_db(self.database)
            
            return True
        except pyodbc.Error as e:
            print(f"Conexion fallida  {e}.")
            return False
        
    def return_conection(self):
        return self.cursor
    
    def close_conection(self):
        try:
            self.cursor.close
        except pyodbc.Error as e:
            print(f"Conexion fallida  {e}.")
            return None

    def use_db(self,database_name):
        # Reviar que exista la base de datos
        self.cursor.execute(f"SELECT database_id FROM sys.databases WHERE Name = '{database_name}'")
        result =  self.cursor.fetchone()
        if not result:
            print(f"La base de datos '{database_name}' no existe.")
        
        try:
            self.cursor.execute(f"use {database_name}")
        except:
            self.cursor.close()
            print("Conexion Fallida.")
        pass
 
    # Herramientas para trabajar con las tablas de una base de datos
    def exists_table(self,table):
        try:
            self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table}'")
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except pyodbc.Error as e:
            print(f"Ocurrio un conflicto con el sistema {e}.")
            
    def drop_table(self,table):
        try:
            self.cursor.execute(f"drop table {table};")
            self.cursor.commit()
            print(f"La tabla {table} existe y se elimino correctamente.")
        except:
            print("Hubo un problema al borrar la tabla.")
    
    def coun_row_table(self,table):
        try:
            self.cursor.execute(f"select count(*) as cantidad from {table}")
            result = self.cursor.fetchone()
            print(f"La tabla {table} cotiene {result[0]}")
        except:
            print("Hubo un problema al borrar la tabla.")
    
    # Herramientas en base a datos de las consultas
    def execute_query(self,query):
        try:
            self.cursor.execute(query)
            self.cursor.commit()
            print("Consulta ejecutada con exito.")
        except:
            print("Problema con la consulta.")