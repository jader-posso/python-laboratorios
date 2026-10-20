CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

productos = []
opcion = ""

while opcion != "0":
    print()
    print("================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar por código")
    print("4. Actualizar existencias")
    print("5. Eliminar producto")
    print("6. Consultar productos sin stock")
    print("7. Resumen del inventario")
    print("0. Salir")

    opcion = input("Opción: ").strip()

    if opcion == "1":
        codigo = input("Código: ").strip()
        repetido = False

        # El código se revisa antes de pedir los demás datos, para no hacer
        # escribir todo el producto y rechazarlo al final
        for producto in productos:
            if producto["codigo"] == codigo:
                repetido = True
                break

        if codigo == "":
            print("El código no puede estar vacío.")
        elif repetido:
            print("El código ya está registrado.")
        else:
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            if nombre == "":
                print("El nombre no puede estar vacío.")
            elif categoria not in CATEGORIAS:
                print("Categoría no permitida.")
            elif precio <= 0:
                print("El precio debe ser mayor que cero.")
            elif cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                productos.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": precio,
                    "cantidad": cantidad
                })
                print("Producto registrado.")
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(producto["codigo"], "-", producto["nombre"], "-", producto["categoria"], "-", "$" + str(producto["precio"]), "-", str(producto["cantidad"]) + " unidades")
    elif opcion == "3":
        codigo_buscado = input("Código: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            print("Código:", encontrado["codigo"])
            print("Nombre:", encontrado["nombre"])
            print("Categoría:", encontrado["categoria"])
            print("Precio:", encontrado["precio"])
            print("Cantidad:", encontrado["cantidad"])
        else:
            print("No se encontró el producto.")
    elif opcion == "4":
        codigo_buscado = input("Código: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            nueva_cantidad = int(input("Nueva cantidad: "))

            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                encontrado["cantidad"] = nueva_cantidad
                print("Cantidad actualizada.")
        else:
            print("No se encontró el producto.")
    elif opcion == "5":
        codigo_buscado = input("Código: ").strip()
        encontrado = None

        for producto in productos:
            if producto["codigo"] == codigo_buscado:
                encontrado = producto
                break

        if encontrado is not None:
            productos.remove(encontrado)
            print("Producto eliminado.")
        else:
            print("No se encontró el producto.")
    elif opcion == "6":
        agotados = [
            producto["nombre"]
            for producto in productos
            if producto["cantidad"] == 0
        ]

        if len(agotados) == 0:
            print("No hay productos sin existencias.")
        else:
            print("Sin existencias:")

            for nombre in agotados:
                print("-", nombre)
    elif opcion == "7":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            unidades = 0
            valor_inventario = 0
            categorias_utilizadas = {
                producto["categoria"]
                for producto in productos
            }

            for producto in productos:
                unidades += producto["cantidad"]
                valor_inventario += producto["precio"] * producto["cantidad"]

            print("Productos:", len(productos))
            print("Unidades:", unidades)
            print("Valor del inventario: $" + str(valor_inventario))
            print("Categorías utilizadas (" + str(len(categorias_utilizadas)) + "):", ", ".join(sorted(categorias_utilizadas)))
    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")