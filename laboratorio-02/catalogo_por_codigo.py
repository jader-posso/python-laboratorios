numeros = [1, 2, 3, 4]

cuadrados = {numero: numero ** 2 for numero in numeros}

print(cuadrados)

productos = [
    {"codigo": "P001", "nombre": "Teclado"},
    {"codigo": "P002", "nombre": "Mouse"},
    {"codigo": "P003", "nombre": "Monitor"}
]

catalogo = {producto["codigo"]: producto["nombre"] for producto in productos}

print(catalogo)