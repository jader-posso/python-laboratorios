try:
    dividendo = float(input("Dividendo: "))
    divisor = float(input("Divisor: "))
    resultado = dividendo / divisor
except ValueError:
    print("La entrada no puede convertirse en un número.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print("Resultado:", resultado)
finally:
    print("Fin de la operación.")
