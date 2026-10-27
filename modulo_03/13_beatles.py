"""
Lab 13 · Los fundamentos de las listas: los Beatles
Python Essentials 1 · sección 3.4.11
Enunciado: modulo_03/README.md
"""

# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon") 
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    newBeatles = input("Añade a Stu Sutcliffe y  despues a Pete Best: ")
    beatles.append(newBeatles)    
    
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)

# probando la longitud de la lista
print("Los Fab", len(beatles))
