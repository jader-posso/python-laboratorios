nombre = input("Nombre de la prueba: ").strip()

resultado = input("Resultado (aprobado/fallida): ").strip().lower()
while resultado not in ("aprobado", "fallida"):
    print("Escribe 'aprobado' o 'fallida'.")
    resultado = input("Resultado (aprobado/fallida): ").strip().lower()

observacion = input("Observación breve: ").strip()

with open("pruebas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre} | {resultado} | {observacion}\n")

print("Prueba registrada en pruebas.txt")
