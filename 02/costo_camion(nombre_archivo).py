
def costo_camion(nombre_archivo):
    costo = 0
    with open(nombre_archivo, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            cajones = int(row[1])
            precio = float(row[2].rstrip(row[2][-2]))
            costo += cajones * precio
    return costo

costo = costo_camion('camion.csv')
print('Costo total: ', costo)