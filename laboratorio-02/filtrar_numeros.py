numeros = [3, 8, 12, 5, 20, 7]

mayores = [numero for numero in numeros if numero >= 10]

print(mayores)

notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

aprobadas = [nota for nota in notas if nota >= 3.0]
inferiores = [nota for nota in notas if nota < 3.0]
duplicadas = [nota * 2 for nota in notas]

print(aprobadas)
print(inferiores)
print(duplicadas)

estados = ["Aprobado" if nota >= 3.0 else "No aprobado" for nota in notas]

print(estados)