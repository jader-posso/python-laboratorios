materias = ["Matemáticas", "Español", "Física", "Química", "Programación"]

for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)

materias.append("Inglés")

print()
print("Después de agregar un elemento:")

for posicion, materia in enumerate(materias, start=1):
    print(posicion, "-", materia)