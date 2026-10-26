"""
Lab 03 · Calculadora de impuestos (if-else)
Python Essentials 1 · sección 3.1.11
Enunciado: modulo_03/README.md
"""

ingreso = float(input("Introduce tus ingresos: "))

if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = 14839.02 + (ingreso - 85528) * 0.32

if impuesto < 0.0:
    impuesto = 0.0
impuesto = round(impuesto, 0)

print("El impuesto es:", impuesto, "pesos")