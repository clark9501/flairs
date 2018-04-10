import time
import Adafruit_BBIO.PWM as PWM
myPWM1="P8_13"
myPWM2="P9_14"
myPWM3="P9_42"

PWM.start(myPWM1, 10, 60)
PWM.start(myPWM2, 10, 60)
PWM.start(myPWM3, 10, 60)
DC=10;
start = 10
DC=input("What Duty Cycle Would You Like (0-100)? ")

while DC <15.1 and start==10:
    DC=input("What Duty Cycle Would You Like (0-100)? ")
    
    print(str(DC))
    PWM.set_duty_cycle(myPWM1, DC)
    PWM.set_duty_cycle(myPWM2, DC)
    PWM.set_duty_cycle(myPWM3, DC)
    #time.sleep(1)
    #DC=DC+0.1

PWM.stop(myPWM1)
PWM.stop(myPWM2)
PWM.stop(myPWM3)
PWM.cleanup()
print('all done')
