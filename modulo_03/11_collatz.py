"""
Lab 11 · Hipótesis de Collatz (while)
Python Essentials 1 · sección 3.2.15
Enunciado: modulo_03/README.md
"""
pasos=0
c0 =int(input("Introduce un numero: "))

while c0 != 1:
    if c0 % 2 == 0 :
        c0 = c0 // 2
        pasos+=1
        print(c0)
    else:
        c0 = 3 * c0 + 1
        pasos+=1
        print(c0)
print("Pasos: ",pasos)

