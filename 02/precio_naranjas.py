# Escribí un código que abra el archivo ../Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.
with open('precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        if(row[0] == 'Naranja'):
            costo = float(row[1])
            print(f'El precio de la naranja es: {costo}')