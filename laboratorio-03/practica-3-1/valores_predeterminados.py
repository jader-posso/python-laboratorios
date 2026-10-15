def calcular_total(precio, cantidad, descuento = 0):
    subtotal = precio * cantidad
    return subtotal - (subtotal * (descuento / 100))

print(calcular_total(50000, 2))
print(calcular_total(50000, 2, 10))
print(calcular_total(precio =50000, cantidad = 2, descuento = 20))


# costos de envio

def calcular_cobro(valor_compra, envio = 10000):
    return valor_compra + envio

print(calcular_cobro(50000))
print(calcular_cobro(50000, 15000))
print(calcular_cobro(valor_compra = 50000, envio = 20000))
