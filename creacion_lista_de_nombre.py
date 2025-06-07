nombres = [""] * 10

opcion = ""
while opcion != "3":
    print("1) Agregar persona")
    print("2) Ver persona")
    print("3) Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        i = int(input("Índice: "))
        nombre = input("Nombre: ")
        nombres[i] = nombre

    if opcion == "2":
        i = int(input("Índice: "))
        if nombres[i] != "":
            print("Nombre:", nombres[i])
        else:
            print("No hay nombre en esa posición.")
            break