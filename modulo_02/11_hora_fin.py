"""
Lab 11 · Hora de fin
Python Essentials 1 · sección 2.6
Enunciado: modulo_02/README.md
"""

h = int(input("introduce la hora de inicio: "))
m = int(input("introduce los minutos de inicio: "))
d = int(input("introduce la duración del evento en minutos: "))

print(((h+(d+m)//60)%24),":",((m+d)%60))