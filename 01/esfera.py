# Escribí un programa que le pida a le usuarie que ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma.
# Sugerencia: recordar que el volumen de una esfera es 4/3 π r^3.
# ¿Cuál es el volumen de una esfera de radio 6?

import math
radius = input("Enter the sphere radius: ")
volume = 4/3 * math.pi * float(radius)**3
print(f'The sphere volume is {round(volume, 2)}')
