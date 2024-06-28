def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("╭───────────────────────────────────────╮")
        print("│                                       │")
        print("│            ¡Opción ingresada!         │")
        print("│                                       │")
        print("╰───────────────────────────────────────╯")
        return opc
    except ValueError:
        print("╭───────────────────────────────────────╮")
        print("│                                       │")
        print("│      Error: ¡Ingrese un número!       │")
        print("│                                       │")
        print("╰───────────────────────────────────────╯")
        return -1

