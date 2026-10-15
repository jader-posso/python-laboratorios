productos = ["Teclado", "Mouse"]
nombre = input("Producto nuevo: ").strip()

if nombre == "":
    print("No puede registrarse un nombre vacío.")
elif nombre in productos:
    print("El producto ya está registrado.")
else:
    productos.append(nombre)
    print("Producto agregado.")

print("Lista:", productos)