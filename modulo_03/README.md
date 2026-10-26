# Módulo 3 — Condicionales, bucles y listas

| # | Archivo | Sección | Hecho |
|---|---|---|---|
| 01 | `01_mayor_igual_100.py` | 3.1.6 | ☐ |
| 02 | `02_espatifilo.py` | 3.1.10 | ☐ |
| 03 | `03_impuestos.py` | 3.1.11 | ☐ |
| 04 | `04_anio_bisiesto.py` | 3.1.12 | ☐ |
| 05 | `05_numero_secreto.py` | 3.2.4 | ☐ |
| 06 | `06_mississippi.py` | 3.2.7 | ☐ |
| 07 | `07_chupacabra.py` | 3.2.9 | ☐ |
| 08 | `08_devorador_feo.py` | 3.2.10 | ☐ |
| 09 | `09_devorador_lindo.py` | 3.2.11 | ☐ |
| 10 | `10_piramide.py` | 3.2.14 | ☐ |
| 11 | `11_collatz.py` | 3.2.15 | ☐ |

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

## 05 · Adivina el número secreto (while)
`05_numero_secreto.py` · sección 3.2.4

El número secreto está en `secret_number`. Pide un entero al usuario con un bucle `while`:

- Si **no** acierta → `¡Ja, ja! ¡Estás atrapado en mi bucle!` y vuelve a pedir.
- Si acierta → imprime el número y `¡Bien hecho, muggle! Eres libre ahora.`

El archivo ya trae `secret_number` y el mensaje de bienvenida con `print` multilínea (`"""..."""`).

| Entradas (`secret_number = 777`) | Salida |
|---|---|
| `5` | `¡Ja, ja! ¡Estás atrapado en mi bucle!` |
| `777` | `777` + `¡Bien hecho, muggle! Eres libre ahora.` |

## 06 · Contando mississippily (for)
`06_mississippi.py` · sección 3.2.7

Usa un bucle `for` para contar hasta 5 añadiendo `Mississippi`, con una pausa de 1 s entre líneas (`time.sleep(1)`, ya importado). Al terminar, imprime el mensaje final.

Salida esperada:

```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
¡Listos o no, ahí voy!
```

> El enunciado y la salida del curso no coinciden en la frase final (`¡Listos o no, ahí voy!` / `Lista o no, aquí vengo!`). Cualquiera vale.

## 07 · Atrapado en un bucle (break)
`07_chupacabra.py` · sección 3.2.9

Con un bucle `while`, pide palabras al usuario sin parar hasta que escriba `chupacabra`. Entonces imprime `Has dejado el bucle con éxito.` y termina.

- **No** imprimas las palabras introducidas.
- Usa `if` + `break`.

| Entradas | Salida |
|---|---|
| `hola`, `python`, `chupacabra` | `Has dejado el bucle con éxito.` |

## 08 · El Feo Devorador de Vocales (continue)
`08_devorador_feo.py` · sección 3.2.10

Pide una palabra, pásala a mayúsculas con `user_word = user_word.upper()` y recórrela con `for`. Usa `if-elif-else` + `continue` para "comerse" las vocales `A E I O U`. Imprime cada letra restante **en una línea**.

| Entrada | Salida |
|---|---|
| `Gregory` | `G` `R` `G` `R` `Y` (una por línea) |
| `abstemious` | `B` `S` `T` `M` `S` (una por línea) |
| `IOUEA` | *(nada)* |

## 09 · El Lindo Devorador de Vocales (continue + concatenación)
`09_devorador_lindo.py` · sección 3.2.11

Igual que el anterior, pero en vez de imprimir letra a letra, **concatena** las letras no consumidas en `word_without_vowels` (ya creada vacía) e imprime la variable al final.

| Entrada | Salida |
|---|---|
| `Gregory` | `GRGRY` |
| `abstemious` | `BSTMS` |
| `IOUEA` | *(línea vacía)* |

## 10 · Pirámide de bloques (while)
`10_piramide.py` · sección 3.2.14

Lee el número de bloques y calcula la **altura** de una pirámide plana: la capa de arriba tiene 1 bloque, la siguiente 2, luego 3…

- Solo cuentan las capas **completas**: si no hay bloques suficientes para la siguiente, se para.

Formato: `La altura de la pirámide es: <altura>`

| Entrada | Salida |
|---|---|
| `6` | `La altura de la pirámide es: 3` |
| `20` | `La altura de la pirámide es: 5` |
| `1000` | `La altura de la pirámide es: 44` |
| `2` | `La altura de la pirámide es: 1` |

## 11 · Hipótesis de Collatz (while)
`11_collatz.py` · sección 3.2.15

Lee un natural `c0` (> 0) y repite mientras `c0 != 1`:

- Si es **par** → `c0 = c0 // 2`
- Si es **impar** → `c0 = 3 * c0 + 1`

Imprime cada valor intermedio en una línea y, al final, el número de pasos: `pasos = <n>`.

| Entrada | Salida |
|---|---|
| `16` | `8` `4` `2` `1` (una por línea) + `pasos = 4` |
| `15` | `46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1` (una por línea) + `pasos = 17` |
| `1023` | ver abajo + `pasos = 62` |

<details><summary>Salida completa para <code>1023</code></summary>

```
3070
1535
4606
2303
6910
3455
10366
5183
15550
7775
23326
11663
34990
17495
52486
26243
78730
39365
118096
59048
29524
14762
7381
22144
11072
5536
2768
1384
692
346
173
520
260
130
65
196
98
49
148
74
37
112
56
28
14
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
pasos = 62
```
</details>

> Los datos de prueba del curso tienen erratas (`46` repetido en vez de `23`; en `1023` faltan `520`, `112` y el `1` final). Estas salidas están comprobadas ejecutando el algoritmo.
