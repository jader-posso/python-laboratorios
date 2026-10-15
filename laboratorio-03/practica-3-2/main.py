import operaciones
import saludo
#from mensajes import despedir - en este caso sale error porque no se puede importar la función despedir desde mensajes.py, ya que no está definida en el mismo archivo. Para solucionarlo, se puede definir la función despedir en este archivo o importarla desde otro archivo donde esté definida.
import validaciones

print(saludo.saludar("Jader"))

subtotal = operaciones.calcular_subtotal(100, 5)
descuento = operaciones.calcular_descuento(subtotal, 10)

print(f"Subtotal: {subtotal}")
print(f"Descuento: {descuento}")
print(f"Total: {subtotal - descuento}")
#print(despedir())

#validaciones

nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

if (
    validaciones.nombre_valido(nombre) and
    validaciones.precio_valido(precio) and
    validaciones.cantidad_valida(cantidad)
):
    print("Datos válidos")
else:
    print("Datos inválidos")
    
print(validaciones.categoria_valida("Electrónica", validaciones.CATEGORIAS))
print(validaciones.categoria_valida("Juguetes", validaciones.CATEGORIAS))