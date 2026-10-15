import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "inventario.json"
RUTA_CSV = BASE_DIR / "inventario.csv"
CAMPOS = ["codigo", "nombre", "precio", "cantidad"]


def recuperar_productos():
    """Devuelve (productos, archivo_valido)."""
    try:
        with RUTA_JSON.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        print("No existe inventario.json. Se empieza con un inventario vacío.")
        return [], True
    except json.JSONDecodeError as error:
        print("ERROR: inventario.json tiene un formato inválido.")
        print(f"Detalle: línea {error.lineno}, columna {error.colno}: {error.msg}")
        print("No se guardará nada sobre el archivo hasta que lo corrijas.")
        return [], False

    print(f"Se recuperaron {len(productos)} productos de inventario.json.")
    return productos, True


def guardar_productos(productos):
    with RUTA_JSON.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)
    print("Inventario guardado en", RUTA_JSON)


def exportar_csv(productos):
    with RUTA_CSV.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(productos)
    print("Inventario exportado a", RUTA_CSV)


def mostrar_productos(productos):
    if not productos:
        print("El inventario está vacío.")
        return
    for producto in productos:
        print(f"{producto['codigo']} - {producto['nombre']} | "
              f"precio: {producto['precio']} | cantidad: {producto['cantidad']}")


def agregar_producto(productos):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Precio y cantidad deben ser numéricos. Producto no agregado.")
        return
    if precio < 0 or cantidad < 0:
        print("No se aceptan valores negativos. Producto no agregado.")
        return

    productos.append({"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado (recuerda guardar con la opción 3).")


productos, archivo_valido = recuperar_productos()

while True:
    print()
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Guardar en inventario.json")
    print("4. Exportar a inventario.csv")
    print("0. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        mostrar_productos(productos)
    elif opcion == "2":
        agregar_producto(productos)
    elif opcion == "3":
        if archivo_valido:
            guardar_productos(productos)
        else:
            print("Guardado bloqueado: inventario.json está dañado y se conserva tal cual.")
    elif opcion == "4":
        if archivo_valido:
            exportar_csv(productos)
        else:
            print("Exportación bloqueada: se exportaría un inventario vacío.")
    elif opcion == "0":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
