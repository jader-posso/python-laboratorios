class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def registrar_ingreso(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Ingreso rechazado: el monto debe ser positivo.")
            return False
        self.saldo += monto
        print(f"[{self.titular}] Ingreso de {monto} registrado.")
        return True

    def registrar_gasto(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Gasto rechazado: el monto debe ser positivo.")
            return False
        if monto > self.saldo:
            print(f"[{self.titular}] Gasto rechazado: saldo insuficiente.")
            return False
        self.saldo -= monto
        print(f"[{self.titular}] Gasto de {monto} registrado.")
        return True

    def consultar_saldo(self):
        return self.saldo

maria = Billetera("María")
pedro = Billetera("Pedro")

print(f"Saldo inicial de María: {maria.consultar_saldo()}")
print(f"Saldo inicial de Pedro: {pedro.consultar_saldo()}")
print()

maria.registrar_ingreso(100000)
maria.registrar_gasto(30000)
maria.registrar_ingreso(-500)
maria.registrar_gasto(200000)
print()

pedro.registrar_ingreso(50000)
pedro.registrar_gasto(0)
pedro.registrar_gasto(20000)
print()

print(f"Saldo final de María: {maria.consultar_saldo()}")
print(f"Saldo final de Pedro: {pedro.consultar_saldo()}")
