# ejercicio 2 - acceso al campus

# definimos usuario y clave correctos
usuario_correcto = "alumno"
clave_correcta = "python123"

# contador de intentos
intentos = 0

# usamos while para permitir hasta 3 intentos
while intentos < 3:

    print("Intento", intentos+1, "/3")

    # pedimos usuario y clave
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    # verificamos si coinciden
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        break  # salimos del while si está bien

    else:
        print("Error: credenciales inválidas.")
        intentos += 1  # sumamos intento

# si se usaron los 3 intentos
if intentos == 3:
    print("Cuenta bloqueada.")

else:
    # mostramos menú (esto solo pasa si ingresó bien)

    opcion = ""

    # usamos while para repetir el menú
    while opcion != "4":

        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")

        opcion = input("Opción: ")

        # validamos que sea número
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        # convertimos a int
        opcion = int(opcion)

        # validamos rango
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        # opción 1
        if opcion == 1:
            print("Inscripto")

        # opción 2 - cambiar clave
        elif opcion == 2:
            nueva = input("Ingrese nueva clave: ")
            confirmar = input("Confirme la clave: ")

            # validamos largo mínimo
            if len(nueva) < 6:
                print("Error: mínimo 6 caracteres.")

            elif nueva != confirmar:
                print("Error: no coinciden.")

            else:
                clave_correcta = nueva
                print("Clave cambiada correctamente.")

        # opción 3
        elif opcion == 3:
            print("Seguí así, vas muy bien 💪")

        # opción 4
        elif opcion == 4:
            print("Saliendo del sistema...")