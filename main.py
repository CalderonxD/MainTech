#imports
from datos import *
from datos import bajar_datos
from modulo_usuarios import *
from modulo_tecnicos import *
from menus import *
from modulo_servicios import *
from contactanos import*
from preguntasyrespuesta import*
from modulo_ventas import *
from modulo_pago import*
from menus import ejecutable

#constantes
RUTA_USUARIOS = "usuarios.json"
RUTA_SERVICIOS = "servicios.json"
RUTA_HISTORIAL_VENTAS = "historial_ventas.json"


#cargar datos
# while True:
datosUsuario = bajar_datos(RUTA_USUARIOS)
datosServicios = bajar_datos(RUTA_SERVICIOS)
#opc = pedir_opcion()
#mostrar_menu_principal()
#pedir_opcion()
ejecutable(datosUsuario,datosServicios)
   # if opc == 1:
    #recargar_billetera("1097097808",datosUsuario)
            
    #elif opc == 2:
        #print("Opción para registrar servicio seleccionada.")
            
    #elif opc == 3:
        #print("Opción para registrar compra seleccionada.")
           
    #elif opc == 4:
        #print("Opción para mostrar historial de ventas seleccionada.")
            
    #elif opc == 5:
        #print("Saliendo del programa. ¡Hasta luego!")
        #break
    #else:
        #print("Opción no válida. Por favor, intente de nuevo.")


