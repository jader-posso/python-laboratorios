producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4,
    "categoria": "Periféricos"
}

print(producto)
print(producto["nombre"])
print(producto["precio"])

producto["cantidad"] = 8
producto["activo"] = True

print(producto)

print(producto.get("marca"))
print(producto.get("marca", "Sin marca"))

for clave in producto:
    print(clave)

for valor in producto.values():
    print(valor)

for clave, valor in producto.items():
    print(clave, ":", valor)