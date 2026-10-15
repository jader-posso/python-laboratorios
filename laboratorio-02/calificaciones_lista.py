calificaciones = [4.5, 3.2, 5.0, 2.8, 4.0, 3.5]

print("Tres primeras:", calificaciones[0:3])
print("Dos últimas:", calificaciones[-2:])
print("Cantidad total:", len(calificaciones))

ordenadas = sorted(calificaciones)

print("Orden original:", calificaciones)
print("Ordenadas:", ordenadas)

nota = float(input("Nota a buscar: "))
print("Apariciones de la nota:", calificaciones.count(nota))