# Módulo 3 — Condicionales, bucles y listas

| # | Archivo | Sección | Hecho |
|---|---|---|---|
| 01 | `01_mayor_igual_100.py` | 3.1.6 | ☐ |
| 02 | `02_espatifilo.py` | 3.1.10 | ☐ |
| 03 | `03_impuestos.py` | 3.1.11 | ☐ |
| 04 | `04_anio_bisiesto.py` | 3.1.12 | ☐ |

## 01 · Comparación sin if
`01_mayor_igual_100.py` · sección 3.1.6

Lee un entero `n` y muestra `True` si es mayor o igual que 100, o `False` si es menor.

- Máximo **dos líneas** de código.
- **Sin** `if`: usa solo un operador de comparación.

| Entrada | Salida |
|---|---|
| `55` | `False` |
| `99` | `False` |
| `100` | `True` |
| `101` | `True` |
| `-5` | `False` |
| `+123` | `True` |

## 02 · Espatifilo (if-elif-else con strings)
`02_espatifilo.py` · sección 3.1.10

Lee una palabra y responde según cómo esté escrita:

- `Espatifilo` → `Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!`
- `espatifilo` → `No, ¡quiero un gran Espatifilo!`
- Cualquier otra → `¡Espatifilo!, ¡No <entrada>!`

| Entrada | Salida |
|---|---|
| `espatifilo` | `No, ¡quiero un gran Espatifilo!` |
| `pelargonio` | `¡Espatifilo!, ¡No pelargonio!` |
| `Espatifilo` | `Si, ¡El Espatifilo! es la mejor planta de todos los tiempos!` |

> El enunciado original menciona `"ESPATIFILIO"` en mayúsculas, pero los datos de prueba usan `Espatifilo`. Aquí se sigue la tabla.

## 03 · Calculadora de impuestos (if-else)
`03_impuestos.py` · sección 3.1.11

Lee el ingreso anual (`float`) y muestra el impuesto redondeado a pesos enteros con `round()`.

- Ingreso **≤ 85 528**: 18 % del ingreso − 556,02.
- Ingreso **> 85 528**: 14 839,02 + 32 % de lo que exceda de 85 528.
- Si el resultado es **negativo**, el impuesto es `0.0`.

Formato: `El impuesto es: <valor> pesos`

| Entrada | Salida |
|---|---|
| `10000` | `El impuesto es: 1244.0 pesos` |
| `100000` | `El impuesto es: 19470.0 pesos` |
| `1000` | `El impuesto es: 0.0 pesos` |
| `-100` | `El impuesto es: 0.0 pesos` |

## 04 · Año bisiesto (if-elif-else)
`04_anio_bisiesto.py` · sección 3.1.12

Lee un año e indica si es bisiesto o común según la regla gregoriana:

1. No divisible entre 4 → común.
2. Si no, no divisible entre 100 → bisiesto.
3. Si no, no divisible entre 400 → común.
4. Si no → bisiesto.

Si el año es anterior a 1582, muestra un aviso en lugar del resultado. Pista: `%` y `!=`.

| Entrada | Salida |
|---|---|
| `2000` | `Año bisiesto` |
| `2015` | `Año comun` |
| `1999` | `Año comun` |
| `1996` | `Año bisiesto` |
| `1580` | `No dentro del período del calendario gregoriano` |
