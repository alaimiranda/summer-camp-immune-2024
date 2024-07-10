from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4)
while True:
    print(ultrasonic.distance)

"""
while True:
    ultrasonic.wait_for_in_range()
    print("In range")
    ultrasonic.wait_for_out_of_range()
    print("Out of range")

ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)

def hello():
    print("Hello")

ultrasonic.when_in_range = hello

def bye():
    print("Bye")

ultrasonic.when_out_of_range = bye

ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=2)
ultrasonic.max_distance = 2

#https://projects.raspberrypi.org/en/projects/physical-computing/12
"""