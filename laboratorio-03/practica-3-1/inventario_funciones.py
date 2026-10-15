#crea una lista de 3 productos e implementa mostrar_productos(productos): imprime los registros; buscar_producto(productos, codigo): devuelve el diccionario encontrado o none; valor_inventario(productos): devuelve el total de precio*cantidad; productos_sin_stock(productos): devuelve una lista de nombres; llama las cuatro funciones y explica la diferencia entre return y print, entre parametros y argumentos, y entre modificar una lista que recibes y devoolver una nueva lista.

productos = [
    {"codigo": 1, "nombre": "Producto A", "precio": 100, "cantidad": 10},
    {"codigo": 2, "nombre": "Producto B", "precio": 200, "cantidad": 0},
    {"codigo": 3, "nombre": "Producto C", "precio": 150, "cantidad": 5}
]   

def mostrar_productos(productos):
    for producto in productos:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")    

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None

def valor_inventario(productos):
    total = 0
    for producto in productos:
        total += producto["precio"] * producto["cantidad"]
    return total

def productos_sin_stock(productos):
    sin_stock = []
    for producto in productos:
        if producto["cantidad"] == 0:
            sin_stock.append(producto["nombre"])
    return sin_stock

mostrar_productos(productos)
print("Encontrado:", buscar_producto(productos, 2))
print("Valor total del inventario:", valor_inventario(productos))
print("Productos sin stock:", productos_sin_stock(productos))
print("Inexiwstente:", buscar_producto(productos, 4))

#la diferencia entre return y print es que return devuelve un valor que puede ser utilizado posteriormente en el código, mientras que print simplemente muestra un valor en la consola sin devolverlo. Los parámetros son variables definidas en la función que reciben valores cuando se llama a la función, mientras que los argumentos son los valores reales que se pasan a esos parámetros al invocar la función. Modificar una lista que recibes significa cambiar directamente los elementos de esa lista dentro de la función, afectando la lista original, mientras que devolver una nueva lista crea una copia modificada sin alterar la lista original.