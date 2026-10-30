"""
Lab 02 · Días del mes
Python Essentials 1 · sección 4.3.5
Enunciado: modulo_04/README.md
"""

# 02_dias_del_mes.py · sección 4.3.5
# Días del mes: devuelve el número de días de un mes en un año dado.


def is_year_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if type(year) != int or type(month) != int:
        return None
    if month < 1 or month > 12 or year < 1582:
        return None

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return days[month - 1]


test_years   = [1900, 2000, 2016, 1987, 2000]
test_months  = [2,    2,    1,    11,   13]
test_results = [28,   29,   31,   30,   None]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end=" ")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido (esperado", test_results[i], "obtenido", result, ")")