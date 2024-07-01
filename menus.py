from datos import *
import json
# from main import datosUsuario
# from main import datosServicios
RUTA_USUARIOS = "usuarios.json"
RUTA_SERVICIOS = "servicios.json"
RUTA_HISTORIAL_VENTAS = "historial_ventas.json"

def menu_principal(datos_usuario):
    print("╭───────────────────────────────────────╮")
    print("│                                       │")
    print("│        ¡Bienvenido a MainTech!        │")
    print("│                                       │")
    print("╰───────────────────────────────────────╯")
    opciones = ["1.Iniciar sesion","2.Registrarse","3.Salir...\n\n"]
    longitud_total = 45
    for i in range(len(opciones)):
        print(opciones[i].center(longitud_total))
    return datos_usuario

def ejecutable(datos_usuario):
    opc = 0
    while True:
        menu_principal(datos_usuario)
        try:
            opc = int(input("-"))
            if opc not in [1,2,3]:
                raise ValueError("Opcion invalida")
        except Exception as error:
            error = "opcion no valida"
            print(error)
        else:
            if opc == 1:
                datosUsuarios = bajar_datos(RUTA_USUARIOS)
                # datosServicios = bajar_datos(RUTA_SERVICIOS)
                datosUsuarios = opcion_sesion(datosUsuarios)

def opcion_sesion(datosUsuarios):
    while True:
        try:
            usuario_id = input("Ingrese su id o cedula: ")
            usuario_clave = input("ingrese su contraseña: ")
            usuario_encontrado = False
            for usuario_info in datosUsuarios["usuarios"]:
                if  usuario_info["id"] == usuario_id and usuario_info["contrasena"] == usuario_clave:
                        usuario_encontrado: True
                        if usuario_info["rol"] == "Cliente":
                            
                            menu_clientes(datosUsuarios)
                        elif usuario_info["rol"] == "Tecnico":
                            menu_tecnicos(datosUsuarios)

            if not usuario_encontrado:
                print("la clave o el usuario son incorrectos")
                continue

        except Exception as error:
            error = "opcion no valida"
            print(error)
        return datosUsuarios

def menu_clientes(datosUsuarios,datosServicios):
    print("hola")
    
def menu_tecnicos(datosUsuarios,datosServicios):
    print("hola")

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


def mostrar_menu_usuarios():
    print("╔═══════════════════════════════════════╗")
    print("║          ¡Bienvenido a MainTech!      ║")
    print("╠═══════════════════════════════════════╣")
    print("║  Seleccione una opción del menú:      ║")
    print("║                                       ║")
    print("║  1. Registrar Cliente                 ║")
    print("║     ➤ Añadir un nuevo cliente al sistema")
    print("║                                       ║")
    print("║  2. Registrar Servicio                ║")
    print("║     ➤ Registrar un nuevo servicio para un cliente")
    print("║                                       ║")
    print("║  3. Registrar Compra                  ║")
    print("║     ➤ Registrar una nueva compra realizada por un cliente")
    print("║                                       ║")
    print("║  4. Mostrar Historial de Ventas       ║")
    print("║     ➤ Ver el historial completo de ventas")
    print("║                                       ║")
    print("║  5. Salir                             ║")
    print("║     ➤ Cerrar el programa             ║")
    print("╠═══════════════════════════════════════╣")




def mostrar_menu_principal():
    print("╔═══════════════════════════════════════╗")
    print("║          ¡Bienvenido a MainTech!      ║")
    print("╠═══════════════════════════════════════╣")
    print("║          Seleccione una opción:       ║")
    print("║                                       ║")
    print("║  1. Menú de Usuario                   ║")
    print("║     ➤ Acceder a las opciones de usuario")
    print("║                                       ║")
    print("║  2. Menú de Administrador             ║")
    print("║     ➤ Acceder a las opciones de administrador")
    print("║                                       ║")
    print("╠═══════════════════════════════════════╣")
    print("║  Por favor, ingrese el número de su opción:   ║")
    print("╚═══════════════════════════════════════╝")
