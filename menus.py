def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("╭───────────────────────────────────────╮")
        print("│                                       │")
        print("│            ¡Opción ingresada!         │")
        print("│                                       │")
        print("╰───────────────────────────────────────╯")
        return opc
    except ValueError:
        print("╭───────────────────────────────────────╮")
        print("│                                       │")
        print("│      Error: ¡Ingrese un número!       │")
        print("│                                       │")
        print("╰───────────────────────────────────────╯")
        return -1

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