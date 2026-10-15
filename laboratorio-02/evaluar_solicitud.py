edad = int(input("Edad: "))
inscripcion = input("¿Está inscrito? (si/no): ").strip().lower()
documentos = int(input("Número de documentos entregados: "))

cumple = edad >= 16 and inscripcion and documentos >= 3

if cumple:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud no cumple todos los requisitos.")

    if edad < 16:
        print("- La edad debe ser al menos 16 años.")

    if not inscripcion:
        print("- Debe estar inscrito.")

    if documentos < 3:
        print("- Se requieren al menos 3 documentos.")