import numpy as np 

#array de dimension 0
a=np.array(42)
print(a)


#array de una dimension
b =np.array([1,2,3,4,5])
print(b)

#array de 2 dimensiones 
c =np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(c)

#array de 3 dimensiones
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(d)

#verificar dimension del array
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#**********************Indices de los arreglos*******************#

print(b[0]) #imprimiendo valor 0 del arreglo b
print(b[0]+b[1]) #suma de dos de sus componentes 

print(c[0,0]) #imprimendo valor 00 del arreglo de dos dimensiones
print(c[1,3]) 

print(d[1,1,0]) #imprimendo numeros del arreglo de 3 dimensiones 
print(d[1,0,0])

#********************Arrays Slicing*****************************#

print(b[:3]) #imprime los valores de 0 a 3 del arreglo de una dimension

arr = np.array([1, 2, 3, 4, 5, 6, 7]) #Step de un arreglo imprime 2 y 4 
print(arr[1:5:2])


print(c[1, 1:4]) #Slicing en el array de 2 dimensiones 
print(c[0:2, 1:4])

#****************** Tipos de datos en arrgelos ******************#

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S') #Se crean arreglos con un tipo de datos especificos 
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1]) #Convertir un arreglo en un tipo de dato

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)


#****************** Copy VS View ###################*

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() #copia el arrgelo
arr[0] = 42  #Sobreescribe el dato en la posicion 0

print(arr) #imprime arreglo modificado 
print(x) #imprime arreglo

arr = np.array([1, 2, 3, 4, 5])
x = arr.view() #imprime el arrego modificado
x[0] = 31  #modifica el arreglo

print(arr)
print(x)


#************* Array Shape ******************#

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


#*************** Array Reshape **************#

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  #Arreglo de 1D a una de 2D
newarr = arr.reshape(4, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #Arreglo de 1D a 3D
newarr = arr.reshape(2, 3, 2)
print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8]) #Arreglo de 1D a 3D de 2x2
newarr = arr.reshape(2, 2, -1)
print(newarr)

#*************** Iteracion de un array *******************#

arr = np.array([1, 2, 3])

for x in arr:
  print(x)


#************************** Array Join ****************************#

arr1 = np.array([1, 2, 3])              #Uniendo dos arreglos de 1D
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([1, 2, 3])              #Uniendo dos arreglos de 1D en dos filas con vstack
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

#*********************** Array split ***************************#

arr = np.array([1, 2, 3, 4, 5, 6]) #divide el array en 3 partes 
newarr = np.array_split(arr, 3)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6]) #divide array en 4 partes 
newarr = np.array_split(arr, 4)
print(newarr)

#****************** Array search ****************************#

arr = np.array([1, 2, 3, 4, 5, 4, 4])  #busqueda de valores en los arreglos
x = np.where(arr == 4) #retorno del indice donde se ubican los valores que coincidan
print(x)


#********************** Array sort **************************#

arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) #con sort ponemos en orden el arreglo


arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]]) #Ordenando arreglo 2D
print(np.sort(arr))

#********************** Array filter ************************#

arr = np.array([41, 42, 43, 44]) #Se define un arrglo
x = [True, False, True, False]  #Se define un arreglo con valores booleanos 
newarr = arr[x] #Filtra los dato que coinciden con los valores True
print(newarr)

#ejemplo de filtrado para valores superiores a 42
arr=np.array([41, 42, 43, 44, 45, 46])

filter_arr=[]

for element in arr:
  if element>42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr=arr[filter_arr]
print(filter_arr)
print(newarr)
