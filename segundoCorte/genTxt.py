#Escribir un archivo txt
f = open ('expTXT1.txt','w')
f.write('julian andres ramirez torres')
f.close()

#Leer un archivo txt

f = open ('expTXT1.txt','r')
mensaje = f.read()
print(mensaje)
f.close() 