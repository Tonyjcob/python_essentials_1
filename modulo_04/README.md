# Módulo 4 — Funciones, tuplas, diccionarios y excepciones

| # | Archivo | Sección | Hecho |
|---|---|---|---|
| 01 | `01_anio_bisiesto.py` | 4.3.4 | ☐ |
| 02 | `02_dias_del_mes.py` | 4.3.5 | ☐ |
| 03 | `03_dia_del_anio.py` | 4.3.6 | ☐ |
| 04 | `04_numeros_primos.py` | 4.3.7 | ☐ |
| 05 | `05_consumo_combustible.py` | 4.3.8 | ☐ |

## 01 · Año bisiesto (función)
`01_anio_bisiesto.py` · sección 4.3.4

Escribe la función `is_year_leap(year)`: recibe un año y devuelve `True` si es bisiesto o `False` si no.

Reglas (las mismas del lab de bisiesto del módulo 3):

- Divisible entre 4 → bisiesto…
- …salvo que sea divisible entre 100 → no bisiesto…
- …salvo que sea divisible entre 400 → bisiesto.

El esqueleto trae un código de prueba con dos listas (datos y resultados esperados) que imprime `OK` o `Fallido` por cada caso.

| Año | Resultado |
|---|---|
| `1900` | `False` |
| `2000` | `True` |
| `2016` | `True` |
| `1987` | `False` |

Salida esperada:

```
1900 ->OK
2000 ->OK
2016 ->OK
1987 ->OK
```

## 02 · Días del mes
`02_dias_del_mes.py` · sección 4.3.5

Escribe la función `days_in_month(year, month)`: devuelve el número de días de ese mes en ese año.

- Solo febrero depende del año, pero la función debe valer para cualquier mes.
- **Reutiliza** `is_year_leap()` del lab 01 (cópiala en este archivo).
- Devuelve `None` si los argumentos no tienen sentido (p. ej. mes fuera de 1–12).
- Truco recomendado: una lista con los días de cada mes creada dentro de la función.
- Amplía el código de prueba con más casos.

| Año | Mes | Resultado |
|---|---|---|
| `1900` | `2` | `28` |
| `2000` | `2` | `29` |
| `2016` | `1` | `31` |
| `1987` | `11` | `30` |
| `2000` | `13` | `None` |

> El curso dice "LAB 4.3.1.6" al referirse a la función bisiesto; es el 4.3.4 (lab 01).

## 03 · Día del año
`03_dia_del_anio.py` · sección 4.3.6

Escribe la función `day_of_year(year, month, day)`: devuelve qué número de día del año es esa fecha (1–365/366).

- Devuelve `None` si **cualquier** argumento no es válido (mes inexistente, día fuera de rango para ese mes…).
- Usa las funciones de los labs 01 y 02.
- Añade tus propios casos de prueba.

| Llamada | Resultado |
|---|---|
| `day_of_year(2000, 12, 31)` | `366` |
| `day_of_year(2001, 12, 31)` | `365` |
| `day_of_year(2000, 2, 30)` | `None` |

## 04 · Números primos
`04_numeros_primos.py` · sección 4.3.7

Escribe la función `is_prime(num)`: devuelve `True` si `num` es primo y `False` si no.

- Primo = natural **mayor que 1** cuyos únicos divisores son 1 y él mismo.
- Pista: divide entre 2, 3, 4… y mira el resto (`%`). Si alguno da 0, no es primo.
- Piensa **cuándo parar**: no hace falta llegar hasta `num`. Raíz cuadrada → `x ** 0.5`.

Salida esperada del código de prueba:

```
2 3 5 7 11 13 17 19
```

## 05 · Conversión de consumo de combustible
`05_consumo_combustible.py` · sección 4.3.8

Escribe dos funciones de un argumento:

- `liters_100km_to_miles_gallon(liters)` → convierte **l/100 km** a **mpg** (millas por galón).
- `miles_gallon_to_liters_100km(miles)` → convierte **mpg** a **l/100 km**.

Datos:

- 1 milla = 1609.344 m
- 1 galón = 3.785411784 l

Salida esperada:

```
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757
```

> El último decimal puede variar (p. ej. `...915` en vez de `...916`) según el orden de las operaciones. Es redondeo de coma flotante, no un error.
