# Laboratorios de Python — Explorer, Integrator, Innovator

**Aprendiz:** Jader Alonso Posso Tuberquia — **Ficha:** 3388087

Repositorio acumulativo con los ejercicios y proyectos de los cuatro laboratorios. Cada carpeta conserva su versión del proyecto, para comparar cómo evolucionó el gestor de inventario: desde un script con listas y diccionarios hasta una aplicación orientada a objetos que guarda sus datos en JSON.

Requisitos: Python 3.8 o superior. No hay dependencias externas. Según el equipo, el comando puede ser `python`, `py` o `python3`.

| Laboratorio | Tema | Proyecto final | Cómo ejecutarlo |
|---|---|---|---|
| [Laboratorio 01](laboratorio-01/README.md) | Variables, tipos, operadores e `input()` | Cotizador de compra | `cd laboratorio-01` → `python cotizador_compra.py` |
| [Laboratorio 02](laboratorio-02/README.md) | Decisiones, ciclos, colecciones y comprensiones | Gestor de inventario en un archivo | `cd laboratorio-02` → `python gestor_inventario.py` |
| [Laboratorio 03](laboratorio-03/) | Funciones, módulos y POO | [Gestor orientado a objetos](laboratorio-03/gestor_inventario/) | `cd laboratorio-03/gestor_inventario` → `python main.py` |
| [Laboratorio 04](laboratorio-04/) | Excepciones, archivos, JSON, CSV y POO intermedia | [Gestor persistente](laboratorio-04/gestor_inventario/) | `cd laboratorio-04/gestor_inventario` → `python main.py` |

Los ejercicios de cada práctica se ejecutan igual, desde su carpeta: `python nombre_del_archivo.py`.

## Estructura

```text
python-laboratorios/
├── README.md
├── laboratorio-01/            ejercicios de las prácticas 1.1 a 1.4, cotizador_compra.py y sus retos
├── laboratorio-02/            ejercicios de las prácticas 2.1 a 2.8, gestor_inventario.py y su depuración
├── laboratorio-03/
│   ├── practica-3-1/ … practica-3-4/
│   └── gestor_inventario/     producto.py, inventario.py, main.py, pruebas_gestor.py
└── laboratorio-04/
    ├── practicas/
    │   └── practica-4-1/ … practica-4-4/
    └── gestor_inventario/     + almacenamiento.py, reportes.py, pruebas_gestor.py
```

## Evolución del gestor de inventario

| Versión | Cómo representa los productos | Qué agregó |
|---|---|---|
| Lab 02 | Lista de diccionarios en un solo archivo | Menú con `while`, validaciones, categorías en una tupla, informes con comprensiones |
| Lab 03 | Objetos `Producto` dentro de un objeto `Inventario` | Responsabilidades separadas en módulos, validación en el constructor, propiedades y encapsulamiento |
| Lab 04 | Las mismas clases, convertidas a diccionarios para JSON | Persistencia entre ejecuciones, exportación CSV, manejo de excepciones y protección de archivos dañados |

## Pruebas

| Laboratorio | Pruebas | Resultado |
|---|---|---|
| 01 | Ejemplo de la guía y los 4 casos del cotizador | 385560.0, 180000.0, 150000.0, 300000.0 y 119000.0, todos correctos. Ver la [evidencia](laboratorio-01/EVIDENCIA_PRUEBAS.md). Se regenera con `python pruebas_cotizador.py` |
| 02 | 16 pruebas obligatorias, código vacío y comprobación numérica | 3 productos, 6 unidades, $1740000.0 y 2 categorías. Ver la [evidencia](laboratorio-02/EVIDENCIA_PRUEBAS.md). Se regenera con `python pruebas_gestor.py` |
| 03 | 17 pruebas obligatorias, comprobación numérica y `pruebas_independencia.py` | $1740000.0 y, tras actualizar P002, $1965000.0. Independencia: `Primero: 1`, `Segundo: 0`. Ver la [evidencia](laboratorio-03/gestor_inventario/EVIDENCIA_PRUEBAS.md). Se regenera con `python pruebas_gestor.py` |
| 04 | 19 pruebas obligatorias, prueba numérica, archivos dañados y error de escritura | Ver el [README del gestor](laboratorio-04/gestor_inventario/README.md) y la [evidencia completa](laboratorio-04/gestor_inventario/EVIDENCIA_PRUEBAS.md). Se regenera con `python pruebas_gestor.py` |
