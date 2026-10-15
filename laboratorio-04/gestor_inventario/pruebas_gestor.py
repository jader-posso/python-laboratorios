# pruebas_gestor:
#   ejecuta las pruebas obligatorias del laboratorio sobre una COPIA temporal
#   del proyecto (nunca toca datos/productos.json real) y guarda la salida
#   de cada prueba en EVIDENCIA_PRUEBAS.md

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EVIDENCIA = BASE_DIR / "EVIDENCIA_PRUEBAS.md"
LINEAS_MENU = ("================================", "GESTOR DE INVENTARIO")

TECLADO = ["P001", "Teclado", "Periféricos", "85000", "4"]
MOUSE = ["P002", "Mouse", "Periféricos", "45000", "0"]
MONITOR = ["P003", "Monitor", "Componentes", "700000", "2"]


def registrar(*datos):
    return ["1", *datos]


class Pruebas:
    def __init__(self, carpeta):
        self.carpeta = carpeta
        self.json = carpeta / "datos" / "productos.json"
        self.csv = carpeta / "reportes" / "inventario.csv"
        self.resultados = []

    def ejecutar(self, titulo, entradas, script="main.py"):
        proceso = subprocess.run(
            [sys.executable, "-X", "utf8", script],
            input="\n".join(entradas) + "\n",
            cwd=self.carpeta, capture_output=True, text=True, encoding="utf-8", timeout=30,
        )
        # Se omiten las líneas del menú para que la evidencia sea legible
        lineas = [
            linea for linea in (proceso.stdout + proceso.stderr).splitlines()
            if linea.strip() and linea.strip() not in LINEAS_MENU and linea[:2] not in
            ("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "0.")
        ]
        self.resultados.append((titulo, entradas, "\n".join(lineas)))

    def anotar(self, titulo, contenido):
        self.resultados.append((titulo, None, contenido))

    def contenido(self, ruta):
        return ruta.read_text(encoding="utf-8") if ruta.exists() else "(no existe)"

    def escribir_evidencia(self):
        with EVIDENCIA.open("w", encoding="utf-8") as archivo:
            archivo.write("# Evidencia de pruebas del gestor de inventario\n\n")
            archivo.write("Generado con `python pruebas_gestor.py` sobre una copia temporal del proyecto.\n")
            archivo.write("Las líneas del menú se omiten; `Opción:` indica cada vuelta del menú.\n\n")
            for titulo, entradas, salida in self.resultados:
                archivo.write(f"## {titulo}\n\n")
                if entradas is not None:
                    archivo.write("Entradas: `" + " | ".join(entradas) + "`\n\n")
                archivo.write("```text\n" + salida.strip() + "\n```\n\n")


def correr(p):
    # Pruebas obligatorias (sección 16)
    p.ejecutar("Primera ejecución sin JSON", ["2", "7", "0"])
    p.ejecutar("Guardar dos productos", [*registrar(*TECLADO), *registrar(*MOUSE), "7", "0"])
    p.anotar("Contenido de datos/productos.json", p.contenido(p.json))
    p.ejecutar("Cerrar y reiniciar: se recuperan los productos", ["2", "0"])
    p.ejecutar("Registrar código duplicado", [*registrar("P001"), "2", "0"])
    p.anotar("JSON después del intento duplicado (sigue con 2 registros)",
             f"Registros en el JSON: {len(json.loads(p.contenido(p.json)))}")
    p.ejecutar("Categoría desconocida", [*registrar("P010", "Cable", "Juguetes", "1000", "1"), "3", "P010", "0"])
    p.ejecutar("Precio negativo: se rechaza y se vuelve a pedir",
               [*registrar("P011", "Cable", "Accesorios", "-500", "1000", "1"), "0"])
    p.ejecutar("Precio nan, inf y -inf", [*registrar("P012", "Hub", "Accesorios", "nan", "inf", "-inf", "20000", "3"), "0"])
    p.ejecutar("Cantidad negativa", [*registrar("P013", "Funda", "Accesorios", "15000", "-2", "2"), "0"])
    p.ejecutar("Texto no numérico en precio y cantidad",
               [*registrar("P014", "Pad", "Accesorios", "abc", "12000", "dos", "1"), "0"])
    p.ejecutar("Cantidad cero: producto sin existencias", [*registrar("P015", "Base", "Accesorios", "30000", "0"), "6", "0"])
    p.ejecutar("Eliminar productos y un código inexistente",
               ["5", "P011", "5", "P012", "5", "P013", "5", "P014", "5", "P015", "5", "P999", "0"])
    p.ejecutar("Reiniciar: los eliminados siguen eliminados", ["2", "0"])
    p.ejecutar("Actualizar a -3: se rechaza y se conserva el dato", ["4", "P001", "-3", "4", "3", "P001", "0"])

    # Prueba numérica (sección 17)
    p.ejecutar("Prueba numérica: registrar P003 y consultar resumen", [*registrar(*MONITOR), "7", "0"])
    p.ejecutar("Prueba numérica: reiniciar y obtener los mismos resultados", ["7", "0"])
    p.ejecutar("Prueba numérica: actualizar el Mouse a 5", ["4", "P002", "5", "0"])
    p.ejecutar("Prueba numérica: reiniciar, resumen y exportar CSV", ["7", "9", "0"])
    p.anotar("Contenido de reportes/inventario.csv", p.contenido(p.csv))

    # Prueba de archivos dañados (sección 18), siempre con una copia válida aparte
    copia = p.json.with_name("productos_copia.json")
    shutil.copy(p.json, copia)
    danado = p.contenido(p.json).replace(",", "", 1)
    p.json.write_text(danado, encoding="utf-8")
    p.ejecutar("JSON sin una coma: se detecta y se bloquean las modificaciones", ["2", "1", "8", "0"])
    p.anotar("¿El archivo dañado se conservó sin sustituirse por []?",
             "Sí" if p.contenido(p.json) == danado else "No")
    shutil.copy(copia, p.json)
    p.ejecutar("Restaurar la copia válida y reiniciar", ["2", "0"])

    p.json.write_text('{"codigo": "P001"}', encoding="utf-8")
    p.ejecutar("JSON con estructura inesperada (objeto en vez de lista)", ["0"])
    p.anotar("Contenido conservado", p.contenido(p.json))

    repetidos = [
        {"codigo": "P001", "nombre": "Teclado", "categoria": "Periféricos", "precio": 85000.0, "cantidad": 4},
        {"codigo": "P001", "nombre": "Otro", "categoria": "Accesorios", "precio": 1000.0, "cantidad": 1},
    ]
    p.json.write_text(json.dumps(repetidos, ensure_ascii=False, indent=4), encoding="utf-8")
    p.ejecutar("JSON con código repetido: no hay carga parcial", ["2", "0"])

    p.json.write_text(
        '[{"codigo": "P001", "nombre": "Teclado", "categoria": "Periféricos", "precio": -5, "cantidad": 4}]',
        encoding="utf-8")
    p.ejecutar("JSON con un registro inválido (precio negativo)", ["0"])
    shutil.copy(copia, p.json)

    # Error de escritura: la carpeta de destino es en realidad un archivo
    script = p.carpeta / "error_escritura.py"
    script.write_text(
        "from pathlib import Path\n"
        "from almacenamiento import cargar_inventario, guardar_inventario, ErrorAlmacenamiento\n"
        "bloqueo = Path(__file__).resolve().parent / 'bloqueo'\n"
        "bloqueo.write_text('esto es un archivo, no una carpeta')\n"
        "try:\n"
        "    guardar_inventario(cargar_inventario(), bloqueo / 'productos.json')\n"
        "    print('Inventario guardado.')\n"
        "except ErrorAlmacenamiento as error:\n"
        "    print('Guardado NO confirmado:', error)\n",
        encoding="utf-8")
    p.ejecutar("Error de escritura", [], "error_escritura.py")

    p.ejecutar("Opción no válida y salida con 0", ["x", "0"])
    p.ejecutar("Prueba de serialización", [], "pruebas_serializacion.py")
    p.ejecutar("Prueba de independencia", [], "pruebas_independencia.py")


def main():
    with tempfile.TemporaryDirectory() as temporal:
        carpeta = Path(temporal) / "gestor_inventario"
        shutil.copytree(BASE_DIR, carpeta, ignore=shutil.ignore_patterns(
            "__pycache__", "datos", "reportes", "EVIDENCIA_PRUEBAS.md"))
        pruebas = Pruebas(carpeta)
        correr(pruebas)
        pruebas.escribir_evidencia()

    print(f"{len(pruebas.resultados)} resultados guardados en {EVIDENCIA.name}")


if __name__ == "__main__":
    main()
