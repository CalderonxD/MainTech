from datos import *
from modulo_tecnicos import*
from menus import*
RUTA_JSON = "usuarios.json"
datosUsuario = bajar_datos(RUTA_JSON)

while True:
    if validar_inicio_sesion(datosUsuario):
        break



