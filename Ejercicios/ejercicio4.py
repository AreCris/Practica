#6. Calcular el factorial de un número


numero = 3
factorial = 1
contador = numero

while contador > 1:
    factorial *= contador
    contador -= 1

print("El factorial de", numero, "es", factorial)
