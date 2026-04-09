# ejercicio 3 - agenda de turnos (sin listas)

# inicializamos espacios
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


# pedimos nombre del operador
operador = input("Ingrese su nombre: ")

# validamos nombre
while not operador.isalpha():
    operador = input("Error, ingrese solo letras: ")


# menú infinito (se corta con break)
while True:

    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen")
    print("5) Salir")

    opcion = input("Opción: ")

    # validamos número
    if not opcion.isdigit():
        print("Error, ingrese un número válido.")
        continue

    opcion = int(opcion)

    # validamos rango
    if opcion < 1 or opcion > 5:
        print("Error, opción fuera de rango.")
        continue


    # ---------------- RESERVAR ----------------
    if opcion == 1:

        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            dia = input("Error, ingrese 1 o 2: ")

        dia = int(dia)

        nombre = input("Ingrese nombre del paciente: ")

        while not nombre.isalpha():
            nombre = input("Error, ingrese solo letras: ")


        if dia == 1:

            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Error, nombre repetido.")

            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay más turnos para lunes.")

        else:

            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error, nombre repetido.")

            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay más turnos para martes.")


    # ---------------- CANCELAR ----------------
    elif opcion == 2:

        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            dia = input("Error, ingrese 1 o 2: ")

        dia = int(dia)

        nombre = input("Ingrese nombre a cancelar: ")

        while not nombre.isalpha():
            nombre = input("Error, ingrese solo letras: ")


        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No se encontró ese nombre.")

        else:
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No se encontró ese nombre.")


    # ---------------- VER AGENDA ----------------
    elif opcion == 3:

        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            dia = input("Error, ingrese 1 o 2: ")

        dia = int(dia)

        if dia == 1:
            print("Lunes:")

            if lunes1 == "":
                print("1: Libre")
            else:
                print("1:", lunes1)

            if lunes2 == "":
                print("2: Libre")
            else:
                print("2:", lunes2)

            if lunes3 == "":
                print("3: Libre")
            else:
                print("3:", lunes3)

            if lunes4 == "":
                print("4: Libre")
            else:
                print("4:", lunes4)

        else:
            print("Martes:")

            if martes1 == "":
                print("1: Libre")
            else:
                print("1:", martes1)

            if martes2 == "":
                print("2: Libre")
            else:
                print("2:", martes2)

            if martes3 == "":
                print("3: Libre")
            else:
                print("3:", martes3)


    # ---------------- RESUMEN ----------------
    elif opcion == 4:

        ocupados = 0

        if lunes1 != "": ocupados += 1
        if lunes2 != "": ocupados += 1
        if lunes3 != "": ocupados += 1
        if lunes4 != "": ocupados += 1
        if martes1 != "": ocupados += 1
        if martes2 != "": ocupados += 1
        if martes3 != "": ocupados += 1

        print("Turnos ocupados:", ocupados)


    # ---------------- SALIR ----------------
    elif opcion == 5:
        print("Sistema cerrado.")
        break