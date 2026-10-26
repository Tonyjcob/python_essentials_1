"""
Lab 05 · Adivina el número secreto (while)
Python Essentials 1 · sección 3.2.4
Enunciado: modulo_03/README.md
"""

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle! |
| Introduce un número entero      |
| y adivina qué número he         |
| elegido para ti.                |
| Entonces,                       |
| ¿Cuál es el número secreto?     |
+================================+
""")
guess_number=int(input())
while secret_number != guess_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    guess_number=int(input("¿Cuál es el número secreto?: "))
print("¡Bien hecho, muggle! Eres libre ahora.")