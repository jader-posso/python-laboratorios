# Evidencia de pruebas del gestor de inventario

Generado con `python pruebas_gestor.py`. Cada prueba inicia el programa desde cero con las entradas indicadas.
Las líneas del menú se omiten; `Opción:` indica cada vuelta del menú.

## 1. Listar sin productos

Esperado: Mostrar mensaje de inventario vacío.

Entradas: `2 | 0`

```text
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 2. Registrar P001

Esperado: Se agrega.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## 3. Registrar P001 nuevamente

Esperado: Rechazar código repetido.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 1 | P001 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: El código ya está registrado.
Opción: P001 - Teclado - Periféricos - $85000.0 - 4 unidades
Opción: Programa finalizado.
```

## 4. Registrar código vacío

Esperado: Rechazar.

Entradas: `1 |     | 2 | 0`

```text
Opción: Código: El código no puede estar vacío.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 5. Registrar nombre vacío o solo espacios

Esperado: Rechazar.

Entradas: `1 | P004 |     | Accesorios | 1000 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: El nombre no puede estar vacío.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 6. Registrar categoría fuera de la tupla

Esperado: Rechazar.

Entradas: `1 | P004 | Silla | Muebles | 1000 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Categoría no permitida.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 7. Registrar precio negativo

Esperado: Rechazar.

Entradas: `1 | P004 | Cable | Accesorios | -500 | 1 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: El precio debe ser mayor que cero.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 8. Registrar cantidad negativa

Esperado: Rechazar.

Entradas: `1 | P004 | Cable | Accesorios | 500 | -2 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: La cantidad no puede ser negativa.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 9. Registrar cantidad cero

Esperado: Aceptar como producto sin stock.

Entradas: `1 | P002 | Mouse | Periféricos | 45000 | 0 | 6 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Sin existencias:
- Mouse
Opción: Programa finalizado.
```

## 10. Buscar P001

Esperado: Mostrar su registro.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 3 | P001 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Código: P001
Nombre: Teclado
Categoría: Periféricos
Precio: 85000.0
Cantidad: 4
Opción: Programa finalizado.
```

## 11. Buscar código desconocido

Esperado: Informar que no existe.

Entradas: `3 | P999 | 0`

```text
Opción: Código: No se encontró el producto.
Opción: Programa finalizado.
```

## 12. Actualizar a 10 unidades

Esperado: Cambiar solamente la cantidad.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 4 | P001 | 10 | 3 | P001 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nueva cantidad: Cantidad actualizada.
Opción: Código: Código: P001
Nombre: Teclado
Categoría: Periféricos
Precio: 85000.0
Cantidad: 10
Opción: Programa finalizado.
```

## 13. Actualizar a -3 unidades

Esperado: Conservar la cantidad anterior.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 4 | P001 | -3 | 3 | P001 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nueva cantidad: La cantidad no puede ser negativa.
Opción: Código: Código: P001
Nombre: Teclado
Categoría: Periféricos
Precio: 85000.0
Cantidad: 4
Opción: Programa finalizado.
```

## 14. Eliminar un producto existente

Esperado: Borrar el registro.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 5 | P001 | 2 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Producto eliminado.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 15. Eliminar código inexistente

Esperado: No fallar.

Entradas: `5 | P999 | 2 | 0`

```text
Opción: Código: No se encontró el producto.
Opción: No hay productos registrados.
Opción: Programa finalizado.
```

## 16. Consultar resumen

Esperado: Reflejar los datos actuales.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 7 | 4 | P001 | 1 | 7 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Productos: 1
Unidades: 4
Valor del inventario: $340000.0
Categorías utilizadas (1): Periféricos
Opción: Código: Nueva cantidad: Cantidad actualizada.
Opción: Productos: 1
Unidades: 1
Valor del inventario: $85000.0
Categorías utilizadas (1): Periféricos
Opción: Programa finalizado.
```

## 17. Salir

Esperado: Finalizar el ciclo.

Entradas: `9 | 0`

```text
Opción: Opción no válida.
Opción: Programa finalizado.
```

## Comprobación numérica

Esperado: 3 productos, 6 unidades, valor de $1.740.000, 2 categorías y P002 (Mouse) sin stock.

Cálculo manual: 85000 × 4 + 45000 × 0 + 700000 × 2 = 340000 + 0 + 1400000 = 1740000.

Entradas: `1 | P001 | Teclado | Periféricos | 85000 | 4 | 1 | P002 | Mouse | Periféricos | 45000 | 0 | 1 | P003 | Monitor | Componentes | 700000 | 2 | 6 | 7 | 0`

```text
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Código: Nombre: Categoría: Precio: Cantidad: Producto registrado.
Opción: Sin existencias:
- Mouse
Opción: Productos: 3
Unidades: 6
Valor del inventario: $1740000.0
Categorías utilizadas (2): Componentes, Periféricos
Opción: Programa finalizado.
```
