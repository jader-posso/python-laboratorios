# Gestor de inventario con persistencia

Aplicación de consola que registra, lista, busca, actualiza y elimina productos. Es la evolución del gestor orientado a objetos del Laboratorio 3; esta versión añade:

- carga del inventario desde `datos/productos.json` al iniciar;
- guardado automático después de cada cambio aceptado (y desde el menú);
- exportación de un informe CSV en `reportes/inventario.csv`;
- validaciones y manejo de errores de entrada y de archivos;
- separación de responsabilidades entre clases y módulos.

## Estructura

```
gestor_inventario/
├── main.py
├── producto.py
├── inventario.py
├── almacenamiento.py
├── reportes.py
├── pruebas_independencia.py
├── pruebas_serializacion.py
├── pruebas_gestor.py
├── EVIDENCIA_PRUEBAS.md
├── datos/
│   └── productos.json      (se crea al guardar)
├── reportes/
│   └── inventario.csv      (se crea al exportar)
└── README.md
```

| Archivo | Responsabilidad |
|---|---|
| `producto.py` | Clase `Producto` y la tupla `CATEGORIAS`. Valida sus datos en el constructor, ofrece propiedades de consulta, calcula `precio * cantidad`, y se convierte con `a_diccionario()` / `desde_diccionario()`. Incluye `validar_precio()` y `validar_cantidad()`, que también usa `main.py` para volver a pedir un dato incorrecto. |
| `inventario.py` | Clase `Inventario`. Registra, busca, actualiza, elimina y consulta. `exportar_datos()` devuelve una lista de diccionarios nuevos (no la lista interna) y `desde_datos()` reconstruye un inventario completo o lanza `ValueError`. |
| `almacenamiento.py` | `cargar_inventario()` y `guardar_inventario()`. Ubica el JSON con `pathlib` respecto al proyecto. Informa los problemas con la excepción `ErrorAlmacenamiento`. |
| `reportes.py` | `exportar_csv()`: construye las filas con `valor_inventario` y escribe el CSV con encabezados. Devuelve la ruta del archivo. |
| `main.py` | Menú, lectura de datos con `input()`, coordinación de operaciones y mensajes al usuario. |
| `pruebas_independencia.py` | Comprueba que dos inventarios no comparten datos (del Laboratorio 3). |
| `pruebas_serializacion.py` | Comprueba que un producto se reconstruye igual desde su diccionario. |
| `pruebas_gestor.py` | Ejecuta las pruebas obligatorias, la numérica y la de archivos dañados sobre una copia temporal del proyecto y guarda la salida en `EVIDENCIA_PRUEBAS.md`. |

Reglas de separación que se cumplen:

- Solo `main.py` usa `input()`.
- `almacenamiento.py` no pregunta nada al usuario; devuelve un resultado o lanza una excepción.
- `reportes.py` solo consulta el inventario, nunca cambia existencias.
- Nadie fuera de `Inventario` accede a `_productos`.

## Ejecución

Requiere Python 3.8 o superior, sin dependencias externas. Se puede ejecutar desde cualquier carpeta, porque las rutas se calculan con `Path(__file__).resolve().parent`:

```
python main.py
python pruebas_serializacion.py
python pruebas_independencia.py
python pruebas_gestor.py
```

## Funcionamiento

### Reglas de los productos

- Código único y no vacío.
- Nombre no vacío.
- Categoría de `CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")`.
- Precio numérico, finito (se rechazan `nan` e `inf`) y mayor que cero.
- Cantidad entera y no negativa. La cantidad 0 se acepta: es un producto sin existencias.

`desde_diccionario()` usa el constructor, así que los datos leídos del JSON pasan por las mismas validaciones que los ingresados por teclado.

### Carga al iniciar

| Estado de `productos.json` | Resultado |
|---|---|
| No existe | Inventario vacío, sin error. |
| Existe y es válido | Se recuperan todos los productos. |
| Sintaxis incorrecta, estructura inesperada, registro inválido o código repetido | Se informa el problema y no se carga ningún producto. |

Para evitar cargas parciales, `Inventario.desde_datos()` construye primero un inventario temporal y solo lo devuelve si todos los registros son válidos.

Si el archivo existe pero está dañado, el programa arranca con un inventario vacío **solo en memoria**. Además bloquea las opciones que registran, actualizan, eliminan, guardan o exportan (1, 4, 5, 8 y 9). Así nunca se escribe sobre el archivo problemático. Las consultas siguen disponibles. Para continuar hay que corregir o restaurar el archivo y reiniciar.

### Guardado

- Cada registro, actualización o eliminación **aceptado** se guarda enseguida. Una operación rechazada no se guarda.
- "Inventario guardado." se muestra solo cuando la escritura terminó sin errores.
- Si la escritura falla, aparece el mensaje "Los cambios podrían existir solamente en memoria.". Al salir con 0 se intenta guardar otra vez.
- El JSON se escribe primero en `productos.json.tmp` y luego reemplaza al original. Así, un fallo a mitad de la escritura no deja el archivo incompleto.

