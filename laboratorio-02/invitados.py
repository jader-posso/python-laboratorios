invitados = []

for i in range(5):
    nombre = input("Nombre del invitado " + str(i + 1) + ": ").strip()
    invitados.append(nombre)

print("Cantidad de invitados:", len(invitados))
print("Invitados:", invitados)