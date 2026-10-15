productos = [
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Disco", "categoria": "Componentes"}
]

categorias = {producto["categoria"] for producto in productos}

print(categorias)

categorias_lista = ["Periféricos", "Accesorios", "Periféricos", "Componentes"]
unicas = {categoria for categoria in categorias_lista}

print(unicas)