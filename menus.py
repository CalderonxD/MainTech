from datos import *
import json
from modulo_usuarios import *
from modulo_pago import *
from preguntasyrespuesta import *
from contactanos import *
from modulo_servicios import *
from modulo_ventas import *
from modulo_tecnicos import *

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

def ejecutable(datos_usuario,datosServicios):
    opc = 0
    while True:
        menu_principal(datos_usuario)
        try:
            opc = int(input("-"))
            print("╭───────────────────────────────────────╮")
            print("│                                       │")
            print("│            ¡Opción ingresada!         │")
            print("│                                       │")
            print("╰───────────────────────────────────────╯")
            if opc not in [1,2,3]:
                raise ValueError("Opcion invalida")
        except Exception as error:
            error = "opcion no valida"
            print(error)
            continue
        else:
            if opc == 1:
                datosUsuarios = bajar_datos(RUTA_USUARIOS)
                datosUsuarios = opcion_sesion(datosUsuarios,datosServicios)
                break
            elif opc == 2:
                datosUsuarios = bajar_datos(RUTA_USUARIOS)
                datosUsuarios = registrar_usuario(datosUsuarios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
            elif opc == 3:
                print("--------------------SALIENDO---------------------")
                break
            subir_datos(datosUsuarios,RUTA_USUARIOS)
            break






def opcion_sesion(datosUsuarios, datosServicios):
    while True:
        usuario_id = input("Ingrese su id o cedula: ")
        usuario_clave = input("Ingrese su contraseña: ")
        usuario_encontrado = False
        
        for usuario_info in datosUsuarios["usuarios"]:
            if usuario_info["id"] == usuario_id and usuario_info["contrasena"] == usuario_clave:
                usuario_encontrado = True
                if usuario_info["rol"] == "Cliente":
                    menu_clientes(usuario_id, datosUsuarios,datosServicios)
                elif usuario_info["rol"] == "Tecnico":
                    menu_tecnicos(usuario_id,datosServicios,datosUsuarios)
                elif usuario_info["rol"] == "Admin":
                    menu_admin(datosUsuarios,datosServicios)
                break  # Salir del bucle si el usuario es encontrado
                
        if not usuario_encontrado:
            print("La clave o el usuario son incorrectos")
        else:
            break  # Salir del bucle principal si el usuario es encontrado


def menu_clientes(id_usuario,datosUsuarios,datosServicios):
    while True:
        try:
            opc = 0
            menu_usuarios()
            opc = int(input("-"))
            if opc not in [1,2,3,4,5,6,7,8,9]:
                raise ValueError("Opcion invalida")
        except Exception as error:
            error = "opcion no valida"
            print(error)
        else:
            if opc == 1:
                consultar_pagos_realizados(id_usuario,datosUsuarios)
            elif opc == 2:
                eliminar_usuario(id_usuario,datosUsuarios,datosUsuarios,datosServicios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
                ejecutable(datosUsuarios,datosServicios)
            elif opc == 3:
                mostrar_faq(faq)
            elif opc == 4:
                mostrar_informacion_contacto(empresa)
            elif opc == 5:
                cancelar_solicitud_mantenimiento(id_usuario,datosServicios)
                subir_datos(datosServicios,RUTA_SERVICIOS)
            elif opc == 6:
                while True:
                    menu_servicios()
                    try:
                        eleccion = int(input("-"))
                        if eleccion not in [1,2]:
                            raise ValueError("Opcion invalida")
                    except Exception as error:
                        error = "opcion no valida"
                        print(error)
                    else:
                        if eleccion == 1:
                            mostrar_servicios(datosServicios)
                        elif eleccion == 2:
                            registro_mantenimieno(id_usuario,datosUsuarios,datosServicios)
                            subir_datos(datosServicios,RUTA_SERVICIOS)
                            break
            elif opc == 7:
                editar_usuario(datosUsuarios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
            elif opc == 8:
                agregar_equipo(id_usuario,datosUsuarios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
            elif opc == 9:
                ejecutable(datosUsuarios,datosServicios)
                break
                        
               
def menu_admin(datosUsuarios,datosServicios):
    while True:
        try:
            opc = 0
            menu_administrador()
            opc = int(input("-"))
            if opc not in [1,2,3,4,5,6,7,8,9]:
                raise ValueError("Opcion invalida")
        except Exception as error:
            error = "opcion no valida"
            print(error)
        else:
            if opc == 1:
                mostrar_ventas_ganancias(RUTA_HISTORIAL_VENTAS)
            elif opc == 2:
                agregar_servicio(datosServicios)
                subir_datos(datosServicios,RUTA_SERVICIOS)
            elif opc == 3:
                editar_servicio(datosServicios)
                subir_datos(datosServicios,RUTA_SERVICIOS)
            elif opc == 4:
                eliminar_servicio(datosServicios)
                subir_datos(datosServicios,RUTA_SERVICIOS)
            elif opc == 5:
                mostrar_usuario(datosUsuarios)
            elif opc == 6:
                registrar_tecnico(datosUsuarios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
            elif opc == 7:
                editar_tecnico(datosUsuarios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
            elif opc == 8:
                eliminar_tecnico(datosUsuarios)
                subir_datos(datosUsuarios,RUTA_USUARIOS)
            elif opc == 9:
                ejecutable(datosUsuarios,datosServicios)
                break
        
        
        
    
    
    
def menu_tecnicos(id_usuario,datosServicios,datosUsuarios):
    while True:
        try:
            opc = 0
            menu_tecnico()
            opc = int(input("-"))
            if opc not in [1,2,3,4,5,6,7,8,9]:
                raise ValueError("Opcion invalida")
        except Exception as error:
            error = "opcion no valida"
            print(error)
        else:
            if opc == 1:
                consultar_solicitudes_pendientes(datosServicios,datosUsuarios)
            elif opc == 2:
                consultar_solicitudes_por_realizar(id_usuario,datosServicios)
            elif opc == 3:
                actualizar_avance_solicitud(id_usuario,datosServicios)
                subir_datos(datosServicios,RUTA_SERVICIOS)
            elif opc == 4:
                elegir_solicitud_para_realizar(id_usuario,datosServicios)
                subir_datos(datosServicios,RUTA_SERVICIOS)
            elif opc == 5:
                ejecutable(datosUsuarios,datosServicios)
                break
            

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




def menu_administrador():
    print("╔═══════════════════════════════════════╗")
    print("║       ¡Bienvenido Administrador!      ║")
    print("╠═══════════════════════════════════════╣")
    print("║  Seleccione una opción del menú:      ║")
    print("║                                       ║")
    print("║  1. Consultar Ventas                  ║")
    print("║     ➤ Ver el historial completo de ventas")
    print("║                                       ║")
    print("║  2. Registrar Nuevo Servicio          ║")
    print("║     ➤ Añadir un nuevo servicio        ║")
    print("║                                       ║")
    print("║  3. Modificar Servicio                ║")
    print("║     ➤ Modificar un servicio existente ║")
    print("║                                       ║")
    print("║  4. Eliminar Servicio                 ║")
    print("║     ➤ Eliminar un servicio            ║")
    print("║                                       ║")
    print("║  5. Consultar Clientes                ║")
    print("║     ➤ Ver la lista de clientes        ║")
    print("║                                       ║")
    print("║  6. Registrar Técnico                 ║")
    print("║     ➤ Añadir un nuevo técnico         ║")
    print("║                                       ║")
    print("║  7. Modificar Información de Técnico  ║")
    print("║     ➤ Modificar datos de un técnico   ║")
    print("║                                       ║")
    print("║  8. Eliminar Técnico                  ║")
    print("║     ➤ Eliminar un técnico             ║")
    print("║                                       ║")
    print("║  9. Salir                             ║")
    print("║     ➤ Cerrar el programa              ║")
    print("╚═══════════════════════════════════════╝")


def menu_tecnico():
    print("╔════════════════════════════════════════════════╗")
    print("║                 Menú Técnicos                  ║")
    print("╠════════════════════════════════════════════════╣")
    print("║       Seleccione una opción del menú:          ║")
    print("║                                                ║")
    print("║  1. Ver Lista de Solicitudes Pendientes        ║")
    print("║     ➤ Consultar solicitudes de mantenimiento  ║")
    print("║        pendientes                              ║")
    print("║                                                ║")
    print("║  2. Ver Lista de Solicitudes Por Realizar      ║")
    print("║     ➤ Consultar solicitudes de mantenimiento  ║")
    print("║        por realizar                            ║")
    print("║                                                ║")
    print("║  3. Actualizar Avance de Solicitud             ║")
    print("║     ➤ Modificar el avance de una solicitud de ║")
    print("║        servicio                                ║")
    print("║                                                ║")
    print("║  4. Elegir Solicitud para Realizar             ║")
    print("║     ➤ Seleccionar una solicitud para comenzar ║")
    print("║        a trabajar                              ║")
    print("║                                                ║")
    print("║  5. Salir                                      ║")
    print("║     ➤ Cerrar el programa                      ║")
    print("╚════════════════════════════════════════════════╝")





def menu_usuarios():
    print("╔════════════════════════════════════════════════╗")
    print("║                 Menú Usuarios                  ║")
    print("╠════════════════════════════════════════════════╣")
    print("║       Seleccione una opción del menú:          ║")
    print("║                                                ║")
    print("║  1. Ver Mi Historial de Pago                   ║")
    print("║     ➤ Consultar el historial de pagos         ║")
    print("║                                                ║")
    print("║  2. Eliminar Mi Cuenta                         ║")
    print("║     ➤ Eliminar mi cuenta de usuario           ║")
    print("║                                                ║")
    print("║  3. Preguntas Frecuentes                       ║")
    print("║     ➤ Ver respuestas a preguntas comunes      ║")
    print("║                                                ║")
    print("║  4. Información de la Empresa                  ║")
    print("║     ➤ Ver información sobre la empresa        ║")
    print("║                                                ║")
    print("║  5. Cancelar Solicitud de Mantenimiento        ║")
    print("║     ➤ Cancelar una solicitud de mantenimiento ║")
    print("║                                                ║")
    print("║  6. Consultar y Solicitar Servicios            ║")
    print("║     ➤ Ver y solicitar servicios disponibles   ║")
    print("║                                                ║")
    print("║  7. Modificar Mis Datos de Cliente             ║")
    print("║     ➤ Modificar información personal          ║")
    print("║                                                ║")
    print("║  8. agregar equipo                             ║")
    print("║     ➤ Agregar Equipo a su perfil              ║")
    print("║                                                ║")
    print("║  9. Salir                                      ║")
    print("║     ➤ Cerrar el programa                      ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")

def menu_servicios():
    print("╔════════════════════════════════════════╗")
    print("║            Menú de Servicios           ║")
    print("╠════════════════════════════════════════╣")
    print("║  1. Mostrar Servicios                  ║")
    print("║     ➤ Ver los servicios disponibles   ║")
    print("║                                        ║")
    print("║  2. Solicitar Servicios                ║")
    print("║     ➤ Solicitar un servicio específico ║")
    print("╚════════════════════════════════════════╝")
