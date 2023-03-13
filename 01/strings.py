frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

frutas = frutas + ',Pera'
print(frutas)

print('Naranja' in frutas)
print('nana' in frutas)
print('Lima' in frutas)

string = 'Cocoon'
o = 0
for c in string:
    if(c=='o'):
        o+=1
print(f'Hay {o} letras O en "{string}"')


#version 1
cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
    capadepenapa += c
    if c == 'a' or c =='e' or c =='i' or c =='e'or c =='o' or c =='u':
        capadepenapa +='p' + c
print(capadepenapa)

#version 2
palabra = input('Ingrese una palabra: ')
palabra = palabra.lower()
palabra_nueva = ''

for letra in palabra:
    palabra_nueva += letra
    if letra in "aeiouáéíóú":
        palabra_nueva += 'p' + letra
print(palabra_nueva)