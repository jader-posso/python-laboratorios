# Producto:
#   representa un artículo y controla sus valores
#   se convierte a diccionario y se reconstruye desde uno

import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


def validar_precio(precio):
    # bool es subclase de int, pero True/False no son precios
    if isinstance(precio, bool) or not isinstance(precio, (int, float)):
        raise ValueError("El precio debe ser un número.")

    if not math.isfinite(precio):
        raise ValueError("El precio debe ser un número finito.")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero.")


def validar_cantidad(cantidad):
    if isinstance(cantidad, bool) or not isinstance(cantidad, int):
        raise ValueError("La cantidad debe ser un número entero.")

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if categoria not in CATEGORIAS:
            raise ValueError(f"Categoría no permitida. Usa: {', '.join(CATEGORIAS)}.")

        validar_precio(precio)
        validar_cantidad(cantidad)

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        try:
            validar_cantidad(nueva_cantidad)
        except ValueError:
            return False

        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        return self._precio * self._cantidad

    def a_diccionario(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }

    @classmethod
    def desde_diccionario(cls, datos):
        # Usa el constructor para que también se apliquen las validaciones
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
        )
