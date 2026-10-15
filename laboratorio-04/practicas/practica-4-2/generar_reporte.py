from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CARPETA_REPORTES = BASE_DIR / "reportes"
RUTA_RESUMEN = CARPETA_REPORTES / "resumen.txt"

CARPETA_REPORTES.mkdir(exist_ok=True)

lineas = [
    "Reporte: Resumen semanal",
    "Pruebas ejecutadas: 3",
    "Estado general: estable",
]
RUTA_RESUMEN.write_text("\n".join(lineas) + "\n", encoding="utf-8")

contenido = RUTA_RESUMEN.read_text(encoding="utf-8")
print("Contenido del reporte:")
print(contenido)

print("Archivo guardado en:", RUTA_RESUMEN)
