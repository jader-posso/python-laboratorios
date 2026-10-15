import json
from pathlib import Path

ruta = Path(__file__).resolve().parent / "libros.json"

with ruta.open("r", encoding="utf-8") as archivo:
    libros = json.load(archivo)

print("Catálogo de libros:")
for libro in libros:
    print(f"{libro['codigo']} - {libro['titulo']} ({libro['anio']}) - {libro['autor']}")
