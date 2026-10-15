
ciudades = []

while len(ciudades) <= 4:
    new_ciudad = input(f"Ingrese una ciudad {len(ciudades) + 1}: ")
    ciudades.append(new_ciudad)
print("La primera cuidad es:" + ciudades[0])
print("La tercera ciudad es:" + ciudades[2])
print("La última ciudad es:" + ciudades[-1])
print("Cantidad de ciudades ingresadas: " + str(len(ciudades)))