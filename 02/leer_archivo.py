# Primero, tratá de leer el archivo entero de una en una larga cadena:
with open('camion.csv', 'rt') as f:
    data = f.read()
print(data)

# Para leer una archivo línea por línea, usá un ciclo for:
with open('camion.csv', 'rt') as f:
    for line in f:
        print(line, end = '')
print('\n')

# En ciertas ocasiones, puede pasar que quieras leer una sola línea de texto (por ejemplo, querés saltearte la primera línea del archivo que contiene los nombres de las columnas).
with open('camion.csv', 'rt') as f:
    headers = next(f) # next() devuelve la siguiente línea de texto en el archivo.
    for line in f:
        print(line, end = '')
print('\n')

# Una vez que estés leyendo un archivo línea a línea, podés hacer otras operaciones, como separar los datos dentro de una línea con el método split().
f = open('camion.csv', 'rt')
headers = next(f).split(',')
print(headers)
for line in f:
    row = line.split(',')
    print(row)
f.close()
print('\n')

# Archivos comprimidos
import gzip
with gzip.open('camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
