def subtotal(precio, cant):
    return precio*cant

def descuento(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def impuesto(subtotal):
    return subtotal * 0.12