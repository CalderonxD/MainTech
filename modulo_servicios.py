# from datos import *
from datos import*
from modulo_ventas import*
def registro_mantenimieno(id_usuario,datosCliente, datosServicio):
    while True:
        try:
            print("Ingrese el número del servicio que desea contratar:")
            print("1. Limpieza")
            print("2. Reestablecer Equipo")
            print("3. Comprar e instalar productos")
            print("0. para volver")
            opc = int(input())
        except ValueError:
            print("Ingrese un número válido.")
            continue
        else:
            if opc == 1:
                for usuario in datosCliente["usuarios"]:
                    if usuario["id"] == id_usuario:
                        if usuario.get("equipos"):
                            for equipo in usuario["equipos"]:
                                limpieza = {
                                    "id_solicitud": str(len(datosServicio["servicios"][0]["solicitudes"]) + 1),
                                    "cliente": usuario["nombre"],
                                    "tecnico": "",
                                    "serial": equipo["serial"],
                                    "estado_avance": "asignado",
                                    "estado_pago": False
                                }
                                datosServicio["servicios"][opc - 1]["solicitudes"].append(limpieza)
                                print("Servicio de Limpieza registrado exitosamente!")
                                registrar_historial_limpieza(limpieza["id_solicitud"], limpieza["cliente"], 0)
                                break
                            
            elif opc == 2:
                for usuario in datosCliente["usuarios"]:
                    if usuario["id"] == id_usuario:
                        if usuario.get("equipos"):
                            for equipo in usuario["equipos"]:
                                reestablecer = {
                                    "id_solicitud": str(len(datosServicio["servicios"][1]["solicitudes"]) + 1),
                                    "cliente": usuario["nombre"],
                                    "tecnico": "",
                                    "serial": equipo["serial"],
                                    "estado_avance": "asignado",
                                    "estado_pago": False
                                }
                                datosServicio["servicios"][opc - 1]["solicitudes"].append(reestablecer)
                                print("Servicio de Reestablecer Equipo registrado exitosamente!")
                                registrar_historial_restablecer(reestablecer["id_solicitud"], reestablecer["cliente"], 0)
                                break
                            
                            
            elif opc == 3:
                for usuario in datosCliente["usuarios"]:
                    if usuario["id"] == id_usuario:
                        if usuario.get("equipos"):
                            for equipo in usuario["equipos"]:
                                # Mostrar y seleccionar productos disponibles
                                print("Productos disponibles para comprar e instalar:")
                                productos_disponibles = datosServicio["productos"]["graficas"] + datosServicio["productos"]["procesadores"] + datosServicio["productos"]["ram"]
                                
                                productos_seleccionados = []
                                total_valor = 0
                                
                                while True:
                                    print("Seleccione un producto para agregar (0 para terminar): ")
                                    for idx, producto in enumerate(productos_disponibles, start=1):
                                        print(f"{idx}. {producto['nombre']} - ${producto['precio']}")
                                    
                                    try:
                                        opcion_producto = int(input())
                                        if opcion_producto == 0:
                                            break
                                        elif opcion_producto < 1 or opcion_producto > len(productos_disponibles):
                                            print("Opción inválida.")
                                            continue
                                        
                                        producto_seleccionado = productos_disponibles[opcion_producto - 1]
                                        productos_seleccionados.append(producto_seleccionado)
                                        total_valor += producto_seleccionado["precio"]
                                        print(f"{producto_seleccionado['nombre']} agregado.")
                                    except ValueError:
                                        print("Ingrese un número válido.")
                                
                                comprar_instalar = {
                                    "id_solicitud": str(len(datosServicio["servicios"][2]["solicitudes"]) + 1),
                                    "cliente": usuario["nombre"],
                                    "tecnico": "",
                                    "serial": equipo["serial"],
                                    "estado_avance": "asignado",
                                    "estado_pago": False,
                                    "valor": total_valor,
                                    "productos": productos_seleccionados
                                }
                                datosServicio["servicios"][opc - 1]["solicitudes"].append(comprar_instalar)
                                print("Servicio de Comprar e Instalar Productos registrado exitosamente!")
                                 # Registrar compra en historial de ventas
                                registrar_compra(comprar_instalar["id_solicitud"], usuario["nombre"], total_valor, productos_seleccionados)
                                break
            elif opc == 0:
                break
            
            else:
                print("Opción no implementada.")
    
            break
        



def agregar_servicio(datos):
    datos = dict(datos)
    servicio = {}
    servicio["servicio"] = input("Ingrese el nombre del servicio: ")
    servicio["precio"] = int(input("Ingrese el precio del servicio: "))
    servicio["solicitudes"] = []
    
    datos["servicios"].append(servicio)
    print("Servicio registrado exitosamente!")
        
    return datos




