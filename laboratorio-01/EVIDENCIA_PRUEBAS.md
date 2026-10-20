# Evidencia de pruebas del cotizador de compra

Generado con `python pruebas_cotizador.py`. Cada caso ejecuta `cotizador_compra.py` con las entradas indicadas.

| Caso | Precio | Cantidad | Descuento | Impuesto | Esperado | Obtenido | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| Ejemplo de la guía | 180000 | 2 | 10 % | 19 % | 385560.0 | 385560.0 | Correcto |
| Caso 1 | 100000 | 2 | 10 % | 0 % | 180000.0 | 180000.0 | Correcto |
| Caso 2 | 50000 | 3 | 0 % | 0 % | 150000.0 | 150000.0 | Correcto |
| Caso 3 | 80000 | 5 | 25 % | 0 % | 300000.0 | 300000.0 | Correcto |
| Caso 4 | 100000 | 1 | 0 % | 19 % | 119000.0 | 119000.0 | Correcto |

Cálculo manual del caso 4: subtotal = 100000 × 1 = 100000; descuento = 0; base = 100000; impuesto = 100000 × 19 / 100 = 19000; total = 100000 + 19000 = 119000.

## Ejemplo de la guía

Entradas: `Laura | Teclado mecánico | 180000 | 2 | 10 | 19`

```text
=============================
      COTIZADOR PYTHON
=============================
Nombre del cliente: Producto: Precio unitario: Cantidad: Descuento (%): Impuesto (%): 
-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Laura
Producto: Teclado mecánico
Precio unitario: $180000.0
Cantidad: 2
Subtotal: $360000.0
Descuento: $36000.0
Base: $324000.0
Impuesto: $61560.0
TOTAL: $385560.0
```

## Caso 1

Entradas: `Ana | Mouse | 100000 | 2 | 10 | 0`

```text
=============================
      COTIZADOR PYTHON
=============================
Nombre del cliente: Producto: Precio unitario: Cantidad: Descuento (%): Impuesto (%): 
-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Ana
Producto: Mouse
Precio unitario: $100000.0
Cantidad: 2
Subtotal: $200000.0
Descuento: $20000.0
Base: $180000.0
Impuesto: $0.0
TOTAL: $180000.0
```

## Caso 2

Entradas: `Luis | Audífonos | 50000 | 3 | 0 | 0`

```text
=============================
      COTIZADOR PYTHON
=============================
Nombre del cliente: Producto: Precio unitario: Cantidad: Descuento (%): Impuesto (%): 
-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Luis
Producto: Audífonos
Precio unitario: $50000.0
Cantidad: 3
Subtotal: $150000.0
Descuento: $0.0
Base: $150000.0
Impuesto: $0.0
TOTAL: $150000.0
```

## Caso 3

Entradas: `Marta | Monitor | 80000 | 5 | 25 | 0`

```text
=============================
      COTIZADOR PYTHON
=============================
Nombre del cliente: Producto: Precio unitario: Cantidad: Descuento (%): Impuesto (%): 
-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Marta
Producto: Monitor
Precio unitario: $80000.0
Cantidad: 5
Subtotal: $400000.0
Descuento: $100000.0
Base: $300000.0
Impuesto: $0.0
TOTAL: $300000.0
```

## Caso 4

Entradas: `Pedro | Teclado | 100000 | 1 | 0 | 19`

```text
=============================
      COTIZADOR PYTHON
=============================
Nombre del cliente: Producto: Precio unitario: Cantidad: Descuento (%): Impuesto (%): 
-----------------------------
RESUMEN DE COMPRA
-----------------------------
Cliente: Pedro
Producto: Teclado
Precio unitario: $100000.0
Cantidad: 1
Subtotal: $100000.0
Descuento: $0.0
Base: $100000.0
Impuesto: $19000.0
TOTAL: $119000.0
```

