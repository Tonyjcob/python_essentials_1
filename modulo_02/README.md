# Módulo 2 — Tipos de datos, variables, operadores, E/S

| # | Archivo | Sección | Hecho |
|---|---|---|---|
| 01 | `01_print_basico.py` | 2.1 | ☐ |
| 02 | `02_print_sep_end.py` | 2.1 | ☐ |
| 03 | `03_flecha.py` | 2.1 | ☐ |
| 04 | `04_literales_strings.py` | 2.2 | ☐ |
| 05 | `05_variables_manzanas.py` | 2.4 | ☐ |
| 06 | `06_millas_km.py` | 2.4 | ☐ |
| 07 | `07_polinomio.py` | 2.4 | ☐ |
| 08 | `08_comentarios.py` | 2.5 | ☐ |
| 09 | `09_entrada_salida.py` | 2.6 | ☐ |
| 10 | `10_fraccion_continua.py` | 2.6 | ☐ |
| 11 | `11_hora_fin.py` | 2.6 | ☐ |

## 01 · print() básico
`01_print_basico.py` · sección 2.1

Muestra una frase con `print()`.
- Prueba comillas simples y dobles.
- Quita los paréntesis o las comillas y observa el error.
- Imprime varias líneas con varias llamadas.

## 02 · print() con sep y end
`02_print_sep_end.py` · sección 2.1

A partir de las cadenas `"Programming"`, `"Essentials"`, `"in"` y `"Python"`, obtén exactamente:
```
Programming***Essentials***in...Python
```
Usa solo los parámetros `sep` y `end` (máx. 2 `print()`).

## 03 · Formatear la salida (flecha)
`03_flecha.py` · sección 2.1

Dibuja esta flecha con `print()`:
```
    *
   * *
  *   *
 *     *
***   ***
  *   *
  *   *
  *****
```
- Reduce al mínimo el número de `print()` (pista: `\n`).
- Haz una versión al doble de tamaño.

## 04 · Literales (strings)
`04_literales_strings.py` · sección 2.2

Con **una sola línea** de código, imprime:
```
"I'm"
""learning""
"""Python"""
```
Pista: secuencias de escape (`\"`, `\'`, `\n`).

## 05 · Variables (manzanas)
`05_variables_manzanas.py` · sección 2.4

- Crea `john`, `mary`, `adam` con 3, 5 y 6 manzanas.
- Imprímelas en una línea separadas por comas.
- Crea `total_apples` con la suma y muéstrala.
- Experimenta: usa una variable sin definir, nombres no válidos…

## 06 · Millas ↔ km
`06_millas_km.py` · sección 2.4

`1 milla = 1.61 km`. Con `kilometers = 12.25` y `miles = 7.38`, calcula las conversiones y muestra:
```
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas
```
Redondea a 2 decimales.

## 07 · Polinomio
`07_polinomio.py` · sección 2.4

Calcula `y = 3x³ − 2x² + 3x − 1` para un `x` float.

| x | y |
|---|---|
| 0.0 | -1.0 |
| 1.0 | 3.0 |
| -1.0 | -9.0 |

## 08 · Comentarios
`08_comentarios.py` · sección 2.5

Arregla este programa: elimina comentarios inútiles o falsos, renombra variables para que se entiendan solas, descomenta lo necesario y añade el `print` que falta.
```python
#este programa calcula los segundos de 2 horas
#escrito hace 2 días
a = 2 # horas
b = 3600 # segundos en 1 hora
print("Horas: ", a) #imprime horas
# print("Segundos en horas: ", a * b)
#aquí debería decir "Adiós" pero no dio tiempo
#fin del programa que calcula los segundos de 3 horas
```

## 09 · Entrada y salida simple
`09_entrada_salida.py` · sección 2.6

Pide dos números `float` (`a` y `b`) y muestra su suma, resta, multiplicación y división. Termina con un mensaje de despedida.

## 10 · Fracción continua
`10_fraccion_continua.py` · sección 2.6

Pide `x` (float) y evalúa:
```
1 / (x + 1 / (x + 1 / (x + 1 / x)))
```
Usa variables intermedias para que sea legible.

| x | resultado |
|---|---|
| 1 | 0.6000000000000001 |
| 10 | 0.09901951266867294 |
| 100 | 0.009999000199950014 |
| -5 | -0.19258202567760344 |

## 11 · Hora de fin
`11_hora_fin.py` · sección 2.6

Pide hora de inicio (`h`, `m`) y duración en minutos. Muestra la hora de fin en formato `h:m` (24 h, sin ceros a la izquierda). Sin `if`: solo `//`, `%`.

| inicio | duración | fin |
|---|---|---|
| 12:17 | 59 | 13:16 |
| 23:58 | 642 | 10:40 |
| 0:01 | 2939 | 1:0 |
