from datetime import datetime
from datos import subir_datos
from datos import bajar_datos
from modulo_servicios import confirmar_decision


#Funcion que permite al cliente recargar su billetera
def recargar_billetera(id_cliente,datos_usuarios):
    while True:
        cantidad_recargar=input("Ingrese la cantidad que desea recargar en su billetera: ")
        if cantidad_recargar.isnumeric()==True:
            break
        else:
            print("Valor invalido")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            decision=confirmar_decision()
            if decision:
                usuario["billetera"]=usuario["billetera"]+int(cantidad_recargar)
                print("Su billetera se ha recargado correctamente")
                print("La cantidad actual en su billetera es:", usuario["billetera"])
                return datos_usuarios
            else:
                print("La recarga a su billetera ha sido cancelada")
                return datos_usuarios
            
    print("Lo sentimos, ha ocurrido un error y no se ha podido recargar su billetera")
    return datos_usuarios


#Funcion que permite al cliente consultar las solicitudes pendientes por pagar
def consultar_solicitudes_por_pagar(id_cliente, datos_servicios):
    solicitudes=[]
    datos_usuarios=bajar_datos("usuarios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            nombre_cliente=usuario["nombre"]
            break
    
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["cliente"]==nombre_cliente and servicio["servicio"]!="comprar e instalar productos" and servicio["solicitudes"][i]["estado_pago"]==False:
                diccionario={}
                diccionario["servicio"]=servicio["servicio"]
                diccionario["precio_servicio"]=servicio["precio"]
                diccionario["id_solicitud"]=servicio["solicitudes"][i]["id_solicitud"]
                #diccionario["fecha_registro"]=servicio["solicitudes"][i]["fecha"]
                diccionario["cliente"]=servicio["solicitudes"][i]["cliente"]
                diccionario["serial_equipo"]=servicio["solicitudes"][i]["serial"]
                diccionario["total_a_pagar"]=servicio["precio"]
                solicitudes.append(diccionario)
                
            elif servicio["solicitudes"][i]["cliente"]==nombre_cliente and servicio["servicio"]=="comprar e instalar productos" and servicio["solicitudes"][i]["estado_pago"]==False:
                diccionario={}
                diccionario["servicio"]=servicio["servicio"]
                diccionario["precio_servicio"]=servicio["precio"]
                diccionario["id_solicitud"]=servicio["solicitudes"][i]["id_solicitud"]
                #diccionario["fecha_registro"]=servicio["solicitudes"][i]["fecha"]
                diccionario["cliente"]=servicio["solicitudes"][i]["cliente"]
                diccionario["serial_equipo"]=servicio["solicitudes"][i]["serial"]
                diccionario["valor"]=servicio["solicitudes"][i]["valor"]
                diccionario["productos"]=servicio["solicitudes"][i]["productos"]
                diccionario["total_a_pagar"]=int(servicio["precio"]) + servicio["solicitudes"][i]["valor"]
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
        print("No existen solicitudes por pagar relacionadas a su documento") 


#Funcion que permite al cliente pagar una solicitud mediante el id de solicitud y teniendo dinero suficiente en su billetera
def pagar_solicitud(id_cliente, datos_usuarios):
    id_solicitud_encontrada=False
    datos_servicios=bajar_datos("servicios.json")
    
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
            nombre_cliente=usuario["nombre"]
            cantidad_billetera=usuario["billetera"]
            break
    
    id_solicitud_ingresado=input("Ingrese el id de la solictud que desea pagar: ")
       
    for servicio in datos_servicios["servicios"]:
        for i in range(len(servicio["solicitudes"])):
            if servicio["solicitudes"][i]["cliente"]==nombre_cliente and servicio["servicio"]!="comprar e instalar productos" and servicio["solicitudes"][i]["estado_pago"]==False and servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado:
                id_solicitud_encontrada=True
                decision=confirmar_decision()
                if decision:
                    total_a_pagar=int(servicio["precio"])
                    
                    if cantidad_billetera>=total_a_pagar:
                        cantidad_restante_billetera=cantidad_billetera - total_a_pagar
                        servicio["solicitudes"][i]["estado_pago"]=True
                        subir_datos(datos_servicios, "servicios.json")
                        
                        for usuario in datos_usuarios["usuarios"]:
                            if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
                                usuario["billetera"]=cantidad_restante_billetera
                                pago={}
                                pago["id_solicitud"]=id_solicitud_ingresado
                                pago["fecha_de_pago"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                pago["servicio"]=servicio["servicio"]
                                pago["precio_servicio"]=int(servicio["precio"])
                                pago["total_pagado"]=total_a_pagar
                                usuario["pagos"].append(pago)
                                print("La solicitud con id",id_solicitud_ingresado, "se ha pagado correctamente")
                                return datos_usuarios
                    
                    else:
                        print("No tiene suficiente dinero en su billetera para realizar esta compra, lo invitamos a recargarla")
                        return datos_usuarios           
                else:
                    print("Su compra se ha cancelado correctamente")
                    return datos_usuarios  
                    
            elif servicio["solicitudes"][i]["cliente"]==nombre_cliente and servicio["servicio"]=="comprar e instalar productos" and servicio["solicitudes"][i]["estado_pago"]==False and servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado:
                id_solicitud_encontrada=True
                decision=confirmar_decision()
                if decision:
                    total_a_pagar=int(servicio["precio"]) + servicio["solicitudes"][i]["valor"]
                    
                    if cantidad_billetera>=total_a_pagar:
                        cantidad_restante_billetera= cantidad_billetera - total_a_pagar
                        servicio["solicitudes"][i]["estado_pago"]=True
                        subir_datos(datos_servicios, "servicios.json")
                        
                        for usuario in datos_usuarios["usuarios"]:
                            if usuario["id"]==id_cliente and usuario["rol"]=="Cliente":
                                usuario["billetera"]=cantidad_restante_billetera
                                pago={}
                                pago["id_solicitud"]=id_solicitud_ingresado
                                pago["fecha_de_pago"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                pago["servicio"]=servicio["servicio"]
                                pago["precio_servicio"]=int(servicio["precio"])
                                pago["precio_productos"]=servicio["solicitudes"][i]["valor"]
                                pago["productos"]=servicio["solicitudes"][i]["productos"]
                                pago["total_pagado"]=total_a_pagar
                                usuario["pagos"].append(pago)
                                print("La solicitud con id",id_solicitud_ingresado, "se ha pagado correctamente")
                                return datos_usuarios
                    else:
                        print("No tiene suficiente dinero en su billetera para realizar esta compra, lo invitamos a recargarla")
                        return datos_usuarios   
                
                else:
                    print("Su compra se ha cancelado correctamente")
                    return datos_usuarios  
                
            elif servicio["solicitudes"][i]["cliente"]==nombre_cliente and servicio["solicitudes"][i]["estado_pago"]==True and servicio["solicitudes"][i]["id_solicitud"]==id_solicitud_ingresado:
                print("La solicitud con id",id_solicitud_ingresado, "ya se ha pagado con anterioridad")
                return datos_usuarios
    
    if id_solicitud_encontrada==False:
        print("Lo sentimos, no existe un id de solicitud", id_solicitud_ingresado, "relacionado a su documento para realizar un pago") 
        return datos_usuarios          


#Funcion que permite al cliente ver los pagos que ha realizado
def consultar_pagos_realizados(id_cliente, datos_usuarios):
    for usuario in datos_usuarios["usuarios"]:
        if usuario["id"]==id_cliente:
            if len(usuario["pagos"])!=0:
                for pago in usuario["pagos"]:
                    for llave,valor in pago.items():
                        if llave!="productos":
                            print(f"{(llave.capitalize()).replace("_"," ")}: {valor}")
                        else:
                            print(f"{(llave.capitalize()).replace("_"," ")}:")
                            for i in range(len(valor)):
                                print(f"{i+1}. {valor[i]["nombre"]}  {valor[i]["precio"]}")
                    print("")
            else:
                print("Lo sentimos, no existen pagos relacionados a su documento")


