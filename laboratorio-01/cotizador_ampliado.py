# Reto de ampliación del cotizador:
#   agrega el nombre del vendedor, un código de cotización y el costo de envío.
#
# Orden de los cálculos:
# 1. subtotal = precio unitario * cantidad
# 2. valor del descuento = subtotal * porcentaje de descuento / 100
# 3. base = subtotal - valor del descuento
# 4. valor del impuesto = base * porcentaje de impuesto / 100
# 5. total antes del envío = base + valor del impuesto
# 6. total final = total antes del envío + costo de envío (el envío va después del impuesto)

print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

codigo_cotizacion = input("Código de la cotización: ")
nombre_vendedor = input("Vendedor: ")
nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = int(input("Descuento (%): "))
porcentaje_impuesto = int(input("Impuesto (%): "))
costo_envio = float(input("Costo de envío: "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento / 100
base = subtotal - valor_descuento
valor_impuesto = base * porcentaje_impuesto / 100
total_antes_envio = base + valor_impuesto
total_final = total_antes_envio + costo_envio

print()
print("-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print("Cotización:", codigo_cotizacion)
print("Vendedor:", nombre_vendedor)
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Precio unitario: $" + str(precio_unitario))
print("Cantidad:", cantidad)
print("Subtotal: $" + str(subtotal))
print("Descuento: $" + str(valor_descuento))
print("Base: $" + str(base))
print("Impuesto: $" + str(valor_impuesto))
print("Total antes del envío: $" + str(total_antes_envio))
print("Envío: $" + str(costo_envio))
print("TOTAL: $" + str(total_final))

# Con los datos del ejemplo de la guía y un envío de 15000:
# total antes del envío = 385560
# total final = 385560 + 15000 = 400560
