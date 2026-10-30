"""
Lab 05 · Conversión de consumo de combustible
Python Essentials 1 · sección 4.3.8
Enunciado: modulo_04/README.md
"""

METROS_POR_MILLA = 1609.344     
LITROS_POR_GALON = 3.785411784  


def liters_100km_to_miles_gallon(liters):
    galones = liters / LITROS_POR_GALON        
    millas = 100 * 1000 / METROS_POR_MILLA     
    return millas / galones


def miles_gallon_to_liters_100km(miles):
    km100 = miles * METROS_POR_MILLA / 100000  
    litros = LITROS_POR_GALON                  
    return litros / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
