import csv
from pathlib import Path

ventas = [
    {"codigo": "V001", "producto": "Teclado", "cantidad": 2, "total": 170000},
    {"codigo": "V002", "producto": "Mouse", "cantidad": 3, "total": 135000},
    {"codigo": "V003", "producto": "Monitor", "cantidad": 1, "total": 650000},
    {"codigo": "V004", "producto": "Audífonos", "cantidad": 4, "total": 240000}
]

ruta = Path(__file__).resolve().parent / "ventas.csv"

# Exportar
with ruta.open("w", newline="", encoding="utf-8") as archivo:
    campos = ["codigo", "producto", "cantidad", "total"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(ventas)

print("Ventas exportadas:", ruta)

# Leer nuevamente y calcular el total vendido
total_vendido = 0

with ruta.open("r", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for venta in lector:
        total = float(venta["total"])  # en el CSV todo se lee como texto
        total_vendido += total
        print(venta["codigo"], venta["producto"], venta["cantidad"], venta["total"])

print("Total vendido:", total_vendido)
