"""
Lab 09 · El Lindo Devorador de Vocales (continue + concatenación)
Python Essentials 1 · sección 3.2.11
Enunciado: modulo_03/README.md
"""

word_without_vowels = ""

# Pide al usuario que introduzca una palabra
# y asígnala a la variable user_word.
palabra = input("Introduce una palabra: ")
palabra = palabra.upper()
for letter in palabra:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter== "U":    
        continue
    else:
        word_without_vowels += letter 
print(word_without_vowels)

# Imprime la palabra asignada a word_without_vowels.

