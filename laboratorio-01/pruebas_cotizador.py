# pruebas_cotizador:
#   ejecuta cotizador_compra.py con los casos de prueba de la práctica 1.5,
#   compara el TOTAL obtenido con el esperado y guarda todo en
#   EVIDENCIA_PRUEBAS.md

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EVIDENCIA = BASE_DIR / "EVIDENCIA_PRUEBAS.md"

# (título, [cliente, producto, precio, cantidad, descuento, impuesto], total esperado)
CASOS = [
    ("Ejemplo de la guía", ["Laura", "Teclado mecánico", "180000", "2", "10", "19"], "385560.0"),
    ("Caso 1", ["Ana", "Mouse", "100000", "2", "10", "0"], "180000.0"),
    ("Caso 2", ["Luis", "Audífonos", "50000", "3", "0", "0"], "150000.0"),
    ("Caso 3", ["Marta", "Monitor", "80000", "5", "25", "0"], "300000.0"),
    ("Caso 4", ["Pedro", "Teclado", "100000", "1", "0", "19"], "119000.0"),
]


def ejecutar(entradas):
    proceso = subprocess.run(
        [sys.executable, "-X", "utf8", "cotizador_compra.py"],
        input="\n".join(entradas) + "\n",
        cwd=BASE_DIR, capture_output=True, text=True, encoding="utf-8", timeout=30,
    )
    return proceso.stdout + proceso.stderr


def total_obtenido(salida):
    for linea in salida.splitlines():
        if linea.startswith("TOTAL: $"):
            return linea.removeprefix("TOTAL: $")
    return "(sin total)"


def main():
    aprobadas = 0

    with EVIDENCIA.open("w", encoding="utf-8") as archivo:
        archivo.write("# Evidencia de pruebas del cotizador de compra\n\n")
        archivo.write("Generado con `python pruebas_cotizador.py`. Cada caso ejecuta ")
        archivo.write("`cotizador_compra.py` con las entradas indicadas.\n\n")
        archivo.write("| Caso | Precio | Cantidad | Descuento | Impuesto | Esperado | Obtenido | Resultado |\n")
        archivo.write("|---|---:|---:|---:|---:|---:|---:|---|\n")

        salidas = []
        for titulo, entradas, esperado in CASOS:
            salida = ejecutar(entradas)
            obtenido = total_obtenido(salida)
            correcto = obtenido == esperado
            aprobadas += correcto
            salidas.append((titulo, entradas, salida))
            _, _, precio, cantidad, descuento, impuesto = entradas
            archivo.write(
                f"| {titulo} | {precio} | {cantidad} | {descuento} % | {impuesto} % "
                f"| {esperado} | {obtenido} | {'Correcto' if correcto else 'DIFERENTE'} |\n"
            )

        archivo.write("\nCálculo manual del caso 4: subtotal = 100000 × 1 = 100000; ")
        archivo.write("descuento = 0; base = 100000; impuesto = 100000 × 19 / 100 = 19000; ")
        archivo.write("total = 100000 + 19000 = 119000.\n\n")

        for titulo, entradas, salida in salidas:
            archivo.write(f"## {titulo}\n\n")
            archivo.write("Entradas: `" + " | ".join(entradas) + "`\n\n")
            archivo.write("```text\n" + salida.strip() + "\n```\n\n")

    print(f"{aprobadas} de {len(CASOS)} casos correctos. Evidencia en {EVIDENCIA.name}")


if __name__ == "__main__":
    main()
