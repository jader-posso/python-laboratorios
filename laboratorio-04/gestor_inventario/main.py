# Producto:
#   representa un artículo y controla sus valores
#
# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta
#
# almacenamiento / reportes:
#   leen y escriben archivos (JSON y CSV)
#
# main:
#   solicita datos
#   muestra menú
#   coordina las operaciones e informa los resultados

from producto import Producto, CATEGORIAS, validar_precio, validar_cantidad
from inventario import Inventario
from almacenamiento import cargar_inventario, guardar_inventario, ErrorAlmacenamiento, RUTA_JSON
from reportes import exportar_csv, BASE_DIR

OPCIONES_QUE_MODIFICAN = ("1", "4", "5", "8", "9")


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
    print("8. Guardar inventario")
    print("9. Exportar reporte CSV")
    print("0. Salir")


def leer_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Debes escribir un número entero.")
            continue

        try:
            validar_cantidad(cantidad)
        except ValueError as error:
            print(error)
            continue

        return cantidad


def leer_precio():
    while True:
        try:
            precio = float(input("Precio: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        try:
            validar_precio(precio)
        except ValueError as error:
            print(error)
            continue

        return precio


def mostrar_producto(producto):
    print(
        f"{producto.codigo} - {producto.nombre} - {producto.categoria} - "
        f"${producto.precio} - {producto.cantidad} unidades"
    )


def guardar(inventario):
    # Devuelve True solo cuando la escritura terminó correctamente
    try:
        guardar_inventario(inventario)
    except ErrorAlmacenamiento as error:
        print(f"Error al guardar: {error}")
        print("Los cambios podrían existir solamente en memoria.")
        return False

    print("Inventario guardado.")
    return True


def registrar(inventario):
    codigo = input("Código: ").strip()

    if inventario.buscar_por_codigo(codigo) is not None:
        print(f"Registro rechazado: el código {codigo} ya existe.")
        return False

    nombre = input("Nombre: ").strip()
    print(f"Categorías permitidas: {', '.join(CATEGORIAS)}")
    categoria = input("Categoría: ").strip()
    precio = leer_precio()
    cantidad = leer_cantidad()

    try:
        producto = Producto(codigo, nombre, categoria, precio, cantidad)
    except ValueError as error:
        print(f"Registro rechazado: {error}")
        return False

    if not inventario.registrar_producto(producto):
        print(f"Registro rechazado: el código {producto.codigo} ya existe.")
        return False

    print("Producto registrado.")
    return True


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
        return False

    cantidad = leer_cantidad()

    if not inventario.actualizar_existencias(codigo, cantidad):
        print("Actualización rechazada.")
        return False

    print("Existencias actualizadas.")
    return True


def eliminar(inventario):
    codigo = input("Código: ").strip()

    if not inventario.eliminar_producto(codigo):
        print(f"El producto {codigo} no existe.")
        return False

    print("Producto eliminado.")
    return True


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

    agotados = [producto.nombre for producto in inventario.productos_sin_stock()]
    print(f"Sin existencias: {', '.join(agotados) or 'Ninguno'}")


def exportar(inventario):
    try:
        ruta = exportar_csv(inventario)
    except OSError as error:
        print(f"No se pudo exportar el reporte: {error}")
        return

    print(f"Reporte exportado: {ruta.relative_to(BASE_DIR).as_posix()}")


def iniciar():
    # Devuelve (inventario, archivo_danado)
    try:
        inventario = cargar_inventario()
    except ErrorAlmacenamiento as error:
        print("ATENCIÓN: no se pudo cargar el inventario.")
        print(error)
        print(f"Revisa o restaura el archivo: {RUTA_JSON}")
        print("Para no perder datos, el archivo no se modificará en esta sesión:")
        print("las opciones que registran, cambian, guardan o exportan quedan bloqueadas.")
        # Inventario vacío solo en memoria para las consultas; nunca se guarda
        return Inventario(), True

    cantidad = len(inventario.listar_productos())
    if cantidad:
        print(f"Se cargaron {cantidad} productos.")
    else:
        print("Inventario vacío.")
    return inventario, False


def main():
    inventario, archivo_danado = iniciar()
    cambios_sin_guardar = False
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if archivo_danado and opcion in OPCIONES_QUE_MODIFICAN:
            print("Operación bloqueada: el archivo del inventario está dañado.")
            print("Corrígelo o restáuralo y vuelve a iniciar el programa.")
            continue

        if opcion == "1":
            if registrar(inventario):
                cambios_sin_guardar = not guardar(inventario)
        elif opcion == "2":
            listar(inventario)
        elif opcion == "3":
            buscar(inventario)
        elif opcion == "4":
            if actualizar(inventario):
                cambios_sin_guardar = not guardar(inventario)
        elif opcion == "5":
            if eliminar(inventario):
                cambios_sin_guardar = not guardar(inventario)
        elif opcion == "6":
            mostrar_sin_stock(inventario)
        elif opcion == "7":
            mostrar_resumen(inventario)
        elif opcion == "8":
            cambios_sin_guardar = not guardar(inventario)
        elif opcion == "9":
            exportar(inventario)
        elif opcion == "0":
            if cambios_sin_guardar:
                print("Hay cambios sin guardar. Intentando guardar antes de salir...")
                guardar(inventario)
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
