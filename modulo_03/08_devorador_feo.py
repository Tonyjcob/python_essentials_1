"""
Lab 08 · El Feo Devorador de Vocales (continue)
Python Essentials 1 · sección 3.2.10
Enunciado: modulo_03/README.md
"""
palabra = input("Introduce una palabra: ")
palabra = palabra.upper()
for letra in palabra:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":    
        continue
    else:
        print(letra)