### Reporte CSV

Columnas: `codigo,nombre,categoria,precio,cantidad,valor_inventario`, donde `valor_inventario = precio * cantidad`. El CSV es una foto del momento: si después cambian las cantidades, hay que volver a exportarlo.

## Estado

Las 9 etapas del laboratorio están completas y todas las pruebas obligatorias pasan.

## Pruebas realizadas

La salida completa de cada prueba está en [EVIDENCIA_PRUEBAS.md](EVIDENCIA_PRUEBAS.md) y se puede regenerar con `python pruebas_gestor.py`.

Las pruebas de archivos dañados y de error de escritura se hicieron sobre **copias** del proyecto, nunca sobre la única versión válida de los datos.

| Situación | Resultado obtenido |
|---|---|
| Primera ejecución, JSON inexistente | "Inventario vacío." sin errores; el resumen muestra 0 productos y $0.0. |
| Guardar productos | `productos.json` contiene todos los registros. |
| Cerrar y reiniciar | "Se cargaron 3 productos." con sus datos. |
| Registrar código duplicado (P001) | "Registro rechazado: el código P001 ya existe." El JSON no cambia. |
| Categoría "Muebles" | Rechazada: categoría no permitida. |
| Nombre vacío | Rechazado: el nombre no puede estar vacío. |
| Precio -5 o 0 | "El precio debe ser mayor que cero." y lo vuelve a pedir. |
| Precio `nan` o `inf` | "El precio debe ser un número finito." y lo vuelve a pedir. |
| Cantidad -2 | "La cantidad no puede ser negativa." y la vuelve a pedir. |
| Cantidad 1.5 | "Debes escribir un número entero." y la vuelve a pedir. |
| Cantidad 0 | Aceptada; aparece en "Sin existencias". |
| Actualizar una cantidad | Se conserva tras reiniciar. |
| Eliminar un producto | Sigue eliminado tras reiniciar. |
| Eliminar o buscar P999 | "El producto P999 no existe." y el programa continúa. |
| Texto no numérico ("abc") en precio o cantidad | Mensaje y nueva oportunidad. |
| JSON con sintaxis incorrecta | "formato JSON inválido (línea 1, columna 41: Expecting ',' delimiter)". Archivo intacto. |
| JSON con un objeto en vez de una lista | "Se esperaba una lista de productos." Archivo intacto. |
| JSON con un campo faltante | "Registro 1: falta el campo 'cantidad'." Archivo intacto. |
| JSON con precio de texto | "Registro 1: El precio debe ser un número." Archivo intacto. |
| JSON con código repetido | "Registro 3: el código P001 está repetido." No se carga ningún producto. Archivo intacto. |
| Opciones 1, 4, 5, 8 y 9 con el JSON dañado | "Operación bloqueada". No se escribe el JSON ni el CSV. |
| Error de escritura (JSON de solo lectura) | "Error al guardar: … Acceso denegado." y "Los cambios podrían existir solamente en memoria." Nunca dice "Inventario guardado.". El original queda intacto y sin `.tmp` sobrante. |
| Exportar CSV | `reportes/inventario.csv` con encabezados y valores correctos. |
| Opción no válida ("x", "99") | "Opción no válida." |
| Opción 0 | "Programa finalizado." |
| Ejecutar desde otra carpeta | Encuentra y crea `datos/` y `reportes/` dentro del proyecto. |

### Prueba numérica

Con P001 Teclado (85000 × 4, Periféricos), P002 Mouse (45000 × 0, Periféricos) y P003 Monitor (700000 × 2, Componentes):

```
Productos registrados: 3
Unidades disponibles: 6
Valor del inventario: $1740000.0
Categorías utilizadas (2): Componentes, Periféricos
Sin existencias: Mouse
```

Tras cerrar y reiniciar se obtienen los mismos resultados. Después de actualizar el Mouse a 5, guardar y reiniciar:

```
Productos registrados: 3
Unidades disponibles: 11
Valor del inventario: $1965000.0
```

CSV exportado:

```
codigo,nombre,categoria,precio,cantidad,valor_inventario
P001,Teclado,Periféricos,85000.0,4,340000.0
P002,Mouse,Periféricos,45000.0,5,225000.0
P003,Monitor,Componentes,700000.0,2,1400000.0
```

### Prueba de serialización

```
Original:      {'codigo': 'P001', 'nombre': 'Teclado', 'categoria': 'Periféricos', 'precio': 85000.0, 'cantidad': 4}
Reconstruido:  {'codigo': 'P001', 'nombre': 'Teclado', 'categoria': 'Periféricos', 'precio': 85000.0, 'cantidad': 4}
¿Mismos datos? True
¿Mismo objeto? False
```
