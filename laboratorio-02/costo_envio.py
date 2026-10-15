valor_compra = float(input("Valor de la compra: "))

if valor_compra >= 200000:
    costo_envio = 0
elif valor_compra >= 100000:
    costo_envio = 10000
else:
    costo_envio = 18000

total = valor_compra + costo_envio

print("Valor de la compra:", valor_compra)
print("Costo de envío:", costo_envio)
print("Total a pagar:", total)