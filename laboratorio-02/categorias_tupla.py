categorias = ("Periféricos", "Componentes", "Accesorios", "Papelería")

for posicion, categoria in enumerate(categorias, start=1):
    print(posicion, "-", categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("La categoría pertenece a las opciones permitidas.")
else:
    print("La categoría no está permitida.")

print("Cantidad de categorías disponibles:", len(categorias))