def registrar_tecnico(datos):
    datos = dict(datos)
    usuario = {}
    
    
    while True:
  
        usuario["nombre"] = input("Ingrese el nombre del tecnico: ")
        usuario["numero"] = input("Ingrese el numero de telefono: ")
        usuario["id"] = input("Ingrese el documento: ")
        usuario["contrasena"] = input("ingrese la contraseña: ")
        usuario["direccion"] = input("Ingrese la direccion: ")
        usuario["ciudad"] = input("Ingrese la ciudad: ")
        usuario["rol"] = "Tecnico"

        for documento_en_uso in datos["usuarios"]:
            if documento_en_uso["id"] == usuario["id"]:
                print("Error: El documento ya está en uso.")
                return datos
        datos["usuarios"].append(usuario)
        print("Usuario registrado con éxito!")
        return datos

def eliminar_tecnico(datos):
    datos = dict(datos)
    try:
        documento = input("Ingrese el documento del Tecnico: ")
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

        print("Participante no existe")
        return datos
    else:
        return datos

def editar_tecnico(datos):
    datos = dict(datos)
    buscar_usuario = input("Ingrese el documento del Tecnico: ")

    try:
        for usuario in datos["usuarios"]:
            if usuario["id"] == buscar_usuario:
                print("Usuario encontrado!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_id = input("Nuevo documento (Enter para dejar sin cambios): ")
                nuevo_ciudad = input("Nueva ciudad(Enter para dejar sin cambios): ")
                nuevo_direccion = input("Nueva direccion (Enter para dejar sin cambios): ")
                nuevo_numero = input("Nuevo numero(Enter para dejar sin cambios): ")
                if nuevo_id:
                    usuario["id"] = nuevo_id
                if nuevo_nombre:
                    usuario["nombre"] = nuevo_nombre
                if nuevo_ciudad:
                    usuario["ciudad"] = nuevo_ciudad
                if nuevo_direccion:
                    usuario["direccion"] = nuevo_direccion
                if nuevo_numero:
                    usuario["numero"] = nuevo_numero
                
                break
        else:
            print("Usuario no encontrado!")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    return datos

def mostrar_tecnico(datos):
    for usuario in datos["usuarios"]:
        if usuario["rol"].lower() == "tecnico":
            print(usuario)
