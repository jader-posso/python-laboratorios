nom_prod = "Empanada"
pre_uni = 100000
cant = 2
por_desc = 0.10
IMP = 0.10

resultado = pre_uni*cant
val_desc = resultado*por_desc
semitotal = resultado-val_desc
val_imp = semitotal*IMP
total = semitotal+val_imp

print("Subtotal: ", resultado)
print("Descuento: ", val_desc)
print("Impuesto: ", val_imp)
print("Total: ", total)