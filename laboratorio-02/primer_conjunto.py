categorias = {"Periféricos", "Accesorios", "Componentes", "Periféricos"}

print(categorias)
print("Cantidad:", len(categorias))

vacio = set()
otro = {}

print(type(vacio))
print(type(otro))

ciudades = ["Bogotá", "Cali", "Bogotá", "Medellín", "Cali"]
unicas = set(ciudades)

print("Total de registros:", len(ciudades))
print("Ciudades diferentes:", len(unicas))
print(unicas)

lista_unicas = list(unicas)
print(lista_unicas)

categorias.add("Componentes")
categorias.update(["Papelería", "Accesorios"])

print(categorias)

categorias.discard("Papelería")
print(categorias)