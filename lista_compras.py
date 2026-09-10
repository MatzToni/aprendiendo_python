###### Lista Interactiva ######

carrito = []

mostrar_menu = True

def agregar(lista):
    articulo = input("Ingresa un articulo para agregar: ")
    lista.append(articulo)
    return "se agrego"

def ver_lista(lista):
    if len(lista) == 0:
        print("El carrito está vacío")
    else:
        for indice, valor in enumerate(lista, 1):
            print(f"{indice}) {valor}.")

while mostrar_menu:
    valor_menu = 3
    print("Menú de opciones:")
    print("-------------------------------------------")
    print("| 1) Agregar un artículo al carrito.      |")
    print("-------------------------------------------")
    print("| 2) Ver todos los artículos del carrito. |")
    print("-------------------------------------------")
    print("| 3) Salir del programa.                  |")
    print("-------------------------------------------")

    try:
        valor_menu = int(input("Ingresa el número de la opción: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")
        continue  # No consume intentos por error de formato

    if valor_menu == 1:
        agregar(carrito)
    elif valor_menu == 2:
        ver_lista(carrito)
    else:
        break
