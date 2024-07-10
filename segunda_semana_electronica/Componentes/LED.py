#LIBRERIAS
import RPi.GPIO as pin #Librería electrónica.
import time #Librería para controlar el tiempo. Ej: time.sleep(2)

#CONSTANTES
LED = 7 #Pin GPIO donde tengas conectado el LED.

#CONFIGURACION INICIAL DE RASPBERRY
pin.setmode(pin.BOARD)
pin.setwarnings(False) #Quita unas alertas.

#CONFIGURACION DE LOS PINES
pin.setup(LED, pin.OUT) #Pin LED como salida (OUT).

#PROGRAMA PRINCIPAL
pin.output(LED, True) #ENCENDER LED.
time.sleep(2) #ESPERA 2 SEGUNDOS.
pin.output(LED, False) #APAGAR LED.