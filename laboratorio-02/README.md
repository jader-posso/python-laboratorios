# Laboratorio 02 — Decisiones, ciclos y colecciones

Ejercicios sobre comparaciones, condiciones compuestas, ciclos `for` y `while`, listas, tuplas, conjuntos, diccionarios y comprensiones, y el proyecto integrador: un **gestor de inventario** de consola en un solo archivo.

## Gestor de inventario

`gestor_inventario.py` muestra un menú que se repite con `while` hasta elegir `0`:

| Opción | Qué hace |
|---|---|
| 1. Registrar producto | Pide código, nombre, categoría, precio y cantidad. Rechaza código vacío o repetido (lo revisa antes de pedir lo demás), nombre vacío, categoría fuera de `CATEGORIAS`, precio ≤ 0 y cantidad negativa |
| 2. Listar productos | Muestra cada producto o avisa que no hay registros |
| 3. Buscar por código | Muestra el producto o avisa que no existe |
| 4. Actualizar existencias | Reemplaza la cantidad; si es negativa la rechaza y conserva la anterior |
| 5. Eliminar producto | Quita el diccionario de la lista; con un código inexistente avisa sin fallar |
| 6. Productos sin stock | Comprensión de lista con los nombres de cantidad 0 |
| 7. Resumen | Productos, unidades, valor del inventario (`precio × cantidad`) y categorías usadas |

### Colecciones utilizadas

| Colección | Dónde | Por qué |
|---|---|---|
| Lista `productos` | Todos los registros | Cambia durante la ejecución: se agregan, modifican y eliminan productos. Se crea una sola vez, fuera del `while` |
| Diccionario por producto | Cada registro | Cada dato se consulta por su nombre (`producto["precio"]`) y todos tienen las mismas claves |
| Tupla `CATEGORIAS` | Categorías permitidas | Son fijas; al ser inmutable no se pueden cambiar por error |
| Conjunto (comprensión) | Categorías usadas en el resumen | Elimina repetidos automáticamente |
| Lista (comprensión) | Productos sin stock | Filtra los nombres con cantidad 0 |

### Otros archivos del proyecto

| Archivo | Qué es |
|---|---|
| `gestor_depuracion.py` | Reto de depuración: copia con cinco errores provocados (lista reiniciada en el ciclo, clave inexistente, registros duplicados, cantidad negativa aceptada y total sin multiplicar por cantidad), corregidos y explicados en comentarios |
| `pruebas_gestor.py` | Ejecuta las pruebas obligatorias y la comprobación numérica, y genera `EVIDENCIA_PRUEBAS.md` |

## Ejecución

Requiere Python 3.8 o superior y no usa dependencias externas. Desde esta carpeta:

```
python gestor_inventario.py
python pruebas_gestor.py
```

Según la guía, en esta versión el programa supone que en los campos numéricos se escriben números; la validación de texto como `abc` llega en el Laboratorio 03.

## Pruebas

Las 16 pruebas obligatorias de la guía y la prueba de código vacío dan el resultado esperado. La salida completa está en [EVIDENCIA_PRUEBAS.md](EVIDENCIA_PRUEBAS.md).

Comprobación numérica con P001 (85000 × 4), P002 (45000 × 0) y P003 (700000 × 2):

```
Productos: 3
Unidades: 6
Valor del inventario: $1740000.0
Categorías utilizadas (2): Componentes, Periféricos
Sin existencias: Mouse
```

## Ejercicios por práctica

| Práctica | Archivos |
|---|---|
| 2.1 Comparaciones y decisiones | `comparaciones.py`, `validar_edad.py`, `clasificar_numero.py`, `clasificar_nota.py`, `disponibilidad.py`, `costo_envio.py`, `error_indentacion.py` |
| 2.2 Condiciones compuestas | `acceso_actividad.py`, `acceso_sala.py`, `rango_edad.py`, `validar_compra.py`, `evaluar_solicitud.py` |
| 2.3 Ciclos `for` y `while` | `contador_for.py`, `tabla_multiplicar.py`, `promedio_notas.py`, `contador_while.py`, `hasta_cero.py`, `sumar_numeros.py`, `suma_interactiva.py`, `menu_repetitivo.py`, `control_ahorros.py` |
| 2.4 Listas | `primera_lista.py`, `operaciones_lista.py`, `ciudades.py`, `invitados.py`, `lista_materias.py`, `calificaciones_lista.py`, `lista_tareas.py`, `sin_duplicados.py` |
| 2.5 Tuplas | `primeras_tuplas.py`, `categorias_tupla.py`, `ubicaciones.py` |
| 2.6 Conjuntos | `primer_conjunto.py`, `etiquetas.py`, `participantes.py`, `inscripciones_talleres.py` |
| 2.7 Diccionarios | `primer_diccionario.py`, `perfil_diccionario.py`, `actualizar_producto.py`, `catalogo_diccionarios.py`, `catalogo_libros.py`, `curso_anidado.py` |
| 2.8 Comprensiones | `cuadrados.py`, `filtrar_numeros.py`, `precios_con_impuesto.py`, `normalizar_codigos.py`, `informe_comprensiones.py`, `catalogo_por_codigo.py`, `categorias_distintas.py`, `informes_inventario.py`, `depuracion_comprension.py` |
| 2.9 Proyecto integrador | `gestor_inventario.py`, `gestor_depuracion.py` |
