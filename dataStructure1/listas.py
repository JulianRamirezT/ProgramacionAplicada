##############LISTAS#################

my_lista=['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(my_lista)
print(type(my_lista))
print(my_lista[2])

print("my_lista size: ",len(my_lista))
print(my_lista[0:2])
print(my_lista[:2])

my_lista.append('Blanco')
print(my_lista)

my_lista.insert(3,'Negro')
print(my_lista)

my_lista.extend(['Marron','Gris'])
print(my_lista)

print(my_lista.index('Azul'))

my_lista.remove('Marron')
print(my_lista)

my_lista.insert(8,'Marron')
print(my_lista)

print(my_lista.pop())
size=len(my_lista)
print("size = ", size)

my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_listaSort=my_lista.sort()
print(my_listaSort)

my_NumList=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Ordenign my_NumList")
my_NumList.sort()
print(my_NumList)

my_NumList.sort(reverse = True)
print("De mayor a menor: ",my_NumList)

