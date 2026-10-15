esta_inscrito = True
tiene_documento = False

if esta_inscrito and tiene_documento:
    print("Puede ingresar.")
else:
    print("No cumple todos los requisitos.")

print()
print("Combinaciones de and:")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

tiene_carnet = False
tiene_autorizacion = True

if tiene_carnet or tiene_autorizacion:
    print("Puede ingresar.")
else:
    print("No puede ingresar.")

print()
print("Combinaciones de or:")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

bloqueado = False

if not bloqueado:
    print("La cuenta está habilitada.")
else:
    print("La cuenta está bloqueada.")

edad = 17
acompanado = True

print(edad >= 18)
print(edad >= 18 or acompanado)
print(edad >= 18 and acompanado)
print(not acompanado)