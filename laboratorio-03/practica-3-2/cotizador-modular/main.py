import calculos
import validaciones

try:
    precio = float(input("Ingrese el precio del producto: "))
    if validaciones.precio_valido(precio):
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if validaciones.cantidad_valida(cantidad):
            porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
            if validaciones.porcentaje_valido(porcentaje_descuento):
                subtotal = calculos.subtotal(precio, cantidad)
                descuento = calculos.descuento(subtotal, porcentaje_descuento)
                impuesto = calculos.impuesto(subtotal - descuento)
                total = subtotal - descuento + impuesto
                print(f"Subtotal: {subtotal:.2f}")
                print(f"Descuento: {descuento:.2f}")
                print(f"Impuesto: {impuesto:.2f}")
                print(f"Total: {total:.2f}")
            else:
                print("Porcentaje de descuento inválido.")
        else:
            print("Cantidad inválida.")
    else:
        print("Precio inválido.")
except ValueError:
    print("Error: debe ingresar un número válido.")
