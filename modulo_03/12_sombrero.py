"""
Lab 12 · Los fundamentos de las listas (sombrero)
Python Essentials 1 · sección 3.4.6
Enunciado: modulo_03/README.md
"""

hat_list = [1, 2, 3, 4, 5]  # Lista de números ocultos en el sombrero.

hat_list[2] = int(input("Introduce un entero: "))

del hat_list[4]

print(hat_list)
