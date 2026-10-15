# almacenamiento:
#   lee y escribe el inventario en datos/productos.json
#   no pregunta nada al usuario: informa con retornos o excepciones

import json
from pathlib import Path

from inventario import Inventario

BASE_DIR = Path(__file__).resolve().parent
RUTA_JSON = BASE_DIR / "datos" / "productos.json"


class ErrorAlmacenamiento(Exception):
    """No se pudo leer o escribir el archivo del inventario."""


def cargar_inventario(ruta=RUTA_JSON):
    # Archivo inexistente: inventario vacío.
    # Archivo dañado: ErrorAlmacenamiento, sin tocar el archivo.
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            registros = json.load(archivo)
    except FileNotFoundError:
        return Inventario()
    except json.JSONDecodeError as error:
        raise ErrorAlmacenamiento(
            f"{ruta.name} tiene un formato JSON inválido "
            f"(línea {error.lineno}, columna {error.colno}: {error.msg})."
        ) from None
    except UnicodeDecodeError:
        raise ErrorAlmacenamiento(f"{ruta.name} no está codificado en UTF-8.") from None
    except OSError as error:
        raise ErrorAlmacenamiento(f"No se pudo leer {ruta.name}: {error.strerror or error}.") from None

    try:
        return Inventario.desde_datos(registros)
    except ValueError as error:
        raise ErrorAlmacenamiento(f"{ruta.name} contiene datos no válidos. {error}") from None


def guardar_inventario(inventario, ruta=RUTA_JSON):
    # Se escribe primero en un archivo temporal y solo al terminar sin errores
    # se reemplaza el original; así un fallo a mitad no deja el JSON a medias.
    datos = inventario.exportar_datos()
    temporal = ruta.with_name(ruta.name + ".tmp")

    try:
        ruta.parent.mkdir(parents=True, exist_ok=True)

        with temporal.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

        temporal.replace(ruta)
    except OSError as error:
        temporal.unlink(missing_ok=True)
        raise ErrorAlmacenamiento(f"No se pudo guardar {ruta.name}: {error.strerror or error}.") from None

    return ruta
