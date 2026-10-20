# Reto de depuración:
#   copia del cotizador en la que se provocaron tres errores a propósito.
#   El código ya está corregido; cada comentario ERROR explica qué pasaba.

print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

nombre_cliente = input("Nombre del cliente: ")
producto = input("Producto: ")

# ERROR 1 (sintaxis): se escribió  precio_unitario = float(input("Precio unitario: ")
# sin el último paréntesis. Python no ejecuta ninguna línea y muestra
# SyntaxError: '(' was never closed. Se corrigió cerrando el paréntesis.
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
porcentaje_descuento = int(input("Descuento (%): "))
porcentaje_impuesto = int(input("Impuesto (%): "))

subtotal = precio_unitario * cantidad

# ERROR 2 (nombre inexistente): se escribió  subtotal * porcentaje_descuentos / 100
# con una "s" de más. El programa pedía todos los datos y se detenía con
# NameError: name 'porcentaje_descuentos' is not defined. Se corrigió usando
# el nombre exacto con el que se creó la variable.
valor_descuento = subtotal * porcentaje_descuento / 100

# ERROR 3 (cálculo incorrecto): se escribió  base = subtotal - porcentaje_descuento
# El programa no fallaba, pero restaba el porcentaje (10) en lugar del valor
# del descuento (36000): con el ejemplo de la guía la base daba 359990.0 en vez
# de 324000.0. Se corrigió restando valor_descuento y comparando con el
# cálculo manual.
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
