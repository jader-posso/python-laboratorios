unidades_disponibles = 12
unidades_solicitadas = 8

hay_suficientes = unidades_disponibles >= unidades_solicitadas
cantidades_iguales = unidades_disponibles == unidades_solicitadas
solicito_mas = unidades_solicitadas > unidades_disponibles

print("Hay suficientes:", hay_suficientes)
print("Las cantidades son iguales:", cantidades_iguales)
print("Se solicitaron más de las disponibles:", solicito_mas)