from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

"""
while True:
    buzzer.beep()
"""

#https://projects.raspberrypi.org/en/projects/physical-computing/8