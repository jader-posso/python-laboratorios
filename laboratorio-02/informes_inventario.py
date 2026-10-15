productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

agotados = [producto["nombre"] for producto in productos if producto["cantidad"] == 0]
precios_altos = [producto["nombre"] for producto in productos if producto["precio"] > 100000]
cantidades = {producto["cantidad"] for producto in productos}
nombre_precio = {producto["nombre"]: producto["precio"] for producto in productos}

print("Productos sin existencias:", agotados)
print("Precio superior a $100000:", precios_altos)
print("Valores de cantidad:", cantidades)
print("Nombre y precio:", nombre_precio)

disponibles = [producto["nombre"] for producto in productos if producto["cantidad"] > 0]

print("Disponibles:", disponibles)

valores = [producto["precio"] * producto["cantidad"] for producto in productos]

print("Valor total:", sum(valores))

grupos = [[1, 2], [3, 4], [5, 6]]

numeros = [numero for grupo in grupos for numero in grupo]

print(numeros)

cuadrados = (numero ** 2 for numero in range(1, 5))

print(type(cuadrados))
print(list(cuadrados))

tupla_cuadrados = tuple(numero ** 2 for numero in range(1, 5))
print(tupla_cuadrados)