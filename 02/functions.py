# Probá una función simple:
def saludar(nombre):
    'Saluda a alguien' # Si la primera instrucción de una función es una cadena, sirve como documentación de la función
    print('Hola', nombre)
saludar('Selena')
help(saludar)

# Preguntar edad
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

for nombre in ['Taylor', 'Selena', 'Meredith']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida')