frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

# 1. Armá una lista con los nombres de frutas
listaFrutas = frutas.split(',')
print(listaFrutas)

# 2. Extraé elementos
print(listaFrutas[0])
print(listaFrutas[1])
print(listaFrutas[-2])
print(listaFrutas[-1])

# 3. Reasigná un valor
listaFrutas[2] = 'Arandanos'
print(listaFrutas)

# 4. Slices
print(listaFrutas[0:3])
print(listaFrutas[-2:])

# 5. Agregar elemento a lista vacía
compra = []
compra.append('Pera')
print(compra)

# 6. Agrega 'Mango' al final de la lista
listaFrutas.append('Mango')
print(listaFrutas)

# 7. Agrega 'Lima' como segundo elemento
listaFrutas.insert(1, 'Lima')
print(listaFrutas)

# 8. Elimina 'Mandarina'
listaFrutas.remove('Mandarina')
print(listaFrutas)

# 9. Determinar la posición de la primera aparición de 'Banana' en la lista
listaFrutas.index('Banana')

# 10. Contá la cantidad de apariciones de 'Banana' en la lista:
listaFrutas.count('Banana')

# 11. Ordená alfabeticamente
listaFrutas.sort()
print(listaFrutas)

# 11. Ordená alfabeticamente a la inversa
listaFrutas.sort(reverse=True)
print(listaFrutas)

# 12. Juntar en string
a = ','.join(listaFrutas)
b = ' '.join(listaFrutas)
print(a)
print(b)