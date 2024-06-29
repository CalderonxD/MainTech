from datos import *
from datos import bajar_datos
from modulo_usuarios import *
from modulo_tecnicos import *
from menus import *
from modulo_servicios import registro_mantenimiento

RUTA_JSON = "usuarios.json"
datosUsuario = bajar_datos(RUTA_JSON)

datosUsuario = eliminar_usuario(datosUsuario)

datosUsuario = editar_usuario(datosUsuario)

""" while True:
    if validar_inicio_sesion(datosUsuario):
        break

registro_mantenimiento(datosUsuario)
 """
