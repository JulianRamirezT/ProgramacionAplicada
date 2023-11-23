import matplotlib

print(matplotlib.__version__) #en mi caso es version 3.8.1

#********************** pyplot ***************************#

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

#********************* Plotting **************************#

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

#********************** Markers ************************#
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')#Señala los puntos con circulos rellenos
plt.show()

plt.plot(ypoints, marker = '*')#Señala los puntos con asteriscos
plt.show()

#Hay una tabla con otros tipos de marcadores

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r') #Macrador con circulo rellenos con o y uniones punteadas con : y color rojo con r
plt.show()


ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r') #marcador circulo relleno, ms=tamaño=20 mfc relleno rojo
plt.show()


ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')#marcador circulo relleno, ms=tamaño=20,  mfc relleno rojo, mec borde rojo
plt.show()

#************************* Line ************************#

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted') #traza una linea punteada
plt.show()

plt.plot(ypoints, linestyle = 'dashed') #traza la linea con lineas
plt.show()

#************************ Labels ************************#

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

plt.title("Sports Watch Data") #titulo
plt.xlabel("Average Pulse") #Nombre de datos en x
plt.ylabel("Calorie Burnage") #Nombre de datos en y
plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125]) #valores en x
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330]) #valores en y
font1 = {'family':'serif','color':'blue','size':20} #fuente color y tamaño de letra en titulo
font2 = {'family':'serif','color':'darkred','size':15} #fuente color y tamaño de letra en x e y
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()

plt.title("Sports Watch Data", loc = 'left') #Posicionar titulo
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.show()

#**************************** Grid ********************************#

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid() #pone una cuadricula en las gráficas
plt.show()

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5) #pone color, formato interlineado y el amcho de linea
plt.show()

#************************* Subplot **************************#

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)  #Tendrá 2 filas, una columna y la imagen irá primero
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)  #Tendrá 2 filas, una columna y la imagen irá segunda
plt.plot(x,y)

plt.show()

#************************* Scatter ***********************#

#Se deben tener dos arreglos de mismos tamaño, y scatter relacionará punto por punto
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()

#Graficando dos imagenes en el mismo cuadro

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

#***************************** Bars ******************************#

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y) #Hace gráfico d barras
plt.show()


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y) #hace barras horizontales
plt.show()


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "#4CAF50") #cambio de color en hex, tambien puede escribirse
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width = 0.1) #Ajuste de tamaño de barras
plt.show()

#************************** Histograms ****************************#

x = np.random.normal(170, 10, 250)
plt.hist(x) #histograma de una distribucion normal random
plt.show() 

#************************** Pie charts ***************************#
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show() 

y = np.array([35, 25, 25, 15]) #define porcetajes
mylabels = ["Apples", "Bananas", "Cherries", "Dates"] #define sus etiquetas
plt.pie(y, labels = mylabels)
plt.show() 


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0] #para arrancar un pedazo del gráfico de ponqué
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend() #Genera leyendas, definiendo que colores corresponden a etiquetas
plt.show() 

