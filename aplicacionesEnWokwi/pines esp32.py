from machine import Pin
from utime import sleep

led_rojo= Pin(5,Pin.OUT)
led_verde= Pin(23,Pin.OUT)
led_azul= Pin(22,Pin.OUT)
led_amarillo= Pin(21,Pin.OUT)
led_amarosc= Pin(19,Pin.OUT)
led_morado= Pin(4,Pin.OUT)
led_purpura= Pin(2,Pin.OUT)
led_azulcl= Pin(12,Pin.OUT)


while True:
  led_rojo.value(0)
  led_verde.value(0)
  led_azul.value(0)
  led_amarillo.value(0)
  led_amarosc.value(0)
  led_morado.value(0)
  led_purpura.value(0)
  led_azulcl.value(0)
  sleep(1)
  print("on")
  led_rojo.value(1)
  led_verde.value(1)
  led_azul.value(1)
  led_amarillo.value(1)
  led_amarosc.value(1)
  led_morado.value(1)
  led_purpura.value(1)
  led_azulcl.value(1)
  sleep(1)
  print("off")
