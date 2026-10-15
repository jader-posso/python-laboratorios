def calcular_subtotal(precio, cantidad):
    subtotal =  precio * cantidad
    return subtotal

resultado = calcular_subtotal(1000, 5)
print(f"El subtotal es: {resultado}")


def mostrar_total(precio, cantidad):
    print(precio*cantidad)

def obtener_total(precio, cantidad):
    return precio * cantidad

mostrar_total(1000, 5)
total = obtener_total(1000, 5)
print("Resultado reutilizable: ", total)


def anunciar():
    print("Operación iniciada")

resultado = anunciar()
print("Valor devuelto: ", resultado)  