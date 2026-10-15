from producto import Producto
from inventario import Inventario

inventario = Inventario()

print("Agregar P001:", inventario.agregar(Producto("P001", "Teclado")))
print("Agregar P002:", inventario.agregar(Producto("P002", "Mouse")))
print("Agregar P001 repetido:", inventario.agregar(Producto("P001", "Monitor")))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)


encontrado = inventario.buscar_por_codigo("P002")

if encontrado is not None:
    print("Encontrado:", encontrado.nombre)
else:
    print("Producto no registrado.")

print("Eliminar P999:", inventario.eliminar("P999"))
print("Eliminar P002:", inventario.eliminar("P002"))

for producto in inventario.listar():
    print(producto.codigo, "-", producto.nombre)
