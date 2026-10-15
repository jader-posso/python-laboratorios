grupo_hoy = ["Ana", "Luis", "Ana", "Sara", "Carlos"]
grupo_manana = ["Sara", "David", "Luis", "Laura", "Luis"]

participantes = set(grupo_hoy + grupo_manana)

print("Registros del día 1:", len(grupo_hoy))
print("Registros del día 2:", len(grupo_manana))
print("Personas diferentes:", len(participantes))
print(participantes)

participantes.add("Pablo")
participantes.discard("Carlos")

print("Después de agregar y eliminar:", participantes)

grupo_a = {"Ana", "Carlos", "Laura", "Sara"}
grupo_b = {"Laura", "Sara", "David", "Pablo"}

print("Unión:", grupo_a | grupo_b)
print("Intersección:", grupo_a & grupo_b)
print("Solo A:", grupo_a - grupo_b)
print("Diferencia simétrica:", grupo_a ^ grupo_b)