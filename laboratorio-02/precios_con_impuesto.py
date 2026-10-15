precios = [10000, 20000, 50000, 80000]
con_impuesto = []

for precio in precios:
    con_impuesto.append(precio * 1.19)

print(con_impuesto)

con_impuesto_comprension = [precio * 1.19 for precio in precios]

print(con_impuesto_comprension)

print("¿Son equivalentes?", con_impuesto == con_impuesto_comprension)