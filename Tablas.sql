--Primero accedemos con -> psql -U postgres

--Creación de BD y usuario (Definiendole los privilegios)
CREATE DATABASE Trajes;
CREATE USER alejandro WITH ENCRYPTED PASSWORD 'proyectobd';
GRANT ALL PRIVILEGES ON DATABASE Trajes TO alejandro;
\c trajes

--Creacion Tabla
CREATE TABLE trajes (
    codigo_trajes INT PRIMARY KEY,
    material VARCHAR(30),
    talla VARCHAR(10),
    color VARCHAR(15),
    disenador VARCHAR(20),
    fecha_compra DATE,
    DNI_Personal_de_Atencion VARCHAR(9) REFERENCES personal_de_atencion(DNI_Personal_de_Atencion)
);
INSERT INTO trajes VALUES ('111', 'Algodon', 'L', 'Azul', 'Pablo', '2022-01-01', '49167338P');
INSERT INTO trajes VALUES ('222', 'Poliester', 'XL', 'Rojo', 'Daniel', '2023-01-01', '75894125F');
INSERT INTO trajes VALUES ('333', 'Lino', 'S', 'Negro', 'Hugo', '2022-01-01', '75804020A');
INSERT INTO trajes VALUES ('444', 'Lana', 'M', 'Marrón', 'Mario', '2022-01-01', '49657812G');
INSERT INTO trajes VALUES ('555', 'Algodon', 'L', 'Blanco', 'Jairo', '2024-01-01', '49367412T');
INSERT INTO trajes VALUES ('666', 'Seda', 'M', 'Azul', 'Andres', '2025-01-01', '49357311Z');
INSERT INTO trajes VALUES ('777', 'Seda', 'XL', 'Verde', 'Alex', '2020-01-01', '49347210W');
INSERT INTO trajes VALUES ('888', 'Algodon', 'S', 'Marrón', 'Francisco', '2019-01-01', '49337119C');
INSERT INTO trajes VALUES ('999', 'Lino', 'XS', 'Negro', 'Jose', '2018-01-01', '49327018M');

CREATE TABLE clientes (
    codigo_cliente INT PRIMARY KEY,
    nombre VARCHAR(30),
    direccion VARCHAR(30),
    correo_electronico VARCHAR(25),
    telefono VARCHAR(10)
);
INSERT INTO clientes VALUES (111, 'Antonio', 'Calle Peru', 'juan13@gmail.com', '955862023');
INSERT INTO clientes VALUES (222, 'German', 'Calle Tona', 'alex18@gmail.com', '955863024');
INSERT INTO clientes VALUES (333, 'Julián', 'Calle Goya', 'dani20@gmail.com', '955864025');
INSERT INTO clientes VALUES (444, 'Paula', 'Calle Jaen', 'manu30@gmail.com', '955865026');
INSERT INTO clientes VALUES (555, 'Marta', 'Calle Luna', 'hugo70@gmail.com', '955866027');
INSERT INTO clientes VALUES (666, 'Ana', 'Calle Peru', 'leo13@gmail.com', '955861078');
INSERT INTO clientes VALUES (777, 'Carlos', 'Calle Luna', 'perez4@gmail.com', '955123456');
INSERT INTO clientes VALUES (888, 'Julia', 'Calle Sol', 'maria0@gmail.com', '955789012');
INSERT INTO clientes VALUES (999, 'Rocio', 'Calle Cadiz', 'luis9@gmail.com', '955654321');

CREATE TABLE personal_de_atencion (
    DNI_Personal_de_Atencion VARCHAR(9) PRIMARY KEY,
    Nombre VARCHAR(30),
    Fecha DATE,
    Sueldo DECIMAL(7,2),
    Anosdeexperiencia DATE
);
INSERT INTO personal_de_atencion VALUES ('49167338P', 'Juan', '1999-01-12', 20.5, '2013-01-13');
INSERT INTO personal_de_atencion VALUES ('75894125F', 'Alex', '1999-05-01', 40.5, '2040-01-13');
INSERT INTO personal_de_atencion VALUES ('75804020A', 'Dani', '1990-05-01', 90.5, '2010-01-13');
INSERT INTO personal_de_atencion VALUES ('49657812G', 'Manu', '1980-10-31', 60.5, '2020-01-13');
INSERT INTO personal_de_atencion VALUES ('49367412T', 'Hugo', '2003-01-12', 10.5, '2030-01-13');
INSERT INTO personal_de_atencion VALUES ('49357311Z', 'Leo', '2004-02-13', 30.5, '2050-01-13');
INSERT INTO personal_de_atencion VALUES ('49347210W', 'Perez', '2005-03-14', 50.5, '2060-01-13');
INSERT INTO personal_de_atencion VALUES ('49337119C', 'Maria', '2006-04-15', 70.5, '2070-01-13');
INSERT INTO personal_de_atencion VALUES ('49327018M', 'Luis', '2007-05-16', 80.5, '2080-01-13');