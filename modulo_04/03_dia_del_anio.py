"""
Lab 03 · Día del año
Python Essentials 1 · sección 4.3.6
Enunciado: modulo_04/README.md
"""

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

def day_of_year(year, month, day):
    max_day = days_in_month(year, month)
    
    if max_day is None:
            return None

    if type(day) != int or day < 1 or day > max_day:
        return None

    total = 0
    for m in range(1, month):
        total += days_in_month(year, m)

    return total + day

test_cases = [
    (2000, 12, 31, 366),    
    (2001, 12, 31, 365),    
    (2000, 2, 30, None),    
    (2001, 2, 29, None),    
    (2000, 3, 1, 61),       
]

for year, month, day, expected in test_cases:
    print(year, month, day, "->", end=" ")
    result = day_of_year(year, month, day)
    if result == expected:
        print("OK")
    else:
        print("Fallido (esperado", expected, "obtenido", result, ")")