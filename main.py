from src.coneccion import db
from tools.barra_progreso import barra_carga
import model.airbus380_cad as table
import random

def create_tables_airbus():
    airbus = db("Shapedb","ajolote","2003yahir","airbus380_acad")
    airbus.connect() # Establecer conexion con airbus.
    # Se revisaran las tablas "ocupaciones", "detalle_vuelos", "clientes", "municipios", "estados"
    # ----------------------------------------------------------------
    print("\n---------------------------------------------\n")
    # ----------------------------------------------------------------
    ocupaciones = airbus.exists_table("ocupaciones")
    if ocupaciones:
        ocupaciones = airbus.drop_table("ocupaciones")
    # ----------------------------------------------------------------
    ocupaciones = airbus.exists_table("detalle_vuelos")
    if ocupaciones:
        ocupaciones = airbus.drop_table("detalle_vuelos")
    # ----------------------------------------------------------------
    ocupaciones = airbus.exists_table("clientes")
    if ocupaciones:
        ocupaciones = airbus.drop_table("clientes")
    # ----------------------------------------------------------------
    ocupaciones = airbus.exists_table("municipios")
    if ocupaciones:
        ocupaciones = airbus.drop_table("municipios")
    # ----------------------------------------------------------------
    ocupaciones = airbus.exists_table("estados")
    if ocupaciones:
        ocupaciones = airbus.drop_table("estados")
    
    cursor =  airbus.return_conection()    
    # Creacion de las tablas
    table.create_estados(cursor)
    table.create_municipios(cursor)
    table.create_clientes(cursor)
    table.create_datalle_vuelos(cursor)
    table.create_ocupaciones(cursor)
    # Cerrar conexion
    airbus.close_conection()
    
def charger_data_estados():
    airbus = db("Shapedb","ajolote","2003yahir","airbus380_acad")
    airbus.connect()
    # Cracion de los registros de estados
    print("\n")
    airbus.count_row_table("datos.dbo.estados")
    airbus.execute_query("insert into estados select * from datos.dbo.estados;")
    print("Estados cargados con exito.")
    # Creacion de los registros de municipios
    print("\n")
    airbus.count_row_table("datos.dbo.municipios")
    airbus.execute_query("insert into municipios select * from datos.dbo.municipios;")
    print("Municipios cargados con exito.")
    airbus.close_conection()
    
def charger_data_clientes():
    airbus = db("Shapedb","ajolote","2003yahir","airbus380_acad")
    airbus.connect()
    
    # Cantidad maxima de datos
    max_clientes =  1000
    count = 1
    
    # Paquete de datos
    result_name = airbus.consult_names()
    result_last_name =  airbus.consult_last_names()    
    
    while True:
        # Escoger un nombre ramdom
        nombre = random.choice(result_name)
        primer_apellido =  random.choice(result_last_name)
        segundo_apellido =  random.choice(result_last_name)
        # Escoger un municipio y estado al azar
        estado_id, municipio_id = airbus.random_estado_municipio()
        
        # Insertar Nombre y checar si existia o no
        airbus.insert_name(count,municipio_id,estado_id,nombre[0],primer_apellido[0],segundo_apellido[0])
        count += 1
        barra_carga(count,max_clientes,35)
        if count >  max_clientes:
            break  
    print(count)
    airbus.close_conection()
    pass


def charger_detalles_vuelo():
    airbus = db("Shapedb","ajolote","2003yahir","airbus380_acad")
    airbus.connect()
    
    max_count = 3000
    count = 0 # ID
    capacidad =  [350,400,450,500] # Capacidad
    vuelo_id =  airbus.random_vuelo()
    
    print(vuelo_id)
    
    while True:
        # Vuelo Random de Mexico
        vuelo_id =  airbus.random_vuelo()
        # Random capacidad
        random_capacidad = random.choice(capacidad)
        # Insetar
        airbus.insert_detalles_vuelo(count,vuelo_id,random_capacidad)    
        count+=1
        barra_carga(count,max_count,35)
        if count >  max_count:
            break
    airbus.close_conection()
    pass

def charger_ocupaciones():
    airbus = db("Shapedb","ajolote","2003yahir","airbus380_acad")
    airbus.connect()
    
    rows_clientes = airbus.count_row_table_return("clientes")
    rows_detalles = airbus.count_row_table_return("detalle_vuelos")
    count_detalles = 1
    count_ocuapciones = 1
    
    while True:
        count_capacidad = 1
        capacidad =  airbus.return_capacidad_detalles(count_detalles)
        capacidad =  capacidad  + 1
        while True:
            id_cliente = random.randrange(1, rows_clientes + 1)
            check_ocupaciones = airbus.insert_ocupaciones(count_ocuapciones,count_detalles,id_cliente)
            if check_ocupaciones:
                count_ocuapciones += 1
                count_capacidad += 1
            if capacidad == count_capacidad:
                break
        
        count_detalles += 1
        barra_carga(count_detalles,300,35)
        if count_detalles == 300:
            break
        pass
    print("Termino")
    airbus.close_conection()
    pass

create_tables_airbus()
print("\n---------------------------------\n")
charger_data_estados()
print("\n---------------------------------\n")
charger_data_clientes()
print("\n---------------------------------\n")
charger_detalles_vuelo()
print("\n---------------------------------\n")
charger_ocupaciones()

input("Presiona Enter para salir...")