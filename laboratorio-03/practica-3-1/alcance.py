def duplicar(numero):
    resultado = numero * 2
    return resultado

doble = duplicar(5)
print(doble)


#funciones y listas

def calcular_unidades(productos):
    total = 0
    for producto in productos:
        total += producto["cantidad"]
    return total

inventario = [
    {"nombre": "Producto A", "cantidad": 10},
    {"nombre": "Producto B", "cantidad": 5}
]

print(calcular_unidades(inventario))


#funcion para los produtos agotados

def agotados(productos):
    productos_agotados = []
    for producto in productos:
        if producto["cantidad"] == 0:
            productos_agotados.append(producto["nombre"])
    return productos_agotados