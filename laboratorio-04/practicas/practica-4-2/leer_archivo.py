from pathlib import Path

ruta = Path("mensaje.txt")

contenido = ruta.read_text(encoding="utf-8")

print("Contenido:")
print(contenido)