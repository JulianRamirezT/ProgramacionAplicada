import threading


def info():
    print(f'{threading.current_thread().name}{threading.get_native_id()}')

#creamos los hilos 
hilo1=threading.Thread(target=info)
hilo2=threading.Thread(target=info)
hilo3=threading.Thread(target=info)

#ejecutamos los hilos

hilo1.start()
hilo2.start()
hilo3.start()

#el codigo principal sigue ejecutando aunque los hilos no hayan terminado 
print(f'{threading.current_thread().name}{threading.get_native_id()}')

def ejecutar():
    print(f'{threading.current_thread().name} te saluda')
#Creamos un temporizador 
temp=threading.Timer(5,function=ejecutar)
temp.start() #el hilo empezará cuando pasen 5 segundos
print(f'{threading.current_thread().name} te saluda') # se ejecuta inmediatamente y el programa solo termina una vez el temporizador haya acabado
