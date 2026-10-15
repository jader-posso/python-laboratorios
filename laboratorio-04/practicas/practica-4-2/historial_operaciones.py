from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_OPERACIONES = BASE_DIR / "operaciones.txt"


def registrar_operacion():
    concepto = input("Concepto: ").strip()
    if not concepto:
        print("El concepto no puede estar vacío.")
        return

    try:
        valor = float(input("Valor: "))
    except ValueError:
        print("El valor debe ser numérico. Operación no registrada.")
        return

    with open(RUTA_OPERACIONES, "a", encoding="utf-8") as archivo:
        archivo.write(f"{concepto} | {valor}\n")

    print("Operación registrada.")


def mostrar_historial():
    try:
        contenido = RUTA_OPERACIONES.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("Todavía no hay operaciones registradas.")
        return

    lineas = contenido.splitlines()
    if not lineas:
        print("Todavía no hay operaciones registradas.")
        return

    print("Historial de operaciones:")
    for numero, linea in enumerate(lineas, start=1):
        print(f"{numero}. {linea}")


while True:
    print()
    print("1. Registrar operación")
    print("2. Mostrar historial")
    print("0. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_operacion()
    elif opcion == "2":
        mostrar_historial()
    elif opcion == "0":
        print("Hasta luego.")
        break
    else:
        print("Opción no válida.")
