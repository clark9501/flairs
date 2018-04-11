import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep

sensorPin = "P9_40"

while(1):
	Signal = ADC.read(sensorPin)
	voltage = 1.8 * signal
	distance = voltage/0.002441 # distance in cm in air
	distance /= 2.54 # distance in inches in air
	print "Distance: ",distance," in"
	sleep(0.1)
