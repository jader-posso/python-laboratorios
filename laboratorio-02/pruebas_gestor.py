# pruebas_gestor:
#   ejecuta gestor_inventario.py con las pruebas obligatorias y la
#   comprobación numérica de la práctica 2.9, y guarda la salida de cada
#   prueba en EVIDENCIA_PRUEBAS.md

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


def ejecutar(entradas):
    proceso = subprocess.run(
        [sys.executable, "-X", "utf8", "gestor_inventario.py"],
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
    ("Listar sin productos", "Mostrar mensaje de inventario vacío", ["2", "0"]),
    ("Registrar P001", "Se agrega", [*registrar(*TECLADO), "2", "0"]),
    ("Registrar P001 nuevamente", "Rechazar código repetido",
     [*registrar(*TECLADO), *registrar("P001"), "2", "0"]),
    ("Registrar código vacío", "Rechazar", [*registrar("   "), "2", "0"]),
    ("Registrar nombre vacío o solo espacios", "Rechazar",
     [*registrar("P004", "   ", "Accesorios", "1000", "1"), "2", "0"]),
    ("Registrar categoría fuera de la tupla", "Rechazar",
     [*registrar("P004", "Silla", "Muebles", "1000", "1"), "2", "0"]),
    ("Registrar precio negativo", "Rechazar",
     [*registrar("P004", "Cable", "Accesorios", "-500", "1"), "2", "0"]),
    ("Registrar cantidad negativa", "Rechazar",
     [*registrar("P004", "Cable", "Accesorios", "500", "-2"), "2", "0"]),
    ("Registrar cantidad cero", "Aceptar como producto sin stock",
     [*registrar(*MOUSE), "6", "0"]),
    ("Buscar P001", "Mostrar su registro", [*registrar(*TECLADO), "3", "P001", "0"]),
    ("Buscar código desconocido", "Informar que no existe", ["3", "P999", "0"]),
    ("Actualizar a 10 unidades", "Cambiar solamente la cantidad",
     [*registrar(*TECLADO), "4", "P001", "10", "3", "P001", "0"]),
    ("Actualizar a -3 unidades", "Conservar la cantidad anterior",
     [*registrar(*TECLADO), "4", "P001", "-3", "3", "P001", "0"]),
    ("Eliminar un producto existente", "Borrar el registro",
     [*registrar(*TECLADO), "5", "P001", "2", "0"]),
    ("Eliminar código inexistente", "No fallar", ["5", "P999", "2", "0"]),
    ("Consultar resumen", "Reflejar los datos actuales",
     [*registrar(*TECLADO), "7", "4", "P001", "1", "7", "0"]),
    ("Salir", "Finalizar el ciclo", ["9", "0"]),
]


def main():
    with EVIDENCIA.open("w", encoding="utf-8") as archivo:
        archivo.write("# Evidencia de pruebas del gestor de inventario\n\n")
        archivo.write("Generado con `python pruebas_gestor.py`. Cada prueba inicia el programa desde cero ")
        archivo.write("con las entradas indicadas.\n")
        archivo.write("Las líneas del menú se omiten; `Opción:` indica cada vuelta del menú.\n\n")

        for numero, (titulo, esperado, entradas) in enumerate(PRUEBAS, start=1):
            archivo.write(f"## {numero}. {titulo}\n\n")
            archivo.write(f"Esperado: {esperado}.\n\n")
            archivo.write("Entradas: `" + " | ".join(entradas) + "`\n\n")
            archivo.write("```text\n" + ejecutar(entradas) + "\n```\n\n")

        archivo.write("## Comprobación numérica\n\n")
        archivo.write("Esperado: 3 productos, 6 unidades, valor de $1.740.000, 2 categorías y P002 (Mouse) sin stock.\n\n")
        archivo.write("Cálculo manual: 85000 × 4 + 45000 × 0 + 700000 × 2 = 340000 + 0 + 1400000 = 1740000.\n\n")
        entradas = [*registrar(*TECLADO), *registrar(*MOUSE), *registrar(*MONITOR), "6", "7", "0"]
        archivo.write("Entradas: `" + " | ".join(entradas) + "`\n\n")
        archivo.write("```text\n" + ejecutar(entradas) + "\n```\n")

    print(f"{len(PRUEBAS) + 1} pruebas guardadas en {EVIDENCIA.name}")


if __name__ == "__main__":
    main()
