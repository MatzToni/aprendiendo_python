contador = 3

while contador > 0:
    print(f"Despegue en: {contador}")
    contador = contador - 1  # Crucial: si no modificas la variable, el bucle será infinito

print("¡Despegue!")