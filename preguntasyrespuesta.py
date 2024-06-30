# Lista de preguntas frecuentes y sus respuestas correspondientes
faq = [
    {
        "pregunta": "¿Cuáles son los métodos de pago aceptados?",
        "respuesta": "Aceptamos tarjetas de crédito, débito, PayPal y transferencias bancarias."
    },
    {
        "pregunta": "¿Hacen envíos internacionales?",
        "respuesta": "Sí, hacemos envíos a la mayoría de los países. Los costos y tiempos de envío varían según la ubicación."
    },
    {
        "pregunta": "¿Cuál es su política de devoluciones?",
        "respuesta": "Puede devolver los productos dentro de los 30 días posteriores a la compra para un reembolso completo. Los artículos deben estar en su estado original."
    },
    {
        "pregunta": "¿Cómo puedo rastrear mi pedido?",
        "respuesta": "Una vez que su pedido haya sido enviado, recibirá un correo electrónico con un número de seguimiento y un enlace para rastrear su paquete."
    },
    {
        "pregunta": "¿Ofrecen descuentos por compras al por mayor?",
        "respuesta": "Sí, ofrecemos descuentos para compras al por mayor. Por favor, póngase en contacto con nuestro equipo de ventas para obtener más información."
    }
]

# Función para mostrar las preguntas frecuentes
def mostrar_faq(faq):
    print("Preguntas Frecuentes:\n")
    for i, item in enumerate(faq, 1):
        print(f"{i}. {item['pregunta']}\n   Respuesta: {item['respuesta']}\n")


