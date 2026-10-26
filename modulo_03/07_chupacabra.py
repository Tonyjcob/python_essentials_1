"""
Lab 07 · Atrapado en un bucle (break)
Python Essentials 1 · sección 3.2.9
Enunciado: modulo_03/README.md
"""
palabra = input()
while True:
    if palabra =="chupacabra":
            break
    if palabra != "chupacabra":
        palabra = input()    
print("Has dejado el bucle con exito")
