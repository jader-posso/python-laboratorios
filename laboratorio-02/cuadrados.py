numeros = [1, 2, 3, 4, 5]
cuadrados = []

for numero in numeros:
    cuadrados.append(numero ** 2)

print(cuadrados)

cuadrados_comprension = [numero ** 2 for numero in numeros]

print(cuadrados_comprension)