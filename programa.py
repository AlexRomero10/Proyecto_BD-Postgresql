from funciones import *

db = Conectar_BD("localhost", "postgres", "usuario", "trajes")

while True:
    opcion = MostrarMenu()

    if opcion == 1:
        print("")
        mostrar_tabla(db)
    elif opcion == 2:
        print("")
        mostrar_tabla_sueldo(db)
    elif opcion == 3:
        nombre_cliente = input("Introduce el nombre del cliente: ")
        mostrar_trajes_cliente(db, nombre_cliente)

    elif opcion == 4:
        codigo_trajes = input("Introduce el código del traje: ")
        material = input("Introduce el material del traje: ")
        talla = input("Introduce la talla del traje: ")
        color = input("Introduce el color del traje: ")
        disenador = input("Introduce el nombre del diseñador del traje: ")
        fecha_compra = input("Introduce la fecha de compra: ")
        agregar_traje(db, codigo_trajes, material, talla, color, disenador, fecha_compra)
        actualizar_tabla_trajes(db)
    elif opcion == 5:
        print("")
        eliminar_clientes(db)
    elif opcion == 6:
        codigo_cliente = input("Introduce el codigo del cliente que desea actualizar: ")
        campo = input("Introduce el campo que desea actualizar (direccion, correo_electronico, telefono): ")
        nuevo_valor = input("Introduce el nuevo valor para el campo seleccionado: ")
        actualizar_cliente(db, codigo_cliente, campo, nuevo_valor)
    elif opcion == 7:
        print("FIN DEL PROGRAMA")
        break
    else:
        print("Opcion no valida")