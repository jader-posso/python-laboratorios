
# 1. Solicita los datos
cantidad = float(input("Cantidad: "))
precio_unitario = float(input("Precio unitario: "))
descuento = float(input("Descuento (%): "))
impuesto = float(input("Impuesto (%): "))

costo_envio = float(input("Costo de envío: "))
nombre_vendedor = input("Nombre del vendedor: ")
codigo_cotizacion = input("Código de la cotización: ")

# 2. Muestra los datos sin hacer cálculos
print("\n--- Datos ingresados ---")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: {precio_unitario}")
print(f"Descuento: {descuento}%")
print(f"Impuesto: {impuesto}%")
print(f"Costo de envío: {costo_envio:.2f}")
print(f"Nombre del vendedor: {nombre_vendedor}")
print(f"Código de la cotización: {codigo_cotizacion}")

# 3. Calcula únicamente el subtotal
subtotal = cantidad * precio_unitario
print(f"\nSubtotal: {subtotal:.2f}")

# 4. Comprueba el subtotal
subtotal_comprobado = cantidad * precio_unitario
if subtotal == subtotal_comprobado:
    print("Subtotal comprobado correctamente.")
else:
    print("Error en el subtotal.")

# 5. Agrega el descuento
valor_descuento = subtotal * descuento / 100
print(f"Descuento: {valor_descuento:.2f}")

# 6. Calcula la base después del descuento
base = subtotal - valor_descuento
print(f"Base después del descuento: {base:.2f}")

# 7. Agrega el impuesto
valor_impuesto = base * impuesto / 100
print(f"Impuesto: {valor_impuesto:.2f}")

# 8. Agrega el costo de envío después del impuesto
total = base + valor_impuesto + costo_envio
print(f"Costo de envío: {costo_envio:.2f}")
print(f"Total: {total:.2f}")

# 9. Organiza la salida final
print("\n--- RESUMEN FINAL ---")
print(f"Código de la cotización: {codigo_cotizacion}")
print(f"Nombre del vendedor:     {nombre_vendedor}")
print(f"Subtotal:                {subtotal:.2f}")
print(f"Descuento:              -{valor_descuento:.2f}")
print(f"Base después descuento:  {base:.2f}")
print(f"Impuesto:               +{valor_impuesto:.2f}")
print(f"Costo de envío:         +{costo_envio:.2f}")
print(f"TOTAL:                   {total:.2f}")

# Preguntas de revisión
# ¿Los nombres de las variables permiten entender qué almacenan?
# R/= Sí.

# ¿Convertiste a número los datos que necesitan operaciones?
# R/= Sí.

# ¿Los cálculos están separados en variables?
# R/= Sí.

# ¿El usuario puede cambiar todos los datos sin editar el código?
# R/= Sí, porque todos los datos se solicitan mediante input().

# ¿La salida permite entender cómo se obtuvo el total?
# R/= Sí.

# ¿Puedes explicar cada línea que escribiste?
# R/= Sí.


### Cambio principal

#La parte importante es esta:


valor_impuesto = base * impuesto / 100
total = base + valor_impuesto + costo_envio
