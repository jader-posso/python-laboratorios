producto = {
    "codigo": "P001",
    "nombre": "Teclado",
    "precio": 85000.0,
    "cantidad": 4
}

nuevo_precio = float(input("Nuevo precio: "))

if nuevo_precio > 0:
    producto.update({"precio": nuevo_precio})
    print("Precio actualizado.")
else:
    print("El precio debe ser mayor que cero.")

for clave, valor in producto.items():
    print(clave, ":", valor)