# Evidencia de pruebas del gestor de inventario

Generado con `python pruebas_gestor.py` sobre una copia temporal del proyecto.
Las líneas del menú se omiten; `Opción:` indica cada vuelta del menú.

## Primera ejecución sin JSON

Entradas: `2 | 7 | 0`

```text
Inventario vacío.
Opción: No hay productos registrados.
Opción: Productos registrados: 0
Unidades disponibles: 0
Valor del inventario: $0.0
Categorías utilizadas (0): Ninguna
Sin existencias: Ninguno
Opción: Programa finalizado.
```

## Guardar dos productos

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 1 | P002 | Mouse | Periféricos | 45000 | 0 | 7 | 0`

```text
Inventario vacío.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Inventario guardado.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Inventario guardado.
Opción: Productos registrados: 2
Unidades disponibles: 4
Valor del inventario: $340000.0
Categorías utilizadas (1): Periféricos
Sin existencias: Mouse
Opción: Programa finalizado.
```

## Contenido de datos/productos.json

```text
[
    {
        "codigo": "P001",
        "nombre": "Teclado",
        "categoria": "Periféricos",
        "precio": 85000.0,
        "cantidad": 4
    },
    {
        "codigo": "P002",
        "nombre": "Mouse",
        "categoria": "Periféricos",
        "precio": 45000.0,
        "cantidad": 0
    }
]
```

## Cerrar y reiniciar: se recuperan los productos

Entradas: `2 | 0`

```text
Se cargaron 2 productos.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
P002 - Mouse - Periféricos - $45000.0 - 0 unidades
Opción: Programa finalizado.
```

## Registrar código duplicado

Entradas: `1 | P001 | 2 | 0`

```text
Se cargaron 2 productos.
Opción: Código: Registro rechazado: el código P001 ya existe.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
P002 - Mouse - Periféricos - $45000.0 - 0 unidades
Opción: Programa finalizado.
```

## JSON después del intento duplicado (sigue con 2 registros)

```text
Registros en el JSON: 2
```

## Categoría desconocida

Entradas: `1 | P010 | Cable | Juguetes | 1000 | 1 | 3 | P010 | 0`

```text
Se cargaron 2 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Registro rechazado: Categoría no permitida. Usa: Periféricos, Componentes, Accesorios.
Opción: Código: El producto P010 no existe.
Opción: Programa finalizado.
```

## Precio negativo: se rechaza y se vuelve a pedir

Entradas: `1 | P011 | Cable | Accesorios | -500 | 1000 | 1 | 0`

```text
Se cargaron 2 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: El precio debe ser mayor que cero.
Precio: Cantidad: Producto registrado.
Inventario guardado.
Opción: Programa finalizado.
```

## Precio nan, inf y -inf

Entradas: `1 | P012 | Hub | Accesorios | nan | inf | -inf | 20000 | 3 | 0`

```text
Se cargaron 3 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: El precio debe ser un número finito.
Precio: El precio debe ser un número finito.
Precio: El precio debe ser un número finito.
Precio: Cantidad: Producto registrado.
Inventario guardado.
Opción: Programa finalizado.
```

## Cantidad negativa

Entradas: `1 | P013 | Funda | Accesorios | 15000 | -2 | 2 | 0`

```text
Se cargaron 4 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: La cantidad no puede ser negativa.
Cantidad: Producto registrado.
Inventario guardado.
Opción: Programa finalizado.
```

## Texto no numérico en precio y cantidad

Entradas: `1 | P014 | Pad | Accesorios | abc | 12000 | dos | 1 | 0`

```text
Se cargaron 5 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Debes escribir un número.
Precio: Cantidad: Debes escribir un número entero.
Cantidad: Producto registrado.
Inventario guardado.
Opción: Programa finalizado.
```

## Cantidad cero: producto sin existencias

Entradas: `1 | P015 | Base | Accesorios | 30000 | 0 | 6 | 0`

```text
Se cargaron 6 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Inventario guardado.
Opción: Sin existencias:
- Mouse
- Base
Opción: Programa finalizado.
```

## Eliminar productos y un código inexistente

Entradas: `5 | P011 | 5 | P012 | 5 | P013 | 5 | P014 | 5 | P015 | 5 | P999 | 0`

```text
Se cargaron 7 productos.
Opción: Código: Producto eliminado.
Inventario guardado.
Opción: Código: Producto eliminado.
Inventario guardado.
Opción: Código: Producto eliminado.
Inventario guardado.
Opción: Código: Producto eliminado.
Inventario guardado.
Opción: Código: Producto eliminado.
Inventario guardado.
Opción: Código: El producto P999 no existe.
Opción: Programa finalizado.
```

## Reiniciar: los eliminados siguen eliminados

Entradas: `2 | 0`

```text
Se cargaron 2 productos.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
P002 - Mouse - Periféricos - $45000.0 - 0 unidades
Opción: Programa finalizado.
```

## Actualizar a -3: se rechaza y se conserva el dato

Entradas: `4 | P001 | -3 | 4 | 3 | P001 | 0`

```text
Se cargaron 2 productos.
Opción: Código: Cantidad: La cantidad no puede ser negativa.
Cantidad: Existencias actualizadas.
Inventario guardado.
Opción: Código: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## Prueba numérica: registrar P003 y consultar resumen

Entradas: `1 | P003 | Monitor | Componentes | 700000 | 2 | 7 | 0`

```text
Se cargaron 2 productos.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Inventario guardado.
Opción: Productos registrados: 3
Unidades disponibles: 6
Valor del inventario: $1740000.0
Categorías utilizadas (2): Componentes, Periféricos
Sin existencias: Mouse
Opción: Programa finalizado.
```

