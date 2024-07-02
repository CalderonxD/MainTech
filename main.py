#imports
from datos import *
# from datos import bajar_datos
# from modulo_usuarios import *
# from modulo_tecnicos import *
from menus import *
# from modulo_servicios import *
# from contactanos import*
# from preguntasyrespuesta import*
# from modulo_ventas import *
# from modulo_pago import*
# from menus import ejecutable

#constantes
RUTA_USUARIOS = "usuarios.json"
RUTA_SERVICIOS = "servicios.json"
RUTA_HISTORIAL_VENTAS = "historial_ventas.json"


#cargar datos
while True:
    datosUsuario = bajar_datos(RUTA_USUARIOS)
    datosServicios = bajar_datos(RUTA_SERVICIOS)
    ejecutable(datosUsuario,datosServicios)
    break


