import json

import json

def agregar_equipo(id_usuario, datosUsuarios):
    datosUsuarios = dict(datosUsuarios)
    for usuario in datosUsuarios["usuarios"]:
        if usuario["id"] == id_usuario:
            equipo = {}
            equipo["marca"] = input("Escriba la marca de su equipo (custom si es una torre): ")
            equipo["serial"] = input("Ingrese el serial de su equipo: ")
            equipo["color"] = input("Ingrese el color de su equipo: ")
            equipo["pago"] = False
            equipo["estado"] = ""
            equipo["servicio"] = ""
            equipo["componentes"] = [
                {
                    "procesador": input("Ingrese el nombre especifico de su procesador: "),
                    "ram": input("Ingrese el tamaño de su ram y su frecuencia(ghz): "),
                    "grafica": input("Ingrese el nombre especifico de su tarjeta grafica: "),
                    "board": input("Ingrese el nombre especifico de su mother board: "),
                    "fuente": input("Ingrese el nombre especifico de su fuente de poder: ")
                }
            ]
            if "equipos" not in usuario:
                usuario["equipos"] = []
            usuario["equipos"].append(equipo)
            print("Equipo Registrado exitosamente!")

            # Guardar los cambios en el archivo JSON
            with open('usuarios.json', 'w', encoding='utf-8') as file:
                json.dump(datosUsuarios, file, ensure_ascii=False, indent=4)
            return datosUsuarios

# Cargar el archivo JSON y llamar a la función como ejemplo
with open('usuarios.json', 'r', encoding='utf-8') as file:
    datosUsuarios = json.load(file)




def usuario_existe(datos, id):
    for usuario in datos["usuarios"]:
        if usuario["id"] == id:
            return True
    return False

def registrar_usuario(datosUsuarios):
    datosUsuarios = dict(datosUsuarios)
    usuario = {}
    usuario["nombre"] = input("Ingrese su nombre: ")
    usuario["numero"] = input("Ingrese su número de celular: ")
    usuario["id"] = input("Ingrese su número de identificación: ")
    usuario["contrasena"] = input("Ingrese su contraseña:  ")
    usuario["direccion"] = input("Ingrese su dirección: ")
    usuario["ciudad"] = input("Ingrese su ciudad: ")
    usuario["rol"] = "Cliente"
    usuario["billetera"] = 0
    usuario["pagos"] = [
        
    ]
    usuario["equipos"] = [

    ]

    
    
    datosUsuarios["usuarios"].append(usuario)
    print("Usuario registrado exitosamente!")
        
    return datosUsuarios

def eliminar_usuario(id_usuario,datos,datosUsuarios,datosServicios):
    datos = dict(datos)
    try:
        documento = id_usuario
        confirmar = int(input("1. para eliminar, 0. para cancelar"))
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    if  confirmar == 1:
        for i in range(len(datos["usuarios"])):
            if datos["usuarios"][i]["id"] == documento:
                datos["usuarios"].pop(i)
                print("Usuario eliminado!")
                return datos
        return datos
    else:
        return datos

def editar_usuario(datos):
    datos = dict(datos)
    buscar_usuario = input("Ingrese el número de documento del usuario: ")

    try:
        for usuario in datos["usuarios"]:
            if usuario["documento"] == buscar_usuario:
                print("Usuario encontrado!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_id = input("Nuevo documento (Enter para dejar sin cambios): ")
                nuevo_ciudad = input("Nueva ciudad(Enter para dejar sin cambios): ")
                nuevo_direccion = input("Nueva Ciudad (Enter para dejar sin cambios): ")
                nuevo_numero = input("Nuevo numero(Enter para dejar sin cambios): ")
                if nuevo_id:
                    usuario["documento"] = nuevo_id
                if nuevo_nombre:
                    usuario["nombre"] = nuevo_nombre
                if nuevo_ciudad:
                    usuario["ciudad"] = nuevo_ciudad
                if nuevo_direccion:
                    usuario["direccion"] = nuevo_direccion
                if nuevo_numero:
                    usuario["numero"] = nuevo_numero
                print("Usuario editado con éxito!")
                break
        else:
            print("Usuario no encontrado!")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    return datos

# def mostrar_usuario(datos):
#     for usuario in datos["usuarios"]:
#         # if usuario["rol"].lower() == "cliente":
#         print(usuario)

# def mostrar_usuario(datos):
#     for usuario in datos["usuarios"]:
#         # Imprime cada usuario como un JSON formateado
#         print(json.dumps(usuario, indent=4))

def mostrar_usuario(datos):
    for usuario in datos["usuarios"]:
        print(f"Nombre: {usuario['nombre']}")
        print(f"Número: {usuario['numero']}")
        print(f"ID: {usuario['id']}")
        print(f"Contraseña: {usuario['contrasena']}")
        print(f"Dirección: {usuario['direccion']}")
        print(f"Ciudad: {usuario['ciudad']}")
        if 'rol' in usuario:
            print(f"Rol: {usuario['rol']}")
        if 'billetera' in usuario:
            print(f"Billetera: {usuario['billetera']}")
        if 'pagos' in usuario:
            print("Pagos:")
            for pago in usuario['pagos']:
                print(f"  Monto: {pago['monto']}, Fecha: {pago['fecha']}")
        if 'equipos' in usuario:
            print("Equipos:")
            for equipo in usuario['equipos']:
                print(f"  Marca: {equipo['marca']}")
                print(f"  Serial: {equipo['serial']}")
                print(f"  Color: {equipo['color']}")
                print(f"  Pago: {equipo['pago']}")
                print(f"  Estado: {equipo['estado']}")
                print(f"  Servicio: {equipo['servicio']}")
                if 'componentes' in equipo:
                    print("  Componentes:")
                    for componente in equipo['componentes']:
                        print(f"    Procesador: {componente['procesador']}")
                        print(f"    RAM: {componente['ram']}")
                        print(f"    Gráfica: {componente['grafica']}")
                        print(f"    Board: {componente['board']}")
                        print(f"    Fuente: {componente['fuente']}")
        print()  # línea en blanco entre cada usuario
