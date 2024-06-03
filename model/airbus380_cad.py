# Función para crear la tabla estados
def create_estados(cursor):
    cursor.execute("""
    CREATE TABLE estados (
        cve_estados INT PRIMARY KEY,
        nombre VARCHAR(50),
        abreviatura VARCHAR(50)
    );
    """)
    cursor.commit()

# Función para crear la tabla municipios
def create_municipios(cursor):
    cursor.execute("""
    CREATE TABLE municipios (
        cve_municipios INT NOT NULL,
        cve_estados INT NOT NULL,
        nombre VARCHAR(50),
        PRIMARY KEY (cve_municipios, cve_estados),
        CONSTRAINT fk_municipio_estado FOREIGN KEY (cve_estados)
            REFERENCES estados (cve_estados)
    );
    """)
    cursor.commit()

# Función para crear la tabla clientes
def create_clientes(cursor):
    cursor.execute("""
    CREATE TABLE clientes (
        cve_clientes INT PRIMARY KEY,
        cve_municipios INT NOT NULL,
        cve_estados INT NOT NULL,
        nombre VARCHAR(50), 
        paterno VARCHAR(50), 
        materno VARCHAR(50), 
        fecha_nacimiento DATETIME,
        CONSTRAINT fk_clientes_municipio FOREIGN KEY (cve_municipios, cve_estados)
            REFERENCES municipios (cve_municipios, cve_estados)
    );
    """)
    cursor.commit()
    
def create_datalle_vuelos(cursor):
    cursor.execute("""
    create table detalle_vuelos(
        cve_detalle_vuelos int primary key,
        cve_vuelos int not null,
        fecha_hora_salida datetime,
        capacidad int,
        constraint fk_detalles_vuelos foreign key (cve_vuelos)
            references vuelos(cve_vuelos)
    );
    """)
    cursor.commit()
    
def create_ocupaciones(cursor):
    cursor.execute("""
    create table ocupaciones(
        cve_ocupaciones int primary key,
        cve_detalle_vuelos int not null,
        cve_clientes int not null,
        constraint fk_detalles_vuelos_ocupaciones foreign key (cve_detalle_vuelos)
            references detalle_vuelos(cve_detalle_vuelos),
        constraint fk_clientes_ocupaciones foreign key (cve_clientes)
            references clientes(cve_clientes)
    );
    """)
    cursor.commit()
    
