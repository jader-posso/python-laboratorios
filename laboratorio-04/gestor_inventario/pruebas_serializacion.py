from producto import Producto

original = Producto("P001", "Teclado", "Periféricos", 85000, 4)

datos = original.a_diccionario()
reconstruido = Producto.desde_diccionario(datos)

print("Original:     ", original.a_diccionario())
print("Diccionario:  ", datos)
print("Reconstruido: ", reconstruido.a_diccionario())
print("¿Mismos datos?", original.a_diccionario() == reconstruido.a_diccionario())
print("¿Mismo objeto?", original is reconstruido)
