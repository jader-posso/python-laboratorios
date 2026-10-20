# pruebas_gestor:
#   ejecuta main.py con las pruebas obligatorias (sección 16), la
#   comprobación numérica (sección 17) y la prueba de independencia
#   (sección 18), y guarda la salida de cada una en EVIDENCIA_PRUEBAS.md

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EVIDENCIA = BASE_DIR / "EVIDENCIA_PRUEBAS.md"
LINEAS_MENU = ("================================", "GESTOR DE INVENTARIO")

TECLADO = ["P001", "Teclado", "Periféricos", "85000", "4"]
MOUSE = ["P002", "Mouse", "Periféricos", "45000", "0"]
MONITOR = ["P003", "Monitor", "Componentes", "700000", "2"]


def registrar(*datos):
    return ["1", *datos]


def ejecutar(entradas, script="main.py"):
    proceso = subprocess.run(
        [sys.executable, "-X", "utf8", script],
        input="\n".join(entradas) + "\n",
        cwd=BASE_DIR, capture_output=True, text=True, encoding="utf-8", timeout=30,
    )
    # Se omiten las líneas del menú para que la evidencia sea legible
    lineas = [
        linea for linea in (proceso.stdout + proceso.stderr).splitlines()
        if linea.strip() and linea.strip() not in LINEAS_MENU and linea[:2] not in
        ("1.", "2.", "3.", "4.", "5.", "6.", "7.", "0.")
    ]
    return "\n".join(lineas)


PRUEBAS = [
    ("Iniciar inventario vacío", "Listado vacío y resumen en cero", ["2", "7", "0"]),
    ("Registrar P001", "Registro aceptado", [*registrar(*TECLADO), "2", "0"]),
    ("Registrar nuevamente P001", "Registro rechazado",
     [*registrar(*TECLADO), *registrar("P001"), "2", "0"]),
    ("Registrar código o nombre vacío", "Registro rechazado",
     [*registrar("   ", "Cable", "Accesorios", "1000", "1"),
      *registrar("P004", "", "Accesorios", "1000", "1"), "2", "0"]),
    ("Categoría no permitida", "Registro rechazado",
     [*registrar("P004", "Silla", "Muebles", "1000", "1"), "2", "0"]),
    ("Precio cero o negativo", "Registro rechazado: se vuelve a pedir el precio",
     [*registrar("P004", "Cable", "Accesorios", "0", "-500", "1000", "1"), "2", "0"]),
    ("Cantidad negativa", "Registro rechazado: se vuelve a pedir la cantidad",
     [*registrar("P004", "Cable", "Accesorios", "1000", "-2", "1"), "2", "0"]),
    ("Cantidad cero", "Producto válido y sin existencias", [*registrar(*MOUSE), "6", "0"]),
    ("Buscar P001", "Mostrar su información", [*registrar(*TECLADO), "3", "P001", "0"]),
    ("Buscar P999", "Informar que no existe", ["3", "P999", "0"]),
    ("Actualizar a 10 unidades", "Modificar solo la cantidad",
     [*registrar(*TECLADO), "4", "P001", "10", "3", "P001", "0"]),
    ("Actualizar a -3 unidades", "Rechazar, conservar el dato anterior",
     [*registrar(*TECLADO), "4", "P001", "-3", "4", "3", "P001", "0"]),
    ("Eliminar producto existente", "Quitar el registro",
     [*registrar(*TECLADO), "5", "P001", "2", "0"]),
    ("Eliminar código inexistente", "Informar sin fallar", ["5", "P999", "2", "0"]),
    ("Ingresar texto en un campo numérico", "Mensaje y nueva oportunidad",
     [*registrar("P004", "Cable", "Accesorios", "abc", "1000", "dos", "1"), "2", "0"]),
    ("Consultar resumen", "Totales coherentes",
     [*registrar(*TECLADO), *registrar(*MOUSE), "7", "0"]),
    ("Salir", "Terminar el ciclo", ["9", "0"]),
]


def escribir(archivo, titulo, esperado, entradas, salida):
    archivo.write(f"## {titulo}\n\n")
    archivo.write(f"Esperado: {esperado}.\n\n")
    if entradas:
        archivo.write("Entradas: `" + " | ".join(entradas) + "`\n\n")
    archivo.write("```text\n" + salida + "\n```\n\n")


def main():
    with EVIDENCIA.open("w", encoding="utf-8") as archivo:
        archivo.write("# Evidencia de pruebas del gestor de inventario orientado a objetos\n\n")
        archivo.write("Generado con `python pruebas_gestor.py`. Cada prueba inicia `main.py` desde cero ")
        archivo.write("con las entradas indicadas.\n")
        archivo.write("Las líneas del menú se omiten; `Opción:` indica cada vuelta del menú.\n\n")

        for numero, (titulo, esperado, entradas) in enumerate(PRUEBAS, start=1):
            escribir(archivo, f"{numero}. {titulo}", esperado, entradas, ejecutar(entradas))

        entradas = [*registrar(*TECLADO), *registrar(*MOUSE), *registrar(*MONITOR),
                    "6", "7", "4", "P002", "5", "7", "0"]
        escribir(
            archivo, "Comprobación numérica",
            "3 productos, 6 unidades, $1740000.0, 2 categorías y Mouse sin stock; "
            "después de actualizar P002 a 5: 11 unidades y $1965000.0 "
            "(1740000 + 45000 × 5 = 1965000)",
            entradas, ejecutar(entradas),
        )

        escribir(
            archivo, "Prueba de independencia",
            "Primero: 1 y Segundo: 0, porque cada Inventario tiene su propia lista",
            None, ejecutar([], "pruebas_independencia.py"),
        )

    print(f"{len(PRUEBAS) + 2} pruebas guardadas en {EVIDENCIA.name}")


if __name__ == "__main__":
    main()
