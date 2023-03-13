# Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
# Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso

palabras = ['banana', 'manzana', 'mandarina']

def geringoso(palabras):
    d = {}
    for palabra in palabras:
        palabra = palabra.lower()
        palabra_nueva = ''

        for letra in palabra:
            palabra_nueva += letra
            if letra in "aeiouáéíóú":
                palabra_nueva += 'p' + letra
        d[palabra] = palabra_nueva
    return d

d = geringoso(palabras)
print(d)

