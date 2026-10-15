# reportes:
#   construye y exporta el informe CSV del inventario
#   solo consulta el inventario, nunca lo modifica

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RUTA_CSV = BASE_DIR / "reportes" / "inventario.csv"
CAMPOS = ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"]


def construir_filas(inventario):
    filas = []

    for datos in inventario.exportar_datos():
        datos["valor_inventario"] = datos["precio"] * datos["cantidad"]
        filas.append(datos)

    return filas


def exportar_csv(inventario, ruta=RUTA_CSV):
    # Los errores de escritura (OSError) se dejan pasar para que main.py los informe
    filas = construir_filas(inventario)

    ruta.parent.mkdir(parents=True, exist_ok=True)

    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(filas)

    return ruta
