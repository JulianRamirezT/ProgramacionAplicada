#sincronizacion 
import threading
from time import sleep
import random

def ejecutar():
    print(f'comienza {threading.current_thread().name}')
    sleep(random.random()) #esperamos un tiempor aleatorio entre 0 y 1
    print(f'Termina {threading.current_thread().name}')

#creamos los hilos 

hilo1 = threading.Thread(target=ejecutar, name='Hilo 1')
hilo2 = threading.Thread(target=ejecutar, name='Hilo 2')

#ejecutamos los hilos 

hilo1.start()
hilo2.start()

#esperamos a que terminen los hilos

hilo1.join()
hilo2.join()

print('El hilo principal si espera por el resto de los hilos')
