# ejercicio 1 - caja de kiosco

# pedimos el nombre del cliente
nombre = input("Ingrese su nombre: ")

# validamos que el nombre no esté vacío y tenga solo letras
while not nombre.isalpha():
    nombre = input("Error, ingrese solo letras: ")


# pedimos la cantidad de productos (como texto primero)
cant_prod = input("Ingrese cantidad de productos a comprar: ")

# validamos que sea un número
while not cant_prod.isdigit():
    cant_prod = input("Error, ingrese solo números: ")

# convertimos a entero para poder usarlo en el for
cant_prod = int(cant_prod)


# inicializamos acumuladores
total_sin_desc = 0
total_con_desc = 0


# recorremos cada producto
for cont in range(cant_prod):

    # pedimos el precio del producto
    precio = input("Ingrese el precio del producto " + str(cont+1) + ": ")

    # validamos que sea número
    while not precio.isdigit():
        precio = input("Error, ingrese solo números: ")

    # convertimos a entero
    precio = int(precio)

    # sumamos al total sin descuento
    total_sin_desc += precio


    # pedimos si tiene descuento
    desc = input("¿Tiene descuento? (S/N): ")

    # validamos que sea s o n (mayúscula o minúscula)
    while desc.lower() != "s" and desc.lower() != "n":
        desc = input("Error, ingrese S o N: ")

    # aplicamos descuento si corresponde
    if desc.lower() == "s":
        precio_desc = precio * 0.9   # 10% de descuento
    else:
        precio_desc = precio

    # sumamos al total con descuento
    total_con_desc += precio_desc

    # mostramos cada producto en una línea como pide el ejercicio
    print("Producto", cont+1, "- Precio:", precio, "Descuento (S/N):", desc)


# calculamos ahorro total
ahorro = total_sin_desc - total_con_desc

# calculamos promedio
promedio = total_con_desc / cant_prod


# mostramos resultados finales
print("\nTotal sin descuentos: $", total_sin_desc)
print("Total con descuentos: $", round(total_con_desc, 2))
print("Ahorro: $", round(ahorro, 2))
print("Promedio por producto: $", round(promedio, 2))