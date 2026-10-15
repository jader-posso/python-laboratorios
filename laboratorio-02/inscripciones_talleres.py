python = {"Ana", "Carlos", "Laura", "Sara"}
java = {"Laura", "Sara", "David", "Pablo"}

print("Inscritos en al menos un taller:", python | java)
print("Inscritos en ambos:", python & java)
print("Inscritos únicamente en Python:", python - java)
print("Inscritos únicamente en Java:", java - python)
print("Inscritos en uno solo de los talleres:", python ^ java)