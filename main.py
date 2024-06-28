from datos import *
from datos import bajar_datos
from modulo_tecnicos import *
from menus import *
from registro_mantenimiento import registro_mantenimiento

RUTA_JSON = "usuarios.json"
datosUsuario = bajar_datos(RUTA_JSON)

while True:
    if validar_inicio_sesion(datosUsuario):
        break

registro_mantenimiento(datosUsuario)

