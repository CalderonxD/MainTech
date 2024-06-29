# from datos import *

def registro_mantenimiento(datosCliente, datosServicio):
    while True:
        try:
            print("Ingrese el número del servicio que desea contratar:")
            print("1. Limpieza")
            print("2. Reestablecer Equipo")
            print("3. Comprar e instalar productos")
            opc = int(input())
        except ValueError:
            print("Ingrese un número válido.")
            continue
        except KeyboardInterrupt:
            print("Operación interrumpida por el usuario.")
            break
        
        cedula = "1097097808"  # Cédula del cliente (puedes cambiar esto según tus necesidades)
        
        if opc == 1:
            for usuario in datosCliente["usuarios"]:
                if usuario["id"] == cedula:
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
                            break
        
        elif opc == 2:
            for usuario in datosCliente["usuarios"]:
                if usuario["id"] == cedula:
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
                            break

        elif opc == 3:
            for usuario in datosCliente["usuarios"]:
                if usuario["id"] == cedula:
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
                            break
        
        else:
            print("Opción no implementada.")

        break
        
        # elif opc == 3:
        #     for usuario in datosCliente["usuarios"]:
        #         if usuario["id"] == cedula:
        #             if usuario.get("equipos"):
        #                 for equipo in usuario["equipos"]:
        #                     comprar_instalar = {
        #                         "id_solicitud": str(len(datosServicio["servicios"][2]["solicitudes"]) + 1),
        #                         "cliente": usuario["nombre"],
        #                         "tecnico": "",
        #                         "serial": equipo["serial"],
        #                         "estado_avance": "asignado",
        #                         "estado_pago": False,
        #                         "valor": 0,
        #                         "productos": []
        #                     }
        #                     datosServicio["servicios"][opc - 1]["solicitudes"].append(comprar_instalar)
        #                     print("Servicio de Comprar e Instalar Productos registrado exitosamente!")
        #                     break
        
        # else:
        #     print("Opción no implementada.")

        # break
       



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

                if nuevo_precio:
                    servicios["servicio"] = nuevo_nombre
                if nuevo_nombre:
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

    



def agregar_servicio_al_usuario(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario") 

    for usuario in datos["usuarios"]:
        if usuario["id"] == buscar_usuario:
            print("Usuario encontrado!")
            servicio = input("Ingrese el servicio que quieres contratar: ")
            if servicio:
                usuario["servicio"] = servicio
                print("Su servicio ha sido contratado con éxito!")
                usuario_encontrado = True  
            break  
    
    if not usuario_encontrado:
        print("Usuario no encontrado")
    
def eliminar_servicio_al_usuario(datos):
    datos = dict(datos)
    try:
        documento = input("Ingrese el documento del usuario: ")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["id"] == documento:
            datos["servicio"].pop(i)
            print("Usuario eliminado!")
            return datos
    
    return datos


def modificar_servicio_al_usuario(datos):
    datos = dict(datos)
    try:
        buscar_usuario = input("Ingrese el documento del usuario: ")
    except KeyboardInterrupt:
        print("Operación interrumpida por el usuario")
        return datos
    
    usuario_encontrado = False  

    for usuario in datos["usuarios"]:
        if usuario["id"] == buscar_usuario:
            print("Usuario encontrado!")
            servicio = input("Ingrese el nuevo servicio que quieres contratar: ")
            if servicio:
                usuario["servicio"] = servicio
                print("Su servicio ha sido modificado con éxito!")
                usuario_encontrado = True  
            break  
    
    if not usuario_encontrado:
        print("Usuario no encontrado")
    
    return datos



#def cancelar_solicitud_mantenimiento(datos):
    id_solicitud_ingresado= input("Ingrese el id de su solicitud de servicio: ")
    for servicio in datos["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["id_socilitud"]==id_solicitud_ingresado and servicio["equipos_asignados"][i]["estado_pago"]==False:
                decision=confirmar_decision()
                if decision:
                    servicio["solicitudes"].pop(i)
                    print("Su solicitud de mantenimiento ha sido cancelada correctamente")
                    return datos
                else:
                    print("Su solicitud de mantenimiento no ha sido cancelada")
                    return datos
                
            elif servicio["solicitudes"][i]["id_socilitud"]==id_solicitud_ingresado and servicio["equipos_asignados"][i]["estado_pago"]==True:
                print("Su solicitud de mantenimiento no puede ser cancelada porque ya se realizo el pago")
                return datos

#def confirmar_decision():
    while True:
        decision = input("¿Esta seguro que desea realizar esta acción? (Si o No)")
        if decision.lower()=="si":
            return True
        elif decision.lower()=="no":
            return False
        else:
            print("Valor invalido")

#def consultar_realizacion_mantenimiento(id_cliente, datos_servicios):
    id_solicitud_ingresado= input("Ingrese el id de su solicitud de servicio: ")
    id_solicitud_encontrado=False
    
    datos_usuarios=bajar_datos("usuarios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            nombre_cliente=usuario["nombre"]
            break
    
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["id_socilitud"]==id_solicitud_ingresado and servicio["solicitudes"][i]["cliente"]==nombre_cliente:
                id_solicitud_encontrado=True
                print("El estado de su solicitud es:", servicio["solicitudes"][i]["estado_avance"])
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
        print("Lo sentimos, no existe un id de solicitud ", id_solicitud_ingresado, "relacionado a su documento")              
  

#def consultar_solicitudes_mantenimiento(id_cliente, datos_servicios):
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
                        print(f"{i+1}. {valor[i]["nombre"]}  {valor[i]["valor"]}")
            print("")
    else:
        print("No existen solicitudes relacionadas a su documento")