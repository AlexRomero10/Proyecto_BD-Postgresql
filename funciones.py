import psycopg2


def Conectar_BD(host, usuario, password, database):
    try:
        db = psycopg2.connect(
            host=host,
            user=usuario,
            password=password,
            database=database
        )

        return db
    except psycopg2.Error as e:
        print("No puedo conectar a la base de datos:", e)
        return None

def MostrarMenu():
    menu = '''
    1- Muestra una tabla con el material, talla, color, diseñador y el total de clientes que han comprado cada traje.
    2- Muestra una tabla con el nombre y el sueldo del personal de atención cuyo sueldo está entre 10 y 50. Ordena los resultados por sueldo de forma descendente.
    3- Pide por teclado el nombre de un cliente y muestra los trajes que ha comprado junto con su información (material, talla, color, diseñador) y el nombre del personal de atención que lo atendió.  
    4- Pide por teclado los datos de un nuevo traje y su respectivo diseñador. Luego, inserta los datos en la tabla trajes y muestra una tabla actualizada con todos los trajes.
    5- Elimina todos los clientes que han comprado en la fecha 2022-01-01 y muestra el número de filas afectadas.
    6- Actualiza la información de un cliente de la tabla clientes solicitando al usuario el código del cliente y el campo que desea actualizar.
    7- Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Selecciona una opción: "))
            while opcion<1 or opcion>7:
                print("Error, el número de la opción debe estar comprendido entre el 1 y el 7")
                opcion=int(input("\nSelecciona una opción: "))
            return opcion
        except:
            print("Error, la opción debe de ser un número.\n")



#Ejercicio1
def mostrar_tabla(db):
    cursor = db.cursor()
    try:
        sql = "SELECT t.material, t.talla, t.color, t.disenador, COUNT(c.codigo_cliente) as total_clientes FROM trajes t INNER JOIN clientes c  ON t.codigo_trajes = c.codigo_cliente GROUP BY t.material, t.talla, t.color, t.disenador"
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except:
        print("Se ha producido un error al ejecutar la consulta.")
    finally:
        cursor.close()






#Ejercicio2
def mostrar_tabla_sueldo(db):
    try:
        sql = "SELECT Nombre, Sueldo FROM personal_de_atencion WHERE Sueldo BETWEEN 10 AND 50 ORDER BY Sueldo DESC"
        cursor = db.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        for result in registros:
            print(result)
    except:
        print("Se ha producido un error en la consulta.")

#Ejercicio3
def mostrar_trajes_cliente(db, nombre_cliente):
    try:
        cursor = db.cursor()
        sql = """SELECT trajes.codigo_trajes, trajes.material, trajes.talla, trajes.color, trajes.disenador, trajes.fecha_compra, personal_de_atencion.Nombre AS nombre_personal
                 FROM trajes
                 INNER JOIN clientes ON trajes.codigo_trajes = clientes.codigo_cliente
                 INNER JOIN personal_de_atencion ON trajes.DNI_Personal_de_Atencion = personal_de_atencion.DNI_Personal_de_Atencion
                 WHERE clientes.nombre = %s"""
        cursor.execute(sql, (nombre_cliente,))
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            print(f"Trajes comprados por {nombre_cliente}:")
            for traje in resultado:
                    print(f"Material: {traje[0]}\nTalla: {traje[1]}\nColor: {traje[2]}\nDiseñador: {traje[3]}\nAtendido por: {traje[4]}\n")
        else:
            print(f"No se encontraron trajes comprados por {nombre_cliente}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")




#Ejercicio4
def agregar_traje(db, codigo_trajes, material, talla, color, disenador,fecha_compra):
    cursor = db.cursor()
    sql = "INSERT INTO trajes (codigo_trajes, material, talla, color, disenador,fecha_compra) VALUES (%s, %s, %s, %s, %s,%s)"
    val = (codigo_trajes, material, talla, color, disenador,fecha_compra)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "traje insertado.")

def actualizar_tabla_trajes(db):
    cursor = db.cursor()
    sql = "SELECT * FROM trajes"
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("Tabla actualizada de trajes:")
        for result in registros:
            print(result)
    except:
        print("Se ha producido un error al mostrar la tabla.")

#Ejercicio5
def eliminar_clientes(db):
    try:
        cursor = db.cursor()
        sql = "DELETE FROM clientes WHERE codigo_cliente IN (SELECT codigo_cliente FROM trajes WHERE fecha_compra = '2022-01-01')"
        cursor.execute(sql)
        filas_afectadas = cursor.rowcount
        print(f"Se han eliminado {filas_afectadas} clientes que han comprado en la fecha 2022-01-01")
        db.commit()
    except:
        print("Se ha producido un error al eliminar los clientes.")
        db.rollback()


#Ejercicio6
def actualizar_cliente(db, codigo_cliente, campo, nuevo_valor):
    sql = f"UPDATE clientes SET {campo} = %s WHERE codigo_cliente = %s"
    try:
        cursor = db.cursor()
        cursor.execute(sql, (nuevo_valor, codigo_cliente))
        db.commit()
        print("El cliente ha sido actualizado correctamente.")
    except:
        db.rollback()
        print("No se ha podido actualizar el cliente.")