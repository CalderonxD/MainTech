from datetime import datetime
import json

def registrar_compra(id_solicitud, cliente, valor_total, productos):
    try:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historial_compra = {
            "fecha": fecha_actual,
            "id_solicitud": id_solicitud,
            "cliente": cliente,
            "valor_total": valor_total,
            "productos": productos
        }
        
        nombre_archivo = "historial_ventas.json"
        try:
            with open(nombre_archivo, "r") as archivo:
                historial_ventas = json.load(archivo)
        except FileNotFoundError:
            historial_ventas = {"compras": []}
        
        historial_ventas["compras"].append(historial_compra)
        
        with open(nombre_archivo, "w") as archivo:
            json.dump(historial_ventas, archivo, indent=4) 

        print("La compra se ha registrado correctamente en el historial de ventas.")
    except Exception as e:
        print(f"Ocurrió un error al registrar la compra: {str(e)}")



def registrar_historial_limpieza(id_solicitud, cliente, valor_total):
    historial = {
        "id_solicitud": id_solicitud,
        "cliente": cliente,
        "valor_total": 30000,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("historial_ventas.json", "r+") as archivo:
            historial_ventas = json.load(archivo)
            if not isinstance(historial_ventas, dict):
                historial_ventas = {}

            # Verificar y actualizar la estructura de historial_ventas
            if "limpieza" not in historial_ventas:
                historial_ventas["limpieza"] = []

            historial_ventas["limpieza"].append(historial)  # Agrega el nuevo registro al historial de limpieza

            archivo.seek(0)  # Mueve el cursor al inicio del archivo
            json.dump(historial_ventas, archivo, indent=4)
            archivo.truncate()  # Trunca cualquier contenido restante si es necesario

    except FileNotFoundError:
        historial_ventas = {"limpieza": [historial]}  # Crea un nuevo archivo si no existe

    except json.JSONDecodeError:
        historial_ventas = {"limpieza": [historial]}  # Crea un nuevo archivo si hay un error de decodificación JSON

    except Exception as e:
        print(f"Error: {e}")


import json
from datetime import datetime

def registrar_historial_restablecer(id_solicitud, cliente, valor_total):
    historial = {
        "id_solicitud": id_solicitud,
        "cliente": cliente,
        "valor_total": 20000,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("historial_ventas.json", "r+") as archivo:
            historial_ventas = json.load(archivo)
            if not isinstance(historial_ventas, dict):
                historial_ventas = {}

            # Verificar y actualizar la estructura de historial_ventas
            if "reestablecer" not in historial_ventas:
                historial_ventas["reestablecer"] = []

            historial_ventas["reestablecer"].append(historial)  # Agrega el nuevo registro al historial de reestablecer

            archivo.seek(0)  # Mueve el cursor al inicio del archivo
            json.dump(historial_ventas, archivo, indent=4)
            archivo.truncate()  # Trunca cualquier contenido restante si es necesario

    except FileNotFoundError:
        historial_ventas = {"reestablecer": [historial]}  # Crea un nuevo archivo si no existe

    except json.JSONDecodeError:
        historial_ventas = {"reestablecer": [historial]}  # Crea un nuevo archivo si hay un error de decodificación JSON

    except Exception as e:
        print(f"Error: {e}")





def mostrar_ventas_ganancias(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for servicio, compras in data.items():
            print(f"--- {servicio.capitalize()} ---")
            for compra in compras:
                print(f"Fecha: {compra.get('fecha', 'No disponible')}")
                print(f"ID Solicitud: {compra.get('id_solicitud', 'No disponible')}")
                print(f"Cliente: {compra.get('cliente', 'No disponible')}")
                
                # Manejar el caso de valor_total vacío o no numérico
                valor_total = compra.get('valor_total', '')
                if isinstance(valor_total, (int, float)):
                    print(f"Valor Total: ${valor_total:,}")
                elif valor_total.isdigit():
                    print(f"Valor Total: ${int(valor_total):,}")
                else:
                    print("Valor Total: No disponible")
                
                print("Productos:")
                for producto in compra.get('productos', []):
                    print(f"- Nombre: {producto.get('nombre', 'No disponible')}")
                    print(f"  Núcleos/Hilos: {producto.get('nucleos/hilos', 'No disponible')}")
                    print(f"  Velocidad: {producto.get('velocidad', 'No disponible')}")
                    print(f"  Precio: ${producto.get('precio', 'No disponible'):,}")
                print()

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'")
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el archivo JSON '{filename}'")

