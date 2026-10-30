"""
Lab 14 · Operaciones con listas: eliminar repeticiones
Python Essentials 1 · sección 3.6.6
Enunciado: modulo_03/README.md
"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for numero in my_list:
      if numero not in new_list:
          new_list.append(numero)
print("La lista con elementos únicos:")
print(new_list)
