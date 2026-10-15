curso = {
    "nombre": "Fundamentos de Python",
    "codigo": "CFP01",
    "temas": ["Variables", "Condicionales", "Ciclos"],
    "instructor": {
        "nombre": "María",
        "area": "Software"
    }
}

print("Nombre del curso:", curso["nombre"])
print("Segundo tema:", curso["temas"][1])
print("Nombre del instructor:", curso["instructor"]["nombre"])
print("Cantidad de temas:", len(curso["temas"]))