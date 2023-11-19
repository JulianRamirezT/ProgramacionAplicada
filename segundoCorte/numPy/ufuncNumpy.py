#************* crear funciones con numpy *************#
import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add)) # chekear si es una ufunc

#ejemplo 

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

#************ Simple arithmetic **************#

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2) #adicion
print(newarr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2) # resta
print(newarr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)#multiplicacion
print(newarr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2) #division
print(newarr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)#potenciacion
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)#remainder
print(newarr)


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)#modulo
print(newarr)

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)#valor absoluto 
print(newarr)

#************** rounding decimals ****************#

arr = np.trunc([-3.1666, 3.6667])
print(arr) #aproxima a -3 y a 3


arr = np.fix([-3.1666, 3.6667])
print(arr) #aproxima a -3 y a 3


arr = np.around(3.1666, 2)
print(arr) #redondea el número usando 2 cifras decimales 

#*************** Logs *****************#

arr = np.arange(1, 10)
print(np.log2(arr)) # logaritmo en base 2

arr = np.arange(1, 10)
print(np.log10(arr)) #logaritmo en base 10


arr = np.arange(1, 10)
print(np.log(arr))# natural log 


#*****************  summations ***************#

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr) #acumuladora
print(newarr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1) #suma
print(newarr)

#****************products ******************#

arr1= np.array([1, 2, 3, 4])
x = np.prod(arr) #1*2*3*4
print(x)

arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2]) #producto entre dos arreglos 
print(x)


#**************** differences *****************#

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr) # al número que sigue le resta el anterior 
print(newarr)

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)

#***************** finding lcm *******************#

num1 = 4
num2 = 6

x = np.lcm(num1, num2)#busca el mínimo común múltiplo 
print(x)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr) #mcm en un arreglo
print(x)


#*************** finding gcd *****************#


num1 = 6
num2 = 9
x = np.gcd(num1, num2) # busca el máximo común divisor 

print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr) #busca máximo común divisor en un arreglo 

print(x)


#****************** trigonometrics functions ***************#

x = np.sin(np.pi/2) #funcion seno de pi/2
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr) # función seno de los valores de un arreglo 
print(x)

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr) #convirtiendo de grados a radianes 
print(x)

x = np.arcsin(1.0) #buscando grado con la función inversa del seno
print(x)

base = 3
perp = 4
x = np.hypot(base, perp) #halla la hipotenusa según teorema de Pitágoras 
print(x)


#******************* hyperbolic functions *****************#

x = np.sinh(np.pi/2) # seno hiperbólico de pi/2 
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)# coseno hiperbólico de ángulos en un areeglo
print(x)

#****************** set operations ******************#

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr) # imprime valores únicos sin repetir 
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2) # une los elementos de ambos arreglos 
print(newarr)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)#busca intersección de los dos arreglos
print(newarr)



