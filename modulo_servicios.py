def registro_mantenimiento():
    while True:
        print("ingrese el numero del servicio que desea contratar | 1.limpieza, 2. Reestblecer Equipo, 3.comprar e instalar productos")
        servicio = int(input(""))
    
    
registro_mantenimiento()


def agregar_servicio(datos):
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
    
def eliminar_servicio(datos):
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


def modificar_servicio(datos):
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



def cancelar_solicitud_mantenimiento(datos):
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

def confirmar_decision():
    while True:
        decision = input("¿Esta seguro que desea realizar esta acción? (Si o No)")
        if decision.lower()=="si":
            return True
        elif decision.lower()=="no":
            return False
        else:
            print("Valor invalido")