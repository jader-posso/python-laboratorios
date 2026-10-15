#analiza

import json

class Producto:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre
        }
    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["codigo"],
            datos["nombre"]
        )


producto = Producto("P001", "Teclado")
print(json.dumps(producto.a_diccionario(), ensure_ascii=False))

datos = {"codigo": "P002", "nombre": "Mouse"}

nuevo = Producto.desde_diccionario(datos)

print(type(nuevo))
print(nuevo.nombre)