nom_emp = "Jader"
horas_tra = 45
val_hora = 50000
APORTE = 0.04

pag_tot = horas_tra * val_hora
pag_por = pag_tot*APORTE

print("Emplado: ", nom_emp)
print("Horas trabajadas: ", horas_tra)
print("Valor de la hora: ", val_hora)
print("Pago total: ", pag_tot)
print("Porcentaje del aporte: ", pag_por, "\n")


#Leer el calculo 
unidades = 4
precio = 25000.0
descuento = 0.20

subtotal = unidades * precio
valor_descuento = subtotal * descuento
total = subtotal - valor_descuento


print("-------------------------")
print("   RESUMEN DE PAGO       ")
print("-------------------------")
print("Trabajador: ", nom_emp)
print("Horas: ", horas_tra)
print("Valor por hora: ", val_hora)
print("Pago total: ", total, "\n")


print("¿cuál es el subtotal?")
print("R/=", subtotal)
print("¿cuánto vale el descuento?")
print("R/=", valor_descuento)
print("¿qué imprimirá el programa?")
print("R/=", total)

