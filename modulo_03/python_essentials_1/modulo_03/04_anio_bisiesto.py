"""
Lab 04 · Año bisiesto (if-elif-else)
Python Essentials 1 · sección 3.1.12
Enunciado: modulo_03/README.md
"""
year = int(input("introduce un año:"))

if year < 1582:
    print("No dentro del período del calendario gregoriano")
elif year % 4 != 0:
    print("Año comun")
else:
    print("Año bisiesto")
    

