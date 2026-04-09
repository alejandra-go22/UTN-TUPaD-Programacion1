# ejercicio 4 - escape room

# variables iniciales (no se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# contador para la regla anti-spam (forzar varias veces seguidas)
forzar_seguidas = 0


# pedimos nombre del agente
agente = input("Ingrese su nombre: ")

# validamos que sea solo letras
while not agente.isalpha():
    agente = input("Error, ingrese solo letras: ")


# el juego se ejecuta mientras tenga recursos y no haya ganado
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:

    # mostramos estado actual
    print("\nEnergía:", energia, "| Tiempo:", tiempo, "| Cerraduras:", cerraduras_abiertas)
    
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opción: ")

    # validamos que sea número
    while not opcion.isdigit():
        opcion = input("Error, ingrese un número válido: ")

    opcion = int(opcion)


    # ---------------- OPCIÓN 1: FORZAR ----------------
    if opcion == 1:

        # cada vez que fuerza, aumenta contador
        forzar_seguidas += 1

        # se descuenta energía y tiempo siempre
        energia -= 20
        tiempo -= 2

        # regla anti-spam (3 veces seguidas)
        if forzar_seguidas == 3:
            print("La cerradura se trabó.")
            alarma = True

        else:
            # si tiene poca energía hay riesgo
            if energia < 40:
                riesgo = input("Riesgo de alarma (ingrese 1-3): ")

                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    riesgo = input("Error, ingrese 1, 2 o 3: ")

                riesgo = int(riesgo)

                if riesgo == 3:
                    alarma = True
                    print("Se activó la alarma.")
                else:
                    cerraduras_abiertas += 1
                    print("Abriste una cerradura.")
            else:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")


    # ---------------- OPCIÓN 2: HACKEAR ----------------
    elif opcion == 2:

        # rompe la racha de forzar
        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        # usamos for como pide el ejercicio
        for i in range(4):
            print("Hackeando paso", i+1)
            codigo_parcial += "A"

        print("Código parcial:", codigo_parcial)

        # si el código llega a 8, abre cerradura
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Se abrió una cerradura automáticamente.")


    # ---------------- OPCIÓN 3: DESCANSAR ----------------
    elif opcion == 3:

        # rompe la racha de forzar
        forzar_seguidas = 0

        energia += 15

        # no puede superar 100
        if energia > 100:
            energia = 100

        tiempo -= 1

        # si la alarma está activa, pierde energía extra
        if alarma == True:
            energia -= 10

        print("Descansaste.")


    else:
        print("Opción inválida.")


# ---------------- FIN DEL JUEGO ----------------

# condición de victoria
if cerraduras_abiertas == 3:
    print("VICTORIA")

# condición de derrota por energía o tiempo
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")

# condición de derrota por alarma
elif alarma == True:
    print("DERROTA (alarma activada)")