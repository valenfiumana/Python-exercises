#Definí una función leer_camion(nombre_archivo) que abre un archivo con el contenido de un camión, lo lee y devuelve la información como una lista de tuplas.
#fragmento de costo_camion.py
import csv

# . . . . . . . con tuplas
def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                lote = (row[0], int(row[1]), float(row[2]))
                camion.append(lote)
            except ValueError:
                print('archivo con datos invalidos, verifique.')
    return camion

camion = leer_camion('camion.csv')
print(camion)
print(camion[0])
print(camion[1][2])

total = 0.0
for s in camion:
    total += s[1] * s[2]
print(total)

# . . . . . . . con diccionario (camion)
def leer_camion2(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                d = {
                    'nombre': row[0],
                    'cajones': int(row[1]),
                    'precio': float(row[2])
                }
                camion.append(d)
            except ValueError:
                print('archivo con datos invalidos, verifique.')
    return camion

camion = leer_camion2('camion.csv')
print(camion)
print(camion[0])
print(camion[1]['nombre'])


# . . . . . . . con diccionario (precios)
import csv
def buscar_precio2(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        d = {}
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                d[row[0]] = float(row[1])
        return d

precios_venta = buscar_precio2('precios.csv')
print(precios_venta)


# Calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia.
#¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

#costo camion
total = 0.0
for c in camion:
    total += c['cajones'] * c['precio']
print(total)

#recaudación venta
def precioVenta(nombreFruta):
    keys = precios_venta.keys()
    for key in keys:
        if(key == nombreFruta):
            return precios_venta[key]

costo = 0
venta_consumidor = 0
for c in camion:
    precio_venta = precioVenta(c['nombre'])
    venta_consumidor += precio_venta * c['cajones']
    costo += c['precio'] * c['cajones']

print(f'El costo total fue {costo}, en venta al consumidor se recaudó {venta_consumidor} \n La ganancia es de {round(venta_consumidor - costo, 2)}')
