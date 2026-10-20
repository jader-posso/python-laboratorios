# Laboratorio 01 — Primeros pasos con Python

Ejercicios sobre variables, tipos de datos, operadores y entrada de datos con `input()`, y el reto integrador: un **cotizador de compra** de consola.

## Cotizador de compra

`cotizador_compra.py` pide el cliente, el producto, el precio unitario, la cantidad y los porcentajes de descuento e impuesto (como números enteros: `10` es 10 %). Con esos datos calcula, en este orden:

1. subtotal = precio unitario × cantidad
2. valor del descuento = subtotal × descuento / 100
3. base = subtotal − valor del descuento
4. valor del impuesto = base × impuesto / 100
5. total = base + valor del impuesto

Cada resultado se guarda en una variable antes de mostrarse en el resumen.

| Archivo | Qué es |
|---|---|
| `cotizador_compra.py` | Cotizador pedido en la práctica 1.5 |
| `cotizador_ampliado.py` | Reto de ampliación: vendedor, código de cotización y costo de envío (se suma después del impuesto) |
| `cotizador_depuracion.py` | Reto de depuración: copia con tres errores provocados (sintaxis, nombre inexistente y cálculo incorrecto), ya corregidos y explicados en comentarios |
| `pruebas_cotizador.py` | Ejecuta los casos de prueba y genera `EVIDENCIA_PRUEBAS.md` |

## Ejecución

Requiere Python 3.8 o superior y no usa dependencias externas. Desde esta carpeta:

```
python cotizador_compra.py
python pruebas_cotizador.py
```

Según el equipo, el comando puede ser `python`, `py` o `python3`.

## Pruebas

| Caso | Precio | Cantidad | Descuento | Impuesto | Total esperado | Total obtenido |
|---|---:|---:|---:|---:|---:|---:|
| Ejemplo de la guía | 180000 | 2 | 10 % | 19 % | 385560.0 | 385560.0 |
| 1 | 100000 | 2 | 10 % | 0 % | 180000.0 | 180000.0 |
| 2 | 50000 | 3 | 0 % | 0 % | 150000.0 | 150000.0 |
| 3 | 80000 | 5 | 25 % | 0 % | 300000.0 | 300000.0 |
| 4 | 100000 | 1 | 0 % | 19 % | 119000.0 | 119000.0 |

La salida completa de cada caso está en [EVIDENCIA_PRUEBAS.md](EVIDENCIA_PRUEBAS.md).

## Ejercicios por práctica

| Práctica | Archivos |
|---|---|
| 1.1 Verificación del entorno | `hola_python.py`, `presentacion.py`, `preguntas.py` |
| 1.2 Variables y tipos de datos | `datos_basicos.py`, `perfil_aprendiz.py`, `inventario.py`, `prediccion.py`, `error_variables.py` |
| 1.3 Operadores y expresiones | `operadores.py`, `conversion_tiempo.py`, `calculo_promedio.py`, `calculo_compra.py`, `calculo_salario.py`, `factura_simple.py`, `construccion.py` |
| 1.4 Entrada con `input()` | `saludo.py`, `datos_usuario.py`, `tipo_entrada.py`, `suma_interactiva.py`, `conversor_temperatura.py`, `conversion_unidades.py`, `depuracion.py` |
| 1.5 Reto integrador | `cotizador_compra.py`, `cotizador_ampliado.py`, `cotizador_depuracion.py` |
