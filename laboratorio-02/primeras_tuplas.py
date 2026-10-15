coordenadas = (4.6097, -74.0817)
meses = ("enero", "febrero", "marzo")

print(coordenadas)
print(coordenadas[0])
print(meses[-1])
print(len(meses))

colores_lista = ["rojo", "verde", "azul"]
colores_lista[0] = "amarillo"

print(colores_lista)

colores_tupla = ("rojo", "verde", "azul")
print(colores_tupla)

valor = (10)
tupla = (10,)

print(type(valor))
print(type(tupla))

producto = ("P001", "Teclado", 85000)

codigo, nombre, precio = producto

print("Código:", codigo)
print("Nombre:", nombre)
print("Precio:", precio)

categorias = ("Periféricos", "Componentes", "Accesorios")

for categoria in categorias:
    print(categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")