# Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra.
# Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'.
# Por ejemplo 'todos somos programadores' pasaría a ser 'todes somes programadores'.

frase = 'todos somos programadores'
palabras = frase.split()
lista_palabras = []
for palabra in palabras:
    if len(palabra)>=2:
        if palabra[-2] == 'o':
            nueva_palabra = palabra[:-2] + 'e' + palabra[-1]
        elif palabra[-1]=='o':
            nueva_palabra = palabra[:-1]+'e'
        else:
            nueva_palabra=palabra
    else:
        nueva_palabra=palabra
    lista_palabras.append(nueva_palabra)
frase_inclusive = ' '.join(lista_palabras)
print(frase_inclusive)

# con funciones
def palabraInclusivo(palabra):
    if len(palabra)>=2:
        if palabra[-2] == 'o':
            return palabra[:-2] + 'e' + palabra[-1]
        elif palabra[-1]=='o':
            return palabra[:-1]+'e'
        else:
            return palabra
    else:
        return palabra

frase = 'Todos somos habilidosos en algo'
palabras = frase.split()
lista_palabras = []

for palabra in palabras:
    palabra = palabraInclusivo(palabra)
    lista_palabras.append(palabra)
frase_inclusive = ' '.join(lista_palabras)
print(frase_inclusive)
