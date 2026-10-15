def calcular_subtotal(precio, cantidad):
    return precio * cantidad
    pass
def calcular_descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)
    pass
def calcular_impuesto(base, porcentaje):
    return base * (porcentaje / 100)
    pass

precio = 100000
cantidad = 2
descuento = 10
impuesto = 19

subtotal =  calcular_subtotal(precio, cantidad)
Descuento = calcular_descuento(subtotal, descuento)
Base = subtotal - Descuento
Impuesto = calcular_impuesto(Base, impuesto)
Total = Base + Impuesto

print(f"Subtotal: {subtotal}")
print(f"Descuento: {Descuento}")
print(f"Base: {Base}")
print(f"Impuesto: {Impuesto}")
print(f"Total: {Total}")