libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967},
    {"codigo": "L002", "titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "año": 1961},
    {"codigo": "L003", "titulo": "La vorágine", "autor": "José Eustasio Rivera", "año": 1924}
]

codigo_buscado = input("Código: ").strip()
encontrado = None

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        encontrado = libro
        break

if encontrado is not None:
    print("Título:", encontrado["titulo"])
    print("Autor:", encontrado["autor"])
    print("Año:", encontrado["año"])
else:
    print("No se encontró el libro.")

print()

nuevo_codigo = input("Código del nuevo libro: ").strip()
repetido = False

for libro in libros:
    if libro["codigo"] == nuevo_codigo:
        repetido = True
        break

if repetido:
    print("El código ya existe. No se agregó el libro.")
else:
    nuevo_libro = {
        "codigo": nuevo_codigo,
        "titulo": input("Título: ").strip(),
        "autor": input("Autor: ").strip(),
        "año": int(input("Año: "))
    }
    libros.append(nuevo_libro)
    print("Libro agregado.")

for libro in libros:
    print(libro["codigo"], "-", libro["titulo"], "-", libro["autor"], "-", libro["año"])