from numpy import random
import numpy as np

x=random.randint(100) #genera un numero entero aleatorio entre 0 y 100
print(x)

x=random.rand() #genera numero tipo float entre 0 y 1
print(x)

x=random.randint(100,size=(5))#genera un arrgelo de 1D de 5 elementos entre 0 y 100
print(x)

#************** Data distribution *******************#

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) #Genera un arreglo de 1D de numeros aleatorios entre 0 y 100
# el primer arreglo indica los numeros que se desean obtener, el p dicta la probabilidad de obtenerlos 
print(x)


x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x) #hace lo mismo pero con un arreglo de 2D

#*************** Random permutation ***************#

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)#devuelve el msimo arreglo modificado
print(arr)   

arr = np.array([1, 2, 3, 4, 5])#devuelve un arreglo reorganizado sin afectar el original 
print(random.permutation(arr))

#*************** Normal distribution ****************************#

x = random.normal(size=(2, 3)) #Genera una distribucion noral de 2x3
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3)) #genera una distribucion normal de tamaño 2x3 con media 1 y desviacion de 2
print(x)

#se genera la grafica de la distribucion normal aleatoria 
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)
plt.show()

#****************** Binomial distribution ***********************#
#n:numero de intentos P:probabilidad del evento size:tamaño del arreglo
x = random.binomial(n=10, p=0.5, size=10)
print(x)

#Se grafica una distribucion binomial 
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()

#***************** Poisson distribution **************************#
#lam: tasa o numero de ocurrencias 
x = random.poisson(lam=2, size=10)
print(x)

sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

#******************** uniform distribution ***************************#
#a:limite inferior b:limite superior. Por default 0 y 1 respectivamente

x=random.uniform(size=(2,3))
print(x)

#grafica de la distribucion uniforme 

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()


#********************* logistic distribution *************************#
#loc: pico predeterminado en 0, scale: desviacion estandar = 1 predeterminado

x=random.logistic(loc=1,scale=2,size=(2,3))
print(x)

#grafica de distribucion logica 

sns.distplot(random.logistic(size=1000), hist=False)
plt.show()


#********************** Multinomial distribution ************************#

#n:numero de resultados posibles, pvals: numero de probabilidades

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

#****************** Exponential distribution *****************************#

#scale:la inversa de la tasa

x=random.exponential(scale=2,size=(2,3))
print(x)

#grafica
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()

#**************** Chi square distribution ******************************#

#df:grado de libertad

x=random.chisquare(df=2,size=(2,3))
print(x)

sns.distplot(random.chisquare(df=2,size=1000),hist=False)
plt.show()

#*************** Rayleigh distribution ****************************#

#scale:desviacion estandar

x=random.rayleigh(scale=2,size=(2,3))
print(x)

#grafica 

sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()


#**************** Pareto distribution ***********************#
#a:parametro de forma 

x=random.pareto(a=2,size=(2,3))
print(x)

#Grafica

sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()


#******************* Zipf distribution **************#
#a:parametro de distribucion 

x=random.zipf(a=2,size=(2,3))
print(x)

#Grafica 

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()
