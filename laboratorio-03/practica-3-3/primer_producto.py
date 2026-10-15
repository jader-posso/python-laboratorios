class producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def mostrar_detalles(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")
        
    def calcular_valor(self):
        return self.precio * self.cantidad

teclado = producto("001", "Teclado", 50.0, 10)
mouse = producto("002", "Mouse", 30.0, 5)

teclado.mostrar_detalles()
print(f"Valor del inventario: {teclado.calcular_valor()}")
print(f"Valor del mouse: {mouse.calcular_valor()}")