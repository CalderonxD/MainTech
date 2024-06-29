#imports
from datos import *
from datos import bajar_datos
from modulo_usuarios import *
from modulo_tecnicos import *
from menus import *
from modulo_servicios import *
from modulo_servicios import registro_mantenimiento
from datos import subir_datos
#constantes
RUTA_USUARIOS = "usuarios.json"
RUTA_SERVICIOS = "servicios.json"
#cargar datos
while True:
    datosUsuario = bajar_datos(RUTA_USUARIOS)
    datosServicios = bajar_datos(RUTA_SERVICIOS)
    #datosUsuario = eliminar_usuario(datosUsuario)
    
    #datosUsuario = editar_usuario(datosUsuario)
    
    # agregar_servicio(datosServicios)
    #registro_mantenimiento(datosUsuario,datosServicios)
    #subir_datos(datosServicios,RUTA_SERVICIOS)

    #(datosServicios)
    #subir_datos(datosServicios,RUTA_SERVICIOS)       
    #break

    mostrar_servicios(datosServicios)
    break