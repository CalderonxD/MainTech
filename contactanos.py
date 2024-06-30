# aqui es toda la informacion de la empresa 
empresa = {
    "nombre": "MainTech",
    "direccion": "Zona Franca Santander, Zenith, Anillo Vial #piso 6, Bucaramanga, El Caucho, Floridablanca, Santander",
    "telefono": "317-7398030",
    "email": "cristianfernando1412@gmail.com"
}
# y esta es la funcion para poder mostrar la informacion del contacto
def mostrar_informacion_contacto(empresa):
    print(f"Nombre de la empresa: {empresa['nombre']}")
    print(f"Dirección: {empresa['direccion']}")
    print(f"Teléfono: {empresa['telefono']}")
    print(f"Email: {empresa['email']}")

