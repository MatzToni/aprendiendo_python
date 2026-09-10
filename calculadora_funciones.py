#función suma
def sumar(a, b):
    return a + b

#función resta
def restar(a, b):
    return a - b

#función multiplica
def multiplicar(a, b):
    return a * b

#función divide
def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

# Ejemplo de prueba al final del archivo:
print("Suma:", sumar(10, 5))
print("Suma:", restar(10, 5))
print("Suma:", multiplicar(10, 5))
print("Suma:", dividir(10, 5))
print("División por cero:", dividir(10, 0))