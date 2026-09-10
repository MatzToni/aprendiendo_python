import random

# Genera un número entero al azar entre 1 y 50 (ambos inclusive)
numero_secreto = random.randint(1, 50)
intentos = random.randint(3, 10)
#print(numero_aleatorio)

print(":::::: Adivina el número secreto ::::::")

while intentos > 0:
    print(f"\nTe quedan {intentos} intento(s).")
    try:
        respuesta = int(input("Ingresa un número: "))
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")
        continue  # No consume intentos por error de formato

    if respuesta == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número secreto: {numero_secreto}")
        break
    elif respuesta > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("El número secreto es mayor.")

    intentos -= 1  # Equivalente abreviado a: intentos = intentos - 1

else:
    # Se ejecuta solo si agotó los intentos sin hacer 'break'
    print(f"\n¡Se terminaron los intentos! El número secreto era: {numero_secreto}")