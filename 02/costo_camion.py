# Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo.
# Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.
# Ayuda: para interpretar un string s como un número entero, usa int(s). Para leerlo como punto flotante, usá float(s).

# version 1
costo = 0
with open('camion.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        cajones = int(row[1])
        precio = float(row[2].rstrip(row[2][-2]))
        costo += cajones * precio
print(f'Costo total {costo}')

# versión 2: con funcion
def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precio_total = 0
        headers = next(f)
        try:
            for line in f:
                row = line.split(',')
                cajon = int(row[1])
                precio = float(row[2])
                precio_total += round(cajon * precio)
            return costo
        except ValueError:
            print("archivo con datos invalidos, verifique")

costo = costo_camion('camion.csv')
print(costo)

# versión 3: con csv
import csv
def costo_camion2(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precio_total = 0
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                cajon = int(row[1])
                precio = float(row[2])
                precio_total += round(cajon * precio)
            return costo
        except ValueError:
            print("archivo con datos invalidos, verifique")


costo = costo_camion2('camion.csv')
print(costo)

# versión 4: con sys
import csv
import sys

def costo_camion2(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precio_total = 0
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                cajon = int(row[1])
                precio = float(row[2])
                precio_total += round(cajon * precio)
            return costo
        except ValueError:
            print("archivo con datos invalidos, verifique")

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)



# versión 5: con tuplas
import csv
def costo_camion3(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precio_total = 0
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                t = (row[0], int(row[1]), float(row[2]))
                nombre, cajones, precio = t
                precio_total += round(cajones*precio) #ó round(t[1]*t[2])
            return costo
        except ValueError:
            print("archivo con datos invalidos, verifique")

costo = costo_camion3('camion.csv')
print(costo)


#versión 6: con diccionarios
import csv
def costo_camion3(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        precio_total = 0
        rows = csv.reader(f)
        headers = next(rows)
        try:
            for row in rows:
                d = {
                    'nombre' : row[0],
                    'cajones' : int(row[1]),
                    'precio': float(row[2])
                }
                precio_total += round(d['cajones']*d['precio'])
            return costo
        except ValueError:
            print("archivo con datos invalidos, verifique")

costo = costo_camion3('camion.csv')
print(costo)
