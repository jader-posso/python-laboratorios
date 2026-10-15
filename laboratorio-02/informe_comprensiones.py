ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

mayores = [venta["producto"] for venta in ventas if venta["total"] > 100000]

print("Productos con ventas superiores a $100000:", mayores)

con_for = []

for venta in ventas:
    if venta["total"] > 100000:
        con_for.append(venta["producto"])

print("Con ciclo for:", con_for)

categorias = {venta["categoria"] for venta in ventas}

print("Categorías diferentes:", categorias)

relacion = {venta["producto"]: venta["total"] for venta in ventas}

print("Producto y valor de venta:", relacion)

valores = [venta["total"] for venta in ventas]

print("Suma de todas las ventas:", sum(valores))