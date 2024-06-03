import pyodbc
import os
import random
from tools.generar_fecha import obtener_fecha_random, obtener_fecha_hora_random

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
    
    def count_row_table(self,table):
        try:
            self.cursor.execute(f"select count(*) as cantidad from {table}")
            result = self.cursor.fetchone()
            print(f"La tabla {table} cotiene {result[0]}")
        except:
            print("Hubo un problema al borrar la tabla.")
            
    def count_row_table_return(self,table):
        try:
            self.cursor.execute(f"select count(*) as cantidad from {table}")
            result = self.cursor.fetchone()
            return result[0]
        except:
            return None
    
    # Herramientas en base a datos de las consultas
    def execute_query(self,query):
        try:
            self.cursor.execute(query)
            self.cursor.commit()
            print("Consulta ejecutada con exito.")
        except:
            print("Problema con la consulta.")
        
    # Herramientas personalizadas para tablas expecificas  
    # Consultas referidas a los estados y municipios
    def random_estado_municipio(self):
        try:
            self.cursor.execute("select * from estados;")
            estados = self.cursor.fetchall()
            estados_random = random.choice(estados)
            
            self.cursor.execute(f"select * from municipios where cve_estados = {estados_random[0]};")
            municipios = self.cursor.fetchall()
            municipios_random = random.choice(municipios)
            
            return estados_random[0], municipios_random[0]
        except:
            return None, None
     
    # Consulta referida a los clientes
    def consult_names(self):
        try:
            self.cursor.execute("select * from datos.dbo.nombres;")
            result = self.cursor.fetchall()
            return result
        except:
            print("Problema con la consulta.")
            
    def consult_last_names(self):
        try:
            self.cursor.execute("select * from datos.dbo.apellidos;")
            result = self.cursor.fetchall()
            return result
        except:
            print("Problema con la consulta.")
        
    def insert_name(self,id,cve_municipio,cve_estado,nombre,primer_apellido,segundo_apellido):
        try:
            fecha_nacimiento =  obtener_fecha_random(1932,2023)
            self.cursor.execute(f"""
                        INSERT INTO clientes(cve_clientes, cve_municipios, cve_estados,nombre, paterno, materno, fecha_nacimiento)
                        VALUES ({id}, {cve_municipio}, {cve_estado}, '{nombre}', '{primer_apellido}','{segundo_apellido}', '{fecha_nacimiento}')
                        """)                        
        except pyodbc.Error as e:
            print("Error" + e)
            return False
    
    # Vuelos
    def random_vuelo(self):
        self.cursor.execute("""
                            select v.cve_vuelos, po.cve_paises, pd.cve_paises from vuelos as v
                                inner join aeropuertos as aed on aed.cve_aeropuertos = v.cve_aeropuertos__destino
                                inner join ciudades as cd on cd.cve_ciudades = aed.cve_ciudades
                                inner join paises as pd on pd.cve_paises = cd.cve_paises
                                inner join aeropuertos as aeo on aeo.cve_aeropuertos = v.cve_aeropuertos__origen
                                inner join ciudades as co on co.cve_ciudades = aeo.cve_ciudades
                                inner join paises as po on po.cve_paises = co.cve_paises
                            where po.cve_paises = 25 OR pd.cve_paises = 25;
                            """)
        result = self.cursor.fetchall()
        vuelo_randon = random.choice(result)
        return vuelo_randon[0]
    
    
    # Detalles Vuelos
    def insert_detalles_vuelo(self,id,vuelo_id,capacidad):
        try:
            # Obtener la fecha
            fecha_hora_salida=obtener_fecha_hora_random(2023,2023)
            self.cursor.execute(f"""
                                INSERT INTO detalle_vuelos(cve_detalle_vuelos,cve_vuelos,fecha_hora_salida,capacidad) VALUES ({id},{vuelo_id},'{fecha_hora_salida}',{capacidad})
                                """)
            self.cursor.commit()
        except pyodbc.Error as e:
            print("Error" + e)
            return False
    
    def return_capacidad_detalles(self,detalles_id):
        try:
            self.cursor.execute(f"""
                                select capacidad from detalle_vuelos where cve_detalle_vuelos = {detalles_id}
                                """)
            result = self.cursor.fetchone()
            return result[0]
        except pyodbc.Error as e:
            print("Error" + e)
            return 0
    
    def insert_ocupaciones(self,id,detalles_id,cliente_id):
        try:
            # Checar que cliente no se repita
            self.cursor.execute(f"""
                        INSERT INTO ocupaciones(cve_ocupaciones,cve_detalle_vuelos,cve_clientes) VALUES ({id},{detalles_id},{cliente_id});
                                """)
            self.cursor.commit()
        except pyodbc.Error as e:
            print("Error" + e)
            return False