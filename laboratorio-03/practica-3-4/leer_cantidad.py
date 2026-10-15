while True:
    texto = input("Cantidad: ")

    try:
        cantidad = int(texto)
    except ValueError:
        print("Debes escribir un entero.\n")
        continue

    if cantidad < 0:
        print("La cantidad no puede ser negativa.\n")
        continue

    break

print(f"Cantidad aceptada: {cantidad}")

#lista compartida

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)


primero = Inventario()
segundo = Inventario()

primero.agregar("Teclado")
print(segundo.productos)
