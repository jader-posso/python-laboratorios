class CuentaPuntos:
    def __init__(self, titular):
        self._titular = titular
        self._puntos = 0

    @property
    def titular(self):
        return self._titular

    @property
    def puntos(self):
        return self._puntos

    def sumar(self, cantidad):
        if cantidad <= 0:
            return False

        self._puntos += cantidad
        return True

    def canjear(self, cantidad):
        if cantidad <= 0 or cantidad > self._puntos:
            return False

        self._puntos -= cantidad
        return True

def resultado(aceptado):
    return "aceptado" if aceptado else "rechazado"

cuenta = CuentaPuntos("Laura")

print(f"Sumar: 80     -> {resultado(cuenta.sumar(80))}")
print(f"Canjear: 30   -> {resultado(cuenta.canjear(30))}")
print(f"Canjear: 100  -> {resultado(cuenta.canjear(100))}")
print(f"Total: {cuenta.puntos}")
