edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

tiene_autorizacion = autorizacion == "si"

if edad >= 18:
    print("Puede ingresar.")
elif tiene_autorizacion:
    print("Puede ingresar con autorización.")
else:
    print("No puede ingresar.")