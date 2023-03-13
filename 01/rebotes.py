# Una pelota de goma es arrojada desde una altura de 100 m y cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
# Escribí un programa que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

h = 100
for i in range(10):
    h = round(h * 3/5, 4)
    print(h)