def eliminar_servicio(datos):
    datos = dict(datos)
    try:
        nombre = input("Ingrese el nombre del servicio: ")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos

    servicio_encontrado = False
    for i in range(len(datos["servicios"])):
        if "servicio" in datos["servicios"][i]:
            if datos["servicios"][i]["servicio"] == nombre:
                confirmacion = input(f"¿Está seguro de que desea eliminar el servicio '{nombre}'? (si/no): ").lower()
                if confirmacion == 'si':
                    datos["servicios"].pop(i)
                    print("Servicio eliminado!")
                else:
                    print("Eliminación cancelada.")
                servicio_encontrado = True
                break
        else:
            print(f"Advertencia: Entrada en el índice {i} no contiene la clave 'servicio'.")

    if not servicio_encontrado:
        print("Servicio no existe")
    
    return datos





def editar_servicio(datos):
    datos = dict(datos)
    buscar_servicio = input("Ingrese el nombre del servicio: ")

    try:
        for servicios in datos["servicios"]:
            if servicios["servicio"] == buscar_servicio:
                print("Servicio encontrado!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_precio = input("Nuevo precio (Enter para dejar sin cambios): ")

                if nuevo_nombre:
                    servicios["servicio"] = nuevo_nombre
                if nuevo_precio:
                    servicios["precio"] = nuevo_precio
                print("Servicio editado con éxito!")
                break
        else:
            print("Servicio no encontrado!")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    return datos




def mostrar_servicios(datos):
    for servicio in datos.get('servicios', []):
        print(f"Servicio: {servicio['servicio']}, Precio: {servicio['precio']}")
    return datos
    




#Funcion que permite  al tecnico consultar si existen solicitudes pendientes por realizar
def consultar_solicitudes_pendientes(datos_servicios, datos_usuarios):
    solicitudes = []
    datos_usuarios = bajar_datos("usuarios.json")
    
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["tecnico"] == "" and servicio["solicitudes"][i]["estado_pago"] == True and servicio["servicio"] != "comprar e instalar productos":
                diccionario = {}
                diccionario["servicio"] = servicio["servicio"]
                diccionario["id_solicitud"] = servicio["solicitudes"][i]["id_solicitud"]
                diccionario["cliente"] = servicio["solicitudes"][i]["cliente"]
                diccionario["serial_equipo"] = servicio["solicitudes"][i]["serial"]
                telefono_cliente = "No disponible"  # Valor por defecto
                for usuario in datos_usuarios["usuarios"]:
                    if usuario["nombre"] == servicio["solicitudes"][i]["cliente"] and usuario["rol"] == "Cliente":
                        telefono_cliente = usuario["numero"]
                        break
                diccionario["telefono_cliente"] = telefono_cliente
                solicitudes.append(diccionario)
                
            elif servicio["solicitudes"][i]["tecnico"] == "" and servicio["solicitudes"][i]["estado_pago"] == True and servicio["servicio"] == "comprar e instalar productos":
                diccionario = {}
                diccionario["servicio"] = servicio["servicio"]
                diccionario["id_solicitud"] = servicio["solicitudes"][i]["id_solicitud"]
                diccionario["cliente"] = servicio["solicitudes"][i]["cliente"]
                diccionario["serial_equipo"] = servicio["solicitudes"][i]["serial"]
                telefono_cliente = "No disponible"  # Valor por defecto
                for usuario in datos_usuarios["usuarios"]:
                    if usuario["nombre"] == servicio["solicitudes"][i]["cliente"] and usuario["rol"] == "Cliente":
                        telefono_cliente = usuario["numero"]
                        break
                diccionario["telefono_cliente"] = telefono_cliente
                diccionario["productos"] = servicio["solicitudes"][i]["productos"]
                solicitudes.append(diccionario)
    
    if len(solicitudes) != 0:
        for diccionario in solicitudes:
            for llave, valor in diccionario.items():
                if llave != "productos" and llave != "valor":
                    print(f"{(llave.capitalize()).replace('_', ' ')}: {valor}")
                else:
                    print(f"{(llave.capitalize()).replace('_', ' ')}:")
                    for i in range(len(valor)):
                        print(f"{i + 1}. {valor[i]['nombre']}")
            print("")
    else:
        print("No existen solicitudes pendientes por el momento")


#Funcion que permite al tecnico consultar las solicitudes que esta realizando
def consultar_solicitudes_por_realizar(id_tecnico, datos_servicios):
    solicitudes=[]
    datos_usuarios=bajar_datos("usuarios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_tecnico and usuario["rol"]=="Tecnico":
            nombre_tecnico=usuario["nombre"]
            break
    
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["tecnico"]==nombre_tecnico and servicio["solicitudes"][i]["estado_avance"]!="finalizado" and servicio["servicio"]!="comprar e instalar productos":
                diccionario={}
                diccionario["servicio"]=servicio["servicio"]
                diccionario["id_solicitud"]=servicio["solicitudes"][i]["id_solicitud"]
                #diccionario["fecha_registro"]=servicio["solicitudes"][i]["fecha"]
                diccionario["estado_avance"]=servicio["solicitudes"][i]["estado_avance"]
                diccionario["cliente"]=servicio["solicitudes"][i]["cliente"]
                diccionario["serial_equipo"]=servicio["solicitudes"][i]["serial"]
                for usuario in datos_usuarios["usuarios"]:
                    if usuario["nombre"] == servicio["solicitudes"][i]["cliente"] and usuario["rol"] == "Cliente":
                        telefono_cliente = usuario["numero"]
                        break
                    else:
                        # Manejar el caso donde no se encuentra ningún usuario coincidente
                        telefono_cliente = "Número no disponible"  # O cualquier valor predeterminado que prefieras

                diccionario["telefono_cliente"] = telefono_cliente

                diccionario["telefono_cliente"]=telefono_cliente
                solicitudes.append(diccionario)
                
            elif servicio["solicitudes"][i]["tecnico"]==nombre_tecnico and servicio["solicitudes"][i]["estado_avance"]!="finalizado" and servicio["servicio"]=="comprar e instalar productos":
                diccionario={}
                diccionario["servicio"]=servicio["servicio"]
                diccionario["id_solicitud"]=servicio["solicitudes"][i]["id_solicitud"]
                #diccionario["fecha_registro"]=servicio["solicitudes"][i]["fecha"]
                diccionario["estado_avance"]=servicio["solicitudes"][i]["estado_avance"]
                diccionario["cliente"]=servicio["solicitudes"][i]["cliente"]
                diccionario["serial_equipo"]=servicio["solicitudes"][i]["serial"]
                for usuario in datos_usuarios["usuarios"]:
                    if usuario["nombre"]==servicio["solicitudes"][i]["cliente"] and usuario["rol"]=="Cliente":
                        telefono_cliente=usuario["numero"]
                        break
                diccionario["telefono_cliente"]=telefono_cliente
                diccionario["productos"]=servicio["solicitudes"][i]["productos"]
                solicitudes.append(diccionario)
    
    if len(solicitudes)!=0:
        for diccionario in solicitudes:
            for llave,valor in diccionario.items():
                if llave!="productos" and llave!="valor":
                    print(f"{(llave.capitalize()).replace("_"," ")}: {valor}")
                else:
                    print(f"{(llave.capitalize()).replace("_"," ")}:")
                    for i in range(len(valor)):
                        print(f"{i+1}. {valor[i]["nombre"]}")
            print("")
    else:
        print("No existen solicitudes que este realizando por el momento")    


#Funcion que permite al tecnico actualizar el estado de avance de la solicitud
def actualizar_avance_solicitud(id_tecnico, datos_servicios):
    datos_usuarios=bajar_datos("usuarios.json")
    solicitud_encontrada=False
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_tecnico and usuario["rol"]=="Tecnico":
            nombre_tecnico=usuario["nombre"]
            break
    
    id_solicitud_ingresado= input("Ingrese el id de la solicitud de servicio a la que desea actualizarle el estado de avance: ")
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado and servicio["solicitudes"][i]["tecnico"]==nombre_tecnico:
                solicitud_encontrada=True
                estado_avance=input("Ingrese el estado de avance de la solicitud: ")
                servicio["solicitudes"][i]["estado_avance"]=estado_avance.lower()
                print("El estado de avance de la solicitud se ha actualizado correctamente")
                return datos_servicios
        
    if solicitud_encontrada==False:
        print("No se pudo entrar un id de solicitud", id_solicitud_ingresado, "relacionado a su documento")
        return datos_servicios        


#Funcion que permite a un cliente cancelar (borrar del json) una solicitud de mantenimiento si todavia no se ha pagado
def cancelar_solicitud_mantenimiento(id_cliente, datos_servicios):
    solicitud_encontrada=False
    datos_usuarios=bajar_datos("usuarios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            nombre_cliente=usuario["nombre"]
            break
    
    id_solicitud_ingresado= input("Ingrese el id de su solicitud de servicio: ")
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado and servicio["solicitudes"][i]["estado_pago"]==False and servicio["solicitudes"][i]["cliente"]==nombre_cliente:
                solicitud_encontrada=True
                decision=confirmar_decision()
                if decision:
                    servicio["solicitudes"].pop(i)
                    print("Su solicitud de mantenimiento ha sido cancelada correctamente")
                    return datos_servicios
                else:
                    print("Su solicitud de mantenimiento no ha sido cancelada")
                    return datos_servicios
                
            elif servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado and servicio["solicitudes"][i]["estado_pago"]==True and servicio["solicitudes"][i]["cliente"]==nombre_cliente:
                solicitud_encontrada=True
                print("Su solicitud de mantenimiento no puede ser cancelada porque ya se realizo el pago")
                return datos_servicios
    
    if solicitud_encontrada==False:
        print("Lo sentimos, no encontramos un id de solicitud", id_solicitud_ingresado, "relacionado a su documento")
        return datos_servicios


#funcion que permite confirmar una decision tomada
def confirmar_decision():
    while True:
        decision = input("¿Esta seguro que desea realizar esta acción? (Si o No): ")
        if decision.lower()=="si":
            return True
        elif decision.lower()=="no":
            return False
        else:
            print("Valor invalido")            
       
                
#Funcion que permite a un cliente consultar el estado de avance de una solicitud de servicio ingresando su id
def consultar_avance_solicitud(id_cliente, datos_servicios):
    id_solicitud_ingresado= input("Ingrese el id de su solicitud de servicio: ")
    id_solicitud_encontrado=False
    
    datos_usuarios=bajar_datos("usuarios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            nombre_cliente=usuario["nombre"]
            break
    
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado and servicio["solicitudes"][i]["cliente"]==nombre_cliente:
                id_solicitud_encontrado=True
                print("El estado de avance de su solicitud es:", servicio["solicitudes"][i]["estado_avance"])
                tecnico_solicitud=servicio["solicitudes"][i]["tecnico"]
                
                if tecnico_solicitud!="":
                    for usuario in datos_usuarios["usuarios"]:
                        if usuario["nombre"]==tecnico_solicitud and usuario["rol"]=="Tecnico":
                            telefono_tecnico=usuario["numero"]
                            print("El técnico asignado a esta solicitud es:", tecnico_solicitud)
                            print("Para mas información puede comunicarse con él al número:", telefono_tecnico)
                            break
                else:
                    print("Y todavía no tiene un ténico asignado")
                break
    
    if id_solicitud_encontrado==False:
        print("Lo sentimos, no existe un id de solicitud", id_solicitud_ingresado, "relacionado a su documento")              
 


#Funcion que permite al cliente consultar el historial de las solicitudes que ha realizado
def consultar_historial_solicitudes(id_cliente, datos_servicios):
    solicitudes=[]
    datos_usuarios=bajar_datos("usuarios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            nombre_cliente=usuario["nombre"]
            break
    
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["cliente"]==nombre_cliente:
                diccionario={}
                diccionario=servicio["solicitudes"][i].copy()
                diccionario["valor servicio"]=servicio["precio"]
                solicitudes.append(diccionario)
    
    if len(solicitudes)!=0:
        for diccionario in solicitudes:
            for llave,valor in diccionario.items():
                if llave!="productos" and llave!="valor":
                    print(f"{(llave.capitalize()).replace("_"," ")}: {valor}")
                elif llave=="valor":
                    print(f"Valor productos: {valor}")
                else:
                    print(f"{(llave.capitalize()).replace("_"," ")}:")
                    for i in range(len(valor)):
                        print(f"{i+1}. {valor[i]["nombre"]}  {valor[i]["precio"]}")
            print("")
    else:
        print("Lo sentimos, no existen solicitudes relacionadas a su documento")


#Funcion que permite al tecnico elegir una solicitud para realizar (poner su nombre en el campo "tecnico" de una solicitud del json)
def elegir_solicitud_para_realizar(id_tecnico, datos_servicios):
    datos_usuarios = bajar_datos("usuarios.json")
    solicitud_encontrada = False
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"] == id_tecnico and usuario["rol"] == "Tecnico":
            nombre_tecnico = usuario["nombre"]
            break
    
    id_solicitud_ingresado = input("Ingrese el id de la solicitud de servicio que desea realizar: ")
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if (servicio["solicitudes"][i]["id_solicitud"] == id_solicitud_ingresado 
                and servicio["solicitudes"][i]["tecnico"] == "" 
                and servicio["solicitudes"][i]["estado_pago"] == True):
                solicitud_encontrada = True
                servicio["solicitudes"][i]["tecnico"] = nombre_tecnico
                print("La solicitud se le ha asignado correctamente")
                print("Las solicitudes que tiene por realizar son: ")
                consultar_solicitudes_por_realizar(id_tecnico, datos_servicios)
                return datos_servicios
    
    if not solicitud_encontrada:
        print("No se pudo encontrar un id de solicitud", id_solicitud_ingresado, "en las solicitudes de servicio pendientes")
        return datos_servicios
