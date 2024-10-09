def mostrar_menu():
    print("Bienvenido al menú de opciones:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        print("Has seleccionado la Opción 1.")
    elif opcion == "2":
        print("Has seleccionado la Opción 2.")
    elif opcion == "3":
        print("Has seleccionado la Opción 3.")
    elif opcion == "4":
        print("Saliendo del programa.")
    else:
        print("Opción no válida, intenta de nuevo.")

def menu():
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_opcion(opcion)

menu()
