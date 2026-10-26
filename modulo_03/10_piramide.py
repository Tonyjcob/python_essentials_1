"""
Lab 10 · Pirámide de bloques (while)
Python Essentials 1 · sección 3.2.14
Enunciado: modulo_03/README.md
"""
altura = 0
bloques = int(input("Introduce el número de bloques: "))

while bloques >= altura + 1:
    altura += 1
    bloques -= altura
    
print("La altura de la pirámide es:", altura)
