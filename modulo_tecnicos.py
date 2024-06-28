def registrar_tecnico(datos):
    datos = dict(datos)
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre: ")
    
    while True:
  
        usuario["nombre"] = input("Ingrese el nombre del tecnico: ")
        usuario["numero"] = input("Ingrese el numero de telefono: ")
        usuario["id"] = input("Ingrese el documento: ")
        usuario["direccion"] = input("Ingrese la direccion: ")
        usuario["cuidad"] = input("Ingrese la ciudad: ")
        usuario["rol"] = input("Ingrese el rol: ")

        for documento_en_uso in datos["usuarios"]:
            if documento_en_uso["id"] == usuario["documento"]:
                print("Error: El documento ya está en uso.")
                return datos
        datos["usuarios"].append(usuario)
        print("Usuario registrado con éxito!")
        return datos

def eliminar_tecnico(datos):
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

def editar_tecnico(datos):
    datos = dict(datos)
    buscar_usuario = input("Ingrese el documento del usuario: ")

    try:
        for usuario in datos["usuarios"]:
            if usuario["documento"] == buscar_usuario:
                print("Usuario encontrado!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_id = input("Nuevo documento (Enter para dejar sin cambios): ")
                nuevo_rol = input("Nuevo tipo de cliente (Enter para dejar sin cambios): ")
                nuevo_edad = input("Nueva edad (Enter para dejar sin cambios): ")
                nuevo_ciudad = input("Nueva ciudad(Enter para dejar sin cambios): ")
                nuevo_direccion = input("Nueva Ciudad (Enter para dejar sin cambios): ")
                nuevo_numero = input("Nuevo numero(Enter para dejar sin cambios): ")
                if nuevo_id:
                    usuario["documento"] = nuevo_id
                if nuevo_nombre:
                    usuario["nombre"] = nuevo_nombre
                if nuevo_rol:
                    usuario["rol"] = nuevo_rol
                if nuevo_ciudad:
                    usuario["ciudad"] = nuevo_ciudad
                if nuevo_direccion:
                    usuario["direccion"] = nuevo_direccion
                if nuevo_numero:
                    usuario["numero"] = nuevo_numero
                if nuevo_edad:
                    try:
                        usuario["edad"] = int(nuevo_edad)
                    except ValueError:
                        print("Error: La edad debe ser un número entero.")
                print("Usuario editado con éxito!")
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
