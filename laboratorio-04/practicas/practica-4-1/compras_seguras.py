cantidad_compras = 0
total = 0.0

while True:
    try:
        importe = float(input("Importe de la compra (0 para terminar): "))
    except ValueError:
        print("Entrada no numérica. Intenta de nuevo.")
        continue

    if importe == 0:
        break
    elif importe < 0:
        print("No se aceptan importes negativos.")
    else:
        cantidad_compras += 1
        total += importe
        print("Compra registrada:", importe)

print("Compras aceptadas:", cantidad_compras)
print("Suma acumulada:", total)
