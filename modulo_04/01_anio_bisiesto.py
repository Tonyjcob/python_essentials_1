"""
Lab 01 · Año bisiesto (función)
Python Essentials 1 · sección 4.3.4
Enunciado: modulo_04/README.md
"""

def is_year_leap(yr):
    if yr % 400 == 0:
        return(True)
    elif yr % 100 == 0:
        return(False)
    elif yr % 4 == 0:
        return(True)
    else:
        return(False)


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
