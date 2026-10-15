# Gestor de inventario orientado a objetos

Aplicación de consola que registra, lista, busca, actualiza y elimina productos, y genera informes del inventario. Es la versión con clases del gestor del Laboratorio 2: cada registro es una instancia de `Producto` y la colección la administra una instancia de `Inventario`.

## Archivos

| Archivo | Responsabilidad |
|---|---|
| `producto.py` | Clase `Producto` y la tupla `CATEGORIAS`. Valida sus datos desde `__init__`, ofrece propiedades de consulta, actualiza existencias y calcula `precio * cantidad`. |
| `inventario.py` | Clase `Inventario`. Guarda su propia lista `self._productos` y hace el registro, la búsqueda, la actualización, la eliminación y los informes. |
| `main.py` | Menú, lectura de datos con `input()` y mensajes al usuario. |
| `pruebas_independencia.py` | Comprueba que dos inventarios no comparten datos. |

`Producto` e `Inventario` no usan `input()` ni imprimen nada: solo devuelven valores (`True`/`False`, objetos, `None` o un diccionario), y `main.py` decide qué mostrar.

## Ejecución

Desde la carpeta `gestor_inventario`:

```
python main.py
python pruebas_independencia.py
```

No requiere instalar dependencias.

## Preguntas antes de programar

1. **¿Qué clase debe evitar los códigos repetidos?** `Inventario`, porque es la única que conoce todos los productos registrados.
2. **¿Qué clase debe comprobar que la cantidad sea válida?** `Producto`, tanto al crearse como en `actualizar_existencias()`. `Inventario` delega en ese método.
3. **¿Qué clase calcula el valor de un producto?** `Producto`, con `calcular_valor()`. `Inventario` suma esos valores en `resumen()`.
4. **¿Dónde debe utilizarse `input()`?** Solo en `main.py`.
5. **¿Quién decide qué mensaje se muestra después de una operación?** `main.py`, según el valor que devuelven los métodos.

## Pruebas realizadas

| Caso | Resultado obtenido |
|---|---|
| Iniciar inventario vacío | "No hay productos registrados." y resumen con 0 productos, 0 unidades y $0 |
| Registrar P001 | Producto registrado |
| Registrar nuevamente P001 | Registro rechazado: el código P001 ya existe |
| Código vacío o solo espacios | Registro rechazado: el código no puede estar vacío |
| Nombre vacío | Registro rechazado: el nombre no puede estar vacío |
| Categoría "Muebles" | Registro rechazado: categoría no permitida |
| Precio 0 | "El precio debe ser mayor que cero." y vuelve a pedirlo |
| Cantidad -2 | "La cantidad no puede ser negativa." y vuelve a pedirla |
| Cantidad 0 (P002 Mouse) | Producto registrado y aparece en "Sin existencias" |
| Buscar P001 | `P001 - Teclado - Periféricos - $85000.0 - 4 unidades` |
| Buscar P999 | "El producto P999 no existe." |
| Actualizar P001 a 10 | Solo cambia la cantidad |
| Actualizar P001 a -3 | Rechazado; conserva la cantidad anterior |
| Eliminar producto existente | Producto eliminado |
| Eliminar P999 | "El producto P999 no existe." y el programa continúa |
| Escribir "abc" en el precio | "Debes escribir un número." y vuelve a pedirlo |
| Opción 9 | "Opción no válida." |
| Opción 0 | "Programa finalizado." |

Si se crea un `Producto` directamente con datos inválidos (por ejemplo, precio -10), se lanza `ValueError`. `main.py` captura ese error al registrar y muestra el mensaje.

### Comprobación numérica

Con P001 (85000 × 4, Periféricos), P002 (45000 × 0, Periféricos) y P003 (700000 × 2, Componentes):

```
Productos registrados: 3
Unidades disponibles: 6
Valor del inventario: $1740000.0
Categorías utilizadas: 2
Producto sin stock: Mouse
```

Después de actualizar P002 a 5 unidades:

```
Productos registrados: 3
Unidades disponibles: 11
Valor del inventario: $1965000.0
```

### Prueba de independencia

```
Primero: 1
Segundo: 0
```
