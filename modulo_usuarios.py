import json



def usuario_existe(datos, id):
    for usuario in datos["usuarios"]:
        if usuario["id"] == id:
            return True
    return False

def registrar_usuario(datos):
    datos = dict(datos)
    usuario = {}
    usuario["nombre"] = input("Ingrese su nombre: ")
    usuario["numero"] = input("Ingrese su número de celular: ")
    usuario["id"] = input("Ingrese su número de identificación: ")
    usuario["contraseña"] = input("Ingrese su contraseña:  ")
    usuario["direccion"] = input("Ingrese su dirección: ")
    usuario["ciudad"] = input("Ingrese su ciudad: ")
    
    datos["usuarios"].append(usuario)
    print("Usuario registrado exitosamente!")
        
    return datos

def eliminar_usuario(datos):
    datos = dict(datos)
    try:
        documento = input("Ingrese el documento del usuario: ")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("Usuario eliminado!")
            return datos
    
    print("Participante no existe")
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

def mostrar_usuario(datos):
    for usuario in datos["usuarios"]:
        if usuario["rol"].lower() == "tecnico":
            print(usuario)

