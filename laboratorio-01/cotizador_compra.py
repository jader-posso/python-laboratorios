
print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = int(input("Descuento (%): "))
porcentaje_impuesto = int(input("Impuesto (%): "))

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento / 100
base = subtotal - valor_descuento
valor_impuesto = base * porcentaje_impuesto / 100
total_final = base + valor_impuesto

print()
print("-----------------------------")
print("RESUMEN DE COMPRA")
print("-----------------------------")
print("Cliente:", nombre_cliente)
print("Producto:", producto)
print("Precio unitario: $" + str(precio_unitario))
print("Cantidad:", cantidad)
print("Subtotal: $" + str(subtotal))
print("Descuento: $" + str(valor_descuento))
print("Base: $" + str(base))
print("Impuesto: $" + str(valor_impuesto))
print("TOTAL: $" + str(total_final))


#Con los datos del ejemplo, los cálculos quedan:

#subtotal = 180000 * 2 = 360000`
#valor_descuento = 360000 * 10 / 100 = 36000`
#base = 360000 - 36000 = 324000`
#valor_impuesto = 324000 × 19 / 100 = 61560`
#total_final = 324000 + 61560 = 385560`

