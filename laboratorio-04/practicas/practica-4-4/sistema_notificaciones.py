class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Cada notificación debe implementar enviar()")


class NotificacionCorreo(Notificacion):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar(self, mensaje):
        return f"[Correo para {self.destinatario}] Asunto: Aviso | {mensaje}"


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        return f"[Consola] >>> {mensaje}"


# Fuera de las notificaciones: qué mensaje se envía y a qué canales.
def notificar(canales, mensaje):
    for canal in canales:
        print(canal.enviar(mensaje))


canales = [NotificacionCorreo("ana@ejemplo.com"), NotificacionConsola()]

notificar(canales, "El inventario fue actualizado.")
