# Producto:
#   representa un artículo y controla sus valores
#
# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta
#
# main:
#   solicita datos
#   muestra menú
#   informa los resultados

# Reto de depuración (sección 20 de la guía):
#   copia del proyecto en la que se provocaron seis errores, uno por uno.
#   El código ya está corregido; cada comentario ERROR explica la causa.

from producto import Producto, CATEGORIAS
# ERROR 5 (importación eliminada): sin esta línea main() fallaba antes de
# mostrar el menú con NameError: name 'Inventario' is not defined.
# Cada módulo debe importar lo que usa, aunque otro módulo ya lo importe.
from inventario import Inventario


def mostrar_menu():
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


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            continue

        return cantidad


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            continue

        return precio


def mostrar_producto(producto):
    # ERROR 2 (propiedad inexistente): se había escrito producto.valor.
    # Producto no tiene esa propiedad, así que al listar o buscar aparecía
    # AttributeError: 'Producto' object has no attribute 'valor'. Se usan
    # las propiedades que sí existen (precio, cantidad) o calcular_valor().
    print(
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} - "
        f"${producto.precio} - {producto.cantidad} unidades"
    )


def registrar(inventario):
    codigo = input("Código: ").strip()

    # Se avisa antes de pedir los demás datos; Inventario vuelve a
    # comprobarlo al registrar
    if inventario.buscar_por_codigo(codigo) is not None:
        print(f"Registro rechazado: el código {codigo} ya existe.")
        return

    nombre = input("Nombre: ").strip()
    print(f"Categorías permitidas: {', '.join(CATEGORIAS)}")
    categoria = input("Categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print(f"Registro rechazado: {error}")
        return

    if inventario.registrar_producto(producto):
        print("Producto registrado.")
    else:
        print(f"Registro rechazado: el código {producto.codigo} ya existe.")


def listar(inventario):
    productos = inventario.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        mostrar_producto(producto)


def buscar(inventario):
    codigo = input("Código: ").strip()
    producto = inventario.buscar_por_codigo(codigo)

    if producto is None:
        print(f"El producto {codigo} no existe.")
    else:
        mostrar_producto(producto)


def actualizar(inventario):
    codigo = input("Código: ").strip()

    if inventario.buscar_por_codigo(codigo) is None:
        print(f"El producto {codigo} no existe.")
        return

    cantidad = leer_cantidad()

    if inventario.actualizar_existencias(codigo, cantidad):
        print("Existencias actualizadas.")
    else:
        print("Actualización rechazada.")


def eliminar(inventario):
    codigo = input("Código: ").strip()

    if inventario.eliminar_producto(codigo):
        print("Producto eliminado.")
    else:
        print(f"El producto {codigo} no existe.")


def mostrar_sin_stock(inventario):
    agotados = inventario.productos_sin_stock()

    if not agotados:
        print("Todos los productos tienen existencias.")
        return

    print("Sin existencias:")
    for producto in agotados:
        print(f"- {producto.nombre}")


def mostrar_resumen(inventario):
    datos = inventario.resumen()
    categorias = ", ".join(sorted(datos["categorias"])) or "Ninguna"

    print(f"Productos registrados: {datos['productos']}")
    print(f"Unidades disponibles: {datos['unidades']}")
    print(f"Valor del inventario: ${datos['valor']}")
    print(f"Categorías utilizadas ({len(datos['categorias'])}): {categorias}")


def main():
    inventario = Inventario()
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            registrar(inventario)
        elif opcion == "2":
            listar(inventario)
        elif opcion == "3":
            buscar(inventario)
        elif opcion == "4":
            actualizar(inventario)
        elif opcion == "5":
            eliminar(inventario)
        elif opcion == "6":
            mostrar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
