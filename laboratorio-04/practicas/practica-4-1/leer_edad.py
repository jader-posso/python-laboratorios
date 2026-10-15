try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("No es un número entero.")
else:
    if edad < 0 or edad > 120:
        print("No se aceptan edades negativas o mayores a 120.")
    else:
        print("Edad aceptada:", edad)