from src.coneccion import db
import model.airbus380_cad as table

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
    airbus.coun_row_table("datos.dbo.estados")
    print("Cargando los datos a la tabla de Estado de Airbus de la de Datos.")
    airbus.execute_query("insert into estados select * from datos.dbo.estados;")
    print("Estados cargados con exito.")
    # Creacion de los registros de municipios
    airbus.coun_row_table("datos.dbo.municipios")
    print("Cargando los datos a la tabla de Estado de Airbus de la de Datos.")
    airbus.execute_query("insert into municipios select * from datos.dbo.municipios;")
    print("Municipios cargados con exito.")
    
    


create_tables_airbus()
print("\n---------------------------------\n")
charger_data_estados()