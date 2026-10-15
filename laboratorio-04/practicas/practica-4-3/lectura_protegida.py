import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "productos.json"


def cargar_productos():
    """Devuelve (productos, archivo_valido)."""
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        print("No existe productos.json. Se empieza con una lista vacía.")
        return [], True
    except json.JSONDecodeError as error:
        print("ERROR: productos.json tiene un formato inválido.")
        print(f"Detalle: línea {error.lineno}, columna {error.colno}: {error.msg}")
        print("El archivo no se modificará hasta que lo revises.")
        return [], False

    print(f"Se cargaron {len(productos)} productos.")
    return productos, True


def guardar_productos(productos):
    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, ensure_ascii=False, indent=4)
    print("Productos guardados.")


def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for producto in productos:
        print(producto["codigo"], "-", producto["nombre"])


def agregar_producto(productos):
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    productos.append({"codigo": codigo, "nombre": nombre})
    guardar_productos(productos)


def revisar_contenido():
    print("----- Contenido de productos.json -----")
    print(ruta.read_text(encoding="utf-8"))
    print("---------------------------------------")


productos, archivo_valido = cargar_productos()

while True:
    print()
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Revisar contenido del archivo")
    print("4. Volver a cargar el archivo")
    print("0. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        mostrar_productos(productos)
    elif opcion == "2":
        if archivo_valido:
            agregar_producto(productos)
        else:
            print("Guardado bloqueado: productos.json está dañado.")
            print("Revísalo (opción 3), corrígelo y vuelve a cargarlo (opción 4).")
    elif opcion == "3":
        if ruta.exists():
            revisar_contenido()
        else:
            print("El archivo todavía no existe.")
    elif opcion == "4":
        productos, archivo_valido = cargar_productos()
    elif opcion == "0":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
