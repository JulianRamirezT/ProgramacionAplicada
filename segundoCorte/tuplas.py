#########TUPLAS############
##### No se pueden modificar despues de creadas #########


my_lista=['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']


print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")

my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ",my_tupla)

print(my_tupla[0])
print(my_tupla[2])

#Evaluar si un elemento está dentro de la tupla con VorF

print('Rojo'in my_tupla)
print(my_tupla.count('Rojo'))

#Empaquetado de una tupla 

my_tupla= 'Gaspar', 5, 8, 1999
print(my_tupla)


#Desempaquetado de tupla, se guardan en orden de la variables 

nombre, dia , mes , año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, "- Día: ", dia, "- Mes: ", mes, "- Año: ", año)


#convertir una tupla en una lista

my_lista2=list(my_tupla)
print(my_lista2)