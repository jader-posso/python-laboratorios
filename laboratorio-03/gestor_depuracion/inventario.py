# Inventario:
#   conserva varios objetos Producto
#   registra, busca, actualiza, elimina y consulta


class Inventario:
    # ERROR 1 (lista compartida): se había declarado  _productos = []  aquí,
    # como atributo de clase, sin crearla en __init__. Todos los objetos
    # Inventario usaban la misma lista: pruebas_independencia.py mostraba
    # "Primero: 1" y "Segundo: 1". Se crea en __init__ con self para que
    # cada inventario tenga la suya.
    def __init__(self):
        self._productos = []

    def registrar_producto(self, producto):
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def listar_productos(self):
        return self._productos.copy()

    # ERROR 3 (falta self): se había escrito  def buscar_por_codigo(codigo):
    # Python pasa el objeto como primer argumento, así que al registrar
    # aparecía TypeError: Inventario.buscar_por_codigo() takes 1 positional
    # argument but 2 were given. Todo método de instancia recibe self primero.
    def buscar_por_codigo(self, codigo):
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [
            producto
            for producto in self._productos
            if producto.cantidad == 0
        ]

    def resumen(self):
        return {
            "productos": len(self._productos),
            "unidades": sum(producto.cantidad for producto in self._productos),
            # ERROR 6 (total mal calculado): se sumaba producto.precio. Con P001,
            # P002 y P003 el valor daba $830000.0 en lugar de $1740000.0.
            # calcular_valor() ya multiplica precio por cantidad.
            "valor": sum((producto.calcular_valor() for producto in self._productos), 0.0),
            "categorias": {producto.categoria for producto in self._productos},
        }
