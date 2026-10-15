total = 0
depositos = 0
deposito = float(input("Depósito (0 para terminar): "))

while deposito != 0:
    if deposito > 0:
        total += deposito
        depositos += 1
        print("Ahorro acumulado:", total)
    else:
        print("El depósito debe ser positivo.")

    print()
    deposito = float(input("Depósito (0 para terminar): "))

print("Depósitos válidos:", depositos)
print("Total ahorrado:", total)