## Prueba numérica: reiniciar y obtener los mismos resultados

Entradas: `7 | 0`

```text
Se cargaron 3 productos.
Opción: Productos registrados: 3
Unidades disponibles: 6
Valor del inventario: $1740000.0
Categorías utilizadas (2): Componentes, Periféricos
Sin existencias: Mouse
Opción: Programa finalizado.
```

## Prueba numérica: actualizar el Mouse a 5

Entradas: `4 | P002 | 5 | 0`

```text
Se cargaron 3 productos.
Opción: Código: Cantidad: Existencias actualizadas.
Inventario guardado.
Opción: Programa finalizado.
```

## Prueba numérica: reiniciar, resumen y exportar CSV

Entradas: `7 | 9 | 0`

```text
Se cargaron 3 productos.
Opción: Productos registrados: 3
Unidades disponibles: 11
Valor del inventario: $1965000.0
Categorías utilizadas (2): Componentes, Periféricos
Sin existencias: Ninguno
Opción: Reporte exportado: reportes/inventario.csv
Opción: Programa finalizado.
```

## Contenido de reportes/inventario.csv

```text
codigo,nombre,categoria,precio,cantidad,valor_inventario
P001,Teclado,Periféricos,85000.0,4,340000.0
P002,Mouse,Periféricos,45000.0,5,225000.0
P003,Monitor,Componentes,700000.0,2,1400000.0
```

## JSON sin una coma: se detecta y se bloquean las modificaciones

Entradas: `2 | 1 | 8 | 0`

```text
ATENCIÓN: no se pudo cargar el inventario.
productos.json tiene un formato JSON inválido (línea 4, columna 9: Expecting ',' delimiter).
Revisa o restaura el archivo: C:\Users\Jader\AppData\Local\Temp\tmpzrdo4id0\gestor_inventario\datos\productos.json
Para no perder datos, el archivo no se modificará en esta sesión:
las opciones que registran, cambian, guardan o exportan quedan bloqueadas.
Opción: No hay productos registrados.
Opción: Operación bloqueada: el archivo del inventario está dañado.
Corrígelo o restáuralo y vuelve a iniciar el programa.
Opción: Operación bloqueada: el archivo del inventario está dañado.
Corrígelo o restáuralo y vuelve a iniciar el programa.
Opción: Programa finalizado.
```

## ¿El archivo dañado se conservó sin sustituirse por []?

```text
Sí
```

## Restaurar la copia válida y reiniciar

Entradas: `2 | 0`

```text
Se cargaron 3 productos.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
P002 - Mouse - Periféricos - $45000.0 - 5 unidades
P003 - Monitor - Componentes - $700000.0 - 2 unidades
Opción: Programa finalizado.
```

## JSON con estructura inesperada (objeto en vez de lista)

Entradas: `0`

```text
ATENCIÓN: no se pudo cargar el inventario.
productos.json contiene datos no válidos. Se esperaba una lista de productos.
Revisa o restaura el archivo: C:\Users\Jader\AppData\Local\Temp\tmpzrdo4id0\gestor_inventario\datos\productos.json
Para no perder datos, el archivo no se modificará en esta sesión:
las opciones que registran, cambian, guardan o exportan quedan bloqueadas.
Opción: Programa finalizado.
```

## Contenido conservado

```text
{"codigo": "P001"}
```

## JSON con código repetido: no hay carga parcial

Entradas: `2 | 0`

```text
ATENCIÓN: no se pudo cargar el inventario.
productos.json contiene datos no válidos. Registro 2: el código P001 está repetido.
Revisa o restaura el archivo: C:\Users\Jader\AppData\Local\Temp\tmpzrdo4id0\gestor_inventario\datos\productos.json
Para no perder datos, el archivo no se modificará en esta sesión:
las opciones que registran, cambian, guardan o exportan quedan bloqueadas.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## JSON con un registro inválido (precio negativo)

Entradas: `0`

```text
ATENCIÓN: no se pudo cargar el inventario.
productos.json contiene datos no válidos. Registro 1: El precio debe ser mayor que cero.
Revisa o restaura el archivo: C:\Users\Jader\AppData\Local\Temp\tmpzrdo4id0\gestor_inventario\datos\productos.json
Para no perder datos, el archivo no se modificará en esta sesión:
las opciones que registran, cambian, guardan o exportan quedan bloqueadas.
Opción: Programa finalizado.
```

## Error de escritura

Entradas: ``

```text
Guardado NO confirmado: No se pudo guardar productos.json: No se puede crear un archivo que ya existe.
```

## Opción no válida y salida con 0

Entradas: `x | 0`

```text
Se cargaron 3 productos.
Opción: Opción no válida.
Opción: Programa finalizado.
```

## Prueba de serialización

Entradas: ``

```text
Original:      {'codigo': 'P001', 'nombre': 'Teclado', 'categoria': 'Periféricos', 'precio': 85000.0, 'cantidad': 4}
Diccionario:   {'codigo': 'P001', 'nombre': 'Teclado', 'categoria': 'Periféricos', 'precio': 85000.0, 'cantidad': 4}
Reconstruido:  {'codigo': 'P001', 'nombre': 'Teclado', 'categoria': 'Periféricos', 'precio': 85000.0, 'cantidad': 4}
¿Mismos datos? True
¿Mismo objeto? False
```

## Prueba de independencia

Entradas: ``

```text
Primero: 1
Segundo: 0
```

