class Estudiante:
    def __init__(self, nombre, ficha, promedio):
        self.nombre = nombre
        self.ficha = ficha
        self.promedio = promedio

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ficha: {self.ficha}")
        print(f"Promedio: {self.promedio}")

    def aprobo(self):
        return self.promedio >= 3

ana = Estudiante("Ana", "2901234", 4.2)
luis = Estudiante("Luis", "2901235", 2.8)

ana.mostrar_perfil()
print(f"¿Aprobó?: {ana.aprobo()}")
luis.mostrar_perfil()
print(f"¿Aprobó?: {luis.aprobo()}")


#funcion o metodo

class regitro:
    def __init__(self):
        self.elementos = []
        
primero = regitro()
segundo = regitro()

primero.elementos.append("Teclado")

print("Primero: ", primero.elementos)
print("Segundo: ", segundo.elementos)
