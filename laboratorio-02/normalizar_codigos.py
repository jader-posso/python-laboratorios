nombres = ["  ana ", "CARLOS", " Laura ", ""]

normalizados = [
    nombre.strip().title()
    for nombre in nombres
    if nombre.strip() != ""
]

print(normalizados)

codigos = [" p001 ", "P002", "", " p003", "  "]

codigos_normalizados = [
    codigo.strip().upper()
    for codigo in codigos
    if codigo.strip() != ""
]

print(codigos_normalizados)