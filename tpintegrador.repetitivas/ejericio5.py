# -------------------- BIENVENIDA --------------------
print("--- BIENVENIDO A LA ARENA ---")

# pedimos nombre del gladiador
nombre = input("Nombre del Gladiador: ").strip()

# validamos que solo tenga letras
while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras. Nombre: ").strip()


# -------------------- VARIABLES INICIALES --------------------
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12


# -------------------- INICIO DEL COMBATE --------------------
print("\n--- INICIO DEL COMBATE ---")


# el juego se repite mientras ambos tengan vida
while vida_jugador > 0 and vida_enemigo > 0:

    # mostramos estado actual
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # pedimos opción
    opcion = input("Opción: ")

    # validamos que sea número
    while not opcion.isdigit():
        opcion = input("Error: Ingrese un número válido: ")

    opcion = int(opcion)

    # validamos rango
    while opcion < 1 or opcion > 3:
        opcion = int(input("Error: opción inválida (1-3): "))


    # -------------------- ACCIÓN 1: ATAQUE PESADO --------------------
    if opcion == 1:

        danio = danio_jugador

        # si el enemigo tiene poca vida → golpe crítico
        if vida_enemigo < 20:
            danio = danio * 1.5

        vida_enemigo -= danio

        print(f"¡Atacaste al enemigo por {danio} de daño!")


    # -------------------- ACCIÓN 2: RÁFAGA VELOZ --------------------
    elif opcion == 2:

        print(">> ¡Inicias una ráfaga de golpes!")

        # usamos for como pide el ejercicio
        for i in range(3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")


    # -------------------- ACCIÓN 3: CURAR --------------------
    elif opcion == 3:

        if pociones > 0:
            vida_jugador += 30
            pociones -= 1

            # opcional: no pasarse de 100
            if vida_jugador > 100:
                vida_jugador = 100

            print("Te curaste 30 puntos de vida")

        else:
            print("No quedan pociones")


    # -------------------- TURNO DEL ENEMIGO --------------------
    # si el enemigo sigue vivo, ataca
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

    print("\n--- NUEVO TURNO ---")


# -------------------- FIN DEL JUEGO --------------------
if vida_jugador > 0:
    print(f"\nVICTORIA! {nombre} ha ganado la batalla")
else:
    print("\nDERROTA. Has caído en combate")