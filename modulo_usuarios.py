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

