import Adafruit_BBIO.PWM as PWM
import time


R = 0.08 # Length of the Moment Arm, in m

##The Following Functions Provide Basic Control for the Motor System of FLAIRs
class Motor:
    # Use P8_13, P9_14, and P9_16 to send the PWM signals
    motor1 = "P8_13"
    motor2 = "P9_14"
    motor3 = "P9_42"

    # Please Change the following settings based on ESC setup. (For current version, 9 for stop, 12 for full forward throttle, 6 for full backward throttle)
    duty_stop = 9
    duty_full_forward = 10.5
    duty_full_backward = 7.5

    def _init_(self):
        #Initialize the PWM generators
        print ('Initialized')
        #(Motor, Duty Frequency, Polarity)
        #Check the ESC setup for frequency
        PWM.start(Motor.motor1,Motor.duty_stop,60)
        PWM.start(Motor.motor2,Motor.duty_stop,60)
        PWM.start(Motor.motor3,Motor.duty_stop,60)

    def shutdown(self):
        print ('System Shutdown')
        #Kill both motor and signals
        PWM.stop(Motor.motor1)
        PWM.stop(Motor.motor2)
        PWM.stop(Motor.motor3)
        PWM.cleanup()

    def stop(self):
        #Set all motors to neutral
        print ('Motor Stop')
        PWM.set_duty_cycle(Motor.motor1,Motor.duty_stop)
        PWM.set_duty_cycle(Motor.motor2,Motor.duty_stop)
        PWM.set_duty_cycle(Motor.motor3,Motor.duty_stop)


    # Following are the basic movement function that enables the robot to move forward,
    # right,left,back with respect to its robotic reference frame with a specified generated force.
    
    # Solely used for test purpose.

    def right(self):
        print ('go right')
        PWM.set_duty_cycle(Motor.motor1,8.4)
        PWM.set_duty_cycle(Motor.motor2,9.6)
        PWM.set_duty_cycle(Motor.motor3,9.8)

    def forward(self):
        print ('go forward')
        PWM.set_duty_cycle(Motor.motor1,9.7)
        PWM.set_duty_cycle(Motor.motor2,9.7)
        PWM.set_duty_cycle(Motor.motor3,0)

    def backward(self):
        print ('go backward')
        PWM.set_duty_cycle(Motor.motor1,8.3)
        PWM.set_duty_cycle(Motor.motor2,8.3)
        PWM.set_duty_cycle(Motor.motor3,0)

    def left(self):
        print ('go left')
        PWM.set_duty_cycle(Motor.motor1,9.6)
        PWM.set_duty_cycle(Motor.motor2,8.4)
        PWM.set_duty_cycle(Motor.motor3,8.2)

    def rotate_ccw(self):
        print ('rotate ccw')
        PWM.set_duty_cycle(Motor.motor1,9.7)
        PWM.set_duty_cycle(Motor.motor2,8.3)
        PWM.set_duty_cycle(Motor.motor3,9.7)

    def rotate_cw(self):
        print ('rotate cw')
        PWM.set_duty_cycle(Motor.motor1,8.3)
        PWM.set_duty_cycle(Motor.motor2,9.7)
        PWM.set_duty_cycle(Motor.motor3,8.3)

    def pwm_set(self,pwm1,pwm2,pwm3):
        print ('rotate cw')
        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)


##    
##   
flairs = Motor()
##
##
### The motor controller test
##key = '0'
##
##
#PWM.start("P8_13",9,60,0)
#PWM.start("P8_19",9,60,0)
#PWM.start("P9_42",9,60,0)
##
##
##while key!='q':
##    print('waiting for next instruction')
##    key = raw_input(">")
##    if key == 'w':
##        flairs.forward()
##        time.sleep(5)
##	print("sleep end")
##    elif key == 's':
##        flairs.backward()
##        time.sleep(5)
##	print("sleep end")
##    elif key == 'a':
##        flairs.left()
##        time.sleep(5)
##	print("sleep end")
##    elif key == 'd':
##        flairs.right()
##        time.sleep(5)
##	print("sleep end")
##    elif key == 'j':
##        flairs.rotate_ccw()
##        time.sleep(5)
##	print("sleep end")
##    elif key == 'k':
##        flairs.rotate_cw()
##        time.sleep(5)
##	print("sleep end")
##    elif key == 'p':
##        flairs.stop()
##    elif key == 'o':
##        flairs.shutdown()
##
##
##PWM.cleanup()
##
##        
