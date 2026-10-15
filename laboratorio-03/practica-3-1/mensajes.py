def mostrar_encabezado():
    print("==========================")
    print("   Bienvenido al sistema   ")
    print("==========================")
    
def mostrar_despedida():
    print("==================================")
    print("    Gracias por usar el sistema   ")
    print("==================================")
    
mostrar_encabezado()
mostrar_encabezado() 
print("Registro de productos")
mostrar_despedida()  

#Parametros y argumentos

def saludar(nombre):
    print(f"Hola {nombre}, bienvenido al sistema")
    
saludar("Jader")
saludar("Maria")


def mostrar_producto(nombre, cantidad):
    print(f"Producto: {nombre}")
    print(f"Existencias: {cantidad}")
    
mostrar_producto("Laptop", 10)
mostrar_producto("Mouse", 25)


def presentar(nombre, ciudad):
    print(f"Hola, mi nombre es {nombre} y vivo en {ciudad}")
    
presentar("Jader", "Bogotá")
presentar("Maria", "Medellín") #Diria la frase en un sentido inverso o incorrecto, ya que el nombre y la ciudad no están en el orden correcto.

def despedir():
    return "¡Hasta luego!"

if __name__ == "__main__": #solo se ejecuta si se llama directamente al archivo, no si se importa como módulo
    print("Prueba directa")