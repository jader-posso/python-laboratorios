# Evidencia de pruebas del gestor de inventario orientado a objetos

Generado con `python pruebas_gestor.py`. Cada prueba inicia `main.py` desde cero con las entradas indicadas.
Las líneas del menú se omiten; `Opción:` indica cada vuelta del menú.

## 1. Iniciar inventario vacío

Esperado: Listado vacío y resumen en cero.

Entradas: `2 | 7 | 0`

```text
Opción: No hay productos registrados.
Opción: Productos registrados: 0
Unidades disponibles: 0
Valor del inventario: $0.0
Categorías utilizadas (0): Ninguna
Opción: Programa finalizado.
```

## 2. Registrar P001

Esperado: Registro aceptado.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## 3. Registrar nuevamente P001

Esperado: Registro rechazado.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 1 | P001 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Registro rechazado: el código P001 ya existe.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## 4. Registrar código o nombre vacío

Esperado: Registro rechazado.

Entradas: `1 |     | Cable | Accesorios | 1000 | 1 | 1 | P004 |  | Accesorios | 1000 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Registro rechazado: El código no puede estar vacío.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Registro rechazado: El nombre no puede estar vacío.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 5. Categoría no permitida

Esperado: Registro rechazado.

Entradas: `1 | P004 | Silla | Muebles | 1000 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Registro rechazado: Categoría no permitida. Usa: Periféricos, Componentes, Accesorios.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 6. Precio cero o negativo

Esperado: Registro rechazado: se vuelve a pedir el precio.

Entradas: `1 | P004 | Cable | Accesorios | 0 | -500 | 1000 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: El precio debe ser mayor que cero.
Precio: El precio debe ser mayor que cero.
Precio: Cantidad: Producto registrado.
Opción: P004 - Cable - Accesorios - $1000.0 - 1 unidades
Opción: Programa finalizado.
```

## 7. Cantidad negativa

Esperado: Registro rechazado: se vuelve a pedir la cantidad.

Entradas: `1 | P004 | Cable | Accesorios | 1000 | -2 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: La cantidad no puede ser negativa.
Cantidad: Producto registrado.
Opción: P004 - Cable - Accesorios - $1000.0 - 1 unidades
Opción: Programa finalizado.
```

## 8. Cantidad cero

Esperado: Producto válido y sin existencias.

Entradas: `1 | P002 | Mouse | Periféricos | 45000 | 0 | 6 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Sin existencias:
- Mouse
Opción: Programa finalizado.
```

## 9. Buscar P001

Esperado: Mostrar su información.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 3 | P001 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## 10. Buscar P999

Esperado: Informar que no existe.

Entradas: `3 | P999 | 0`

```text
Opción: Código: El producto P999 no existe.
Opción: Programa finalizado.
```

## 11. Actualizar a 10 unidades

Esperado: Modificar solo la cantidad.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 4 | P001 | 10 | 3 | P001 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Cantidad: Existencias actualizadas.
Opción: Código: P001 - Teclado - Periféricos - $85000.0 - 10 unidades
Opción: Programa finalizado.
```

## 12. Actualizar a -3 unidades

Esperado: Rechazar, conservar el dato anterior.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 4 | P001 | -3 | 4 | 3 | P001 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Cantidad: La cantidad no puede ser negativa.
Cantidad: Existencias actualizadas.
Opción: Código: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## 13. Eliminar producto existente

Esperado: Quitar el registro.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 5 | P001 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Producto eliminado.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 14. Eliminar código inexistente

Esperado: Informar sin fallar.

Entradas: `5 | P999 | 2 | 0`

```text
Opción: Código: El producto P999 no existe.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 15. Ingresar texto en un campo numérico

Esperado: Mensaje y nueva oportunidad.

Entradas: `1 | P004 | Cable | Accesorios | abc | 1000 | dos | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Debes escribir un número.
Precio: Cantidad: Debes escribir un número entero.
Cantidad: Producto registrado.
Opción: P004 - Cable - Accesorios - $1000.0 - 1 unidades
Opción: Programa finalizado.
```

## 16. Consultar resumen

Esperado: Totales coherentes.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 1 | P002 | Mouse | Periféricos | 45000 | 0 | 7 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Productos registrados: 2
Unidades disponibles: 4
Valor del inventario: $340000.0
Categorías utilizadas (1): Periféricos
Opción: Programa finalizado.
```

## 17. Salir

Esperado: Terminar el ciclo.

Entradas: `9 | 0`

```text
Opción: Opción no válida.
Opción: Programa finalizado.
```

## Comprobación numérica

Esperado: 3 productos, 6 unidades, $1740000.0, 2 categorías y Mouse sin stock; después de actualizar P002 a 5: 11 unidades y $1965000.0 (1740000 + 45000 × 5 = 1965000).

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 1 | P002 | Mouse | Periféricos | 45000 | 0 | 1 | P003 | Monitor | Componentes | 700000 | 2 | 6 | 7 | 4 | P002 | 5 | 7 | 0`

```text
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nombre: Categorías permitidas: Periféricos, Componentes, Accesorios
Categoría: Precio: Cantidad: Producto registrado.
Opción: Sin existencias:
- Mouse
Opción: Productos registrados: 3
Unidades disponibles: 6
Valor del inventario: $1740000.0
Categorías utilizadas (2): Componentes, Periféricos
Opción: Código: Cantidad: Existencias actualizadas.
Opción: Productos registrados: 3
Unidades disponibles: 11
Valor del inventario: $1965000.0
Categorías utilizadas (2): Componentes, Periféricos
Opción: Programa finalizado.
```

## Prueba de independencia

Esperado: Primero: 1 y Segundo: 0, porque cada Inventario tiene su propia lista.

```text
Primero: 1
Segundo: 0
```

