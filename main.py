from datos import *
from modulo_tecnicos import*
from menus import*
RUTA_JSON = "usuarios.json"
datosUsuario = bajar_datos(RUTA_JSON)

def validar_inicio_sesion(datosUsuario):
    id_usuario=input("Ingrese su numero de cedula: ")
    contrasena_usuario=input("Ingrese su contraseña: ")
    
    for usuario in datosUsuario["usuarios"]:
        if usuario["id"]==id_usuario and usuario["contrasena"]==contrasena_usuario:
            print("╭───────────────────────────────────────╮")
            print("│                                       │")
            print("│        ¡Bienvenido a MainTech!        │")
            print("│                                       │")
            print("╰───────────────────────────────────────╯")
            return True
    
    print("╭───────────────────────────────────────╮")
    print("│       ¡Credenciales incorrectas!      │")
    print("│  Intentelo de nuevo o lo invitamos    │")
    print("│  a registrarse en nuestro aplicativo  │")
    print("╰───────────────────────────────────────╯")
    return False

validar_inicio_sesion(datosUsuario)