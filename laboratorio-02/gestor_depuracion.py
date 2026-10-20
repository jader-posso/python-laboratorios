# Reto de depuración de la práctica 2.9:
#   copia del gestor en la que se provocaron cinco errores a propósito.
#   El código ya está corregido; cada comentario ERROR explica la causa.

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

# ERROR 1 (lista reiniciada): productos = [] se había escrito dentro del while.
# Cada vuelta del menú creaba una lista nueva, así que lo registrado se perdía
# y "Listar" siempre decía que no había productos. La lista se crea una sola
# vez, antes del ciclo.
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

        # ERROR 3 (registros duplicados): faltaba este recorrido y la condición
        # "elif repetido". Registrar P001 dos veces agregaba dos diccionarios
        # con el mismo código y "Buscar" solo encontraba el primero.
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
            # ERROR 4 (cantidad negativa aceptada): las dos reglas se habían unido
            # en  elif precio <= 0 and cantidad < 0:  y solo se rechazaba el
            # producto cuando precio Y cantidad estaban mal. Con precio 500 y
            # cantidad -2 se registraba. Cada regla va en su propia condición.
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
            # ERROR 2 (clave inexistente): se había escrito encontrado["valor"].
            # Ese diccionario no tiene la clave "valor", así que al buscar un
            # producto existente el programa se detenía con KeyError: 'valor'.
            # Se usa la clave real, "precio".
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
                # ERROR 5 (total mal calculado): se sumaba solo producto["precio"].
                # Con P001, P002 y P003 el valor daba $830000.0 (85000 + 45000 +
                # 700000) en lugar de $1740000.0. Hay que multiplicar cada precio
                # por su cantidad antes de acumular.
                valor_inventario += producto["precio"] * producto["cantidad"]

            print("Productos:", len(productos))
            print("Unidades:", unidades)
            print("Valor del inventario: $" + str(valor_inventario))
            print("Categorías utilizadas (" + str(len(categorias_utilizadas)) + "):", ", ".join(sorted(categorias_utilizadas)))
    elif opcion == "0":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")