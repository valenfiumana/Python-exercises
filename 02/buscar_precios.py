# Buscar precio frutas

# version 1
def buscar_precio(fruta):
    with open('precios.csv', 'rt') as f:
        frutas = []
        for line in f:
            row = line.split(',')
            frutas.append(row[0]) # agrego nombre fruta a array
            if (row[0] == fruta):
                costo = float(row[1])
                print(f'El precio de un cajon de {fruta} es: {costo}')
        if fruta not in frutas: # si no está en el array con todas las frutas
            print('La fruta no esta en la lista')

buscar_precio('Frambuesa')
buscar_precio('Kale')


# version 2: con diccionario
import csv
def buscar_precio2(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        d = {}
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if len(row) == 2:
                d[row[0]] = float(row[1])
        return d

d = buscar_precio2('precios.csv')
print(d)

# version 3: con csv y verbose --> verbose es un parámetro opcional, un Boolean que dice si se imprime o no algo en pantalla
import csv
def buscar_precio3(fruta, verbose=True):
    precio = None
    with open('precios.csv', 'rt', encoding='utf-8') as archivo:
        archivo_csv = csv.reader(archivo)
        for linea in archivo_csv:
            if linea:  # si no esta vacia
                if linea[0] == fruta:
                    precio = float(linea[1])
                    break #Si encuentra fruta deja de recorrer lista
    if verbose: #Si no aclaro por consola que no quiero imprimir
        if precio != None:
            print(f'El precio de un cajon de {fruta} es ${precio}')
        else:
            print(f'{fruta} no figura en en listado de frutas')

buscar_precio3('Frambuesa')
buscar_precio3('Kale')
buscar_precio3('Frambuesa', False)

# version 4: con while
import csv
def buscar_precio4(fruta, verbose=True):
    precio = None
    with open('precios.csv', 'rt', encoding='utf-8') as archivo:
        archivo_csv = csv.reader(archivo)
        linea = next(archivo_csv)
        fruta_encontrada = False
        seguir = True # flag
        while seguir:
            if linea:
                if linea[0] == fruta:
                    precio = float(linea[1])
                    seguir=False
                    fruta_encontrada=True
            try:
                linea=next(archivo_csv)
            except StopIteration:
                seguir = False
    if verbose:
        if fruta_encontrada:
            print(f'El precio de un cajon de {fruta} es ${precio}')
        else:
            print(f'{fruta} no figura en en listado de frutas')

buscar_precio4('Naranja')
buscar_precio4('Kale')

