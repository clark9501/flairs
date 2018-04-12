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
    duty_stop = 11
    duty_full_forward = 10.5
    duty_full_backward = 7.5

    def _init_(self):
        #Initialize the PWM generators
        #print ('Initialized')
        #(Motor, Duty Frequency, Polarity)
        #Check the ESC setup for frequency
        PWM.start(Motor.motor1,Motor.duty_stop,60)
        PWM.start(Motor.motor2,Motor.duty_stop,60)
        PWM.start(Motor.motor3,Motor.duty_stop,60)

    def shutdown(self):
        #print ('System Shutdown')
        #Kill both motor and signals
        PWM.stop(Motor.motor1)
        PWM.stop(Motor.motor2)
        PWM.stop(Motor.motor3)
        PWM.cleanup()

    def stop(self):
        #Set all motors to neutral
        #print ('Motor Stop')
        PWM.set_duty_cycle(Motor.motor1,Motor.duty_stop)
        PWM.set_duty_cycle(Motor.motor2,Motor.duty_stop)
        PWM.set_duty_cycle(Motor.motor3,Motor.duty_stop)


    # Following are the basic movement function that enables the robot to move forward,
    # right,left,back with respect to its robotic reference frame with a specified generated force.
    
    # Solely used for test purpose.

    def right(self,pwm1,pwm2,pwm3):
        #print ('go right')
	if pwm1 >= 9.8:
		pwm1 = pwm1-0.1
	if pwm2 <= 12.2:
		pwm2 = pwm2+0.1
	if pwm3 <= 12.4:
		pwm3 = pwm3+0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def forward(self,pwm1,pwm2):
        #print ('go forward')
	#if pwm1 <= 11.2:
	#	pwm1 = pwm1+0.1
	#if pwm2 <= 12.5:
	#	pwm2 = pwm2+0.073
        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,11)

    def backward(self,pwm1,pwm2):
        #print ('go backward')
	if pwm1 >= 9.5:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.6:
		pwm2 = pwm2-0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,11)

    def left(self,pwm1,pwm2,pwm3):
        #print ('go left')
	if pwm1 <= 12.2:
		pwm1 = pwm1+0.1
	if pwm2 >= 9.8:
		pwm2 = pwm2-0.1
	if pwm3 >= 9.6:
		pwm3 = pwm3-0.1
        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def rotate_ccw(self,pwm1,pwm2,pwm3):
        #print ('rotate ccw')
	if pwm1 <= 12.2:
		pwm1 = pwm1+0.1
	if pwm2 >= 9.8:
		pwm2 = pwm2-0.1
	if pwm3 <= 12.2:
		pwm3 = pwm3+0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def rotate_cw(self,pwm1,pwm2,pwm3):
        #print ('rotate cw')
	if pwm1 >= 9.8:
		pwm1 = pwm1-0.1
	if pwm2 <= 12.2:
		pwm2 = pwm2+0.1
	if pwm3 >= 9.8:
		pwm3 = pwm3-0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def diag1(self,pwm1,pwm2,pwm3):
        #print ('go right')
	if pwm1 <= 12.1:
		pwm1 = pwm1+0.1
	if pwm2 <= 12.4:
		pwm2 = pwm2+0.1
	if pwm3 <= 12.3:
		pwm3 = pwm3+0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def diag2(self,pwm1,pwm2,pwm3):
        #print ('go right')
	if pwm1 <= 12.4:
		pwm1 = pwm1+0.1
	if pwm2 <= 12.2:
		pwm2 = pwm2+0.1
	if pwm3 >= 9.7:
		pwm3 = pwm3-0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def diag3(self,pwm1,pwm2,pwm3):
        #print ('go right')
	if pwm1 >= 9.9:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.6:
		pwm2 = pwm2-0.1
	if pwm3 >= 9.7:
		pwm3 = pwm3-0.1

        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def diag4(self,pwm1,pwm2,pwm3):
        #print ('go right')
	if pwm1 >= 9.6:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.9:
		pwm2 = pwm2-0.1
	if pwm3 <= 12.3:
		pwm3 = pwm3+0.1
        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)

    def motor1_test(self):
        PWM.set_duty_cycle("P8_13",12)
    def motor2_test(self):
        PWM.set_duty_cycle("P9_14",12)
    def motor3_test(self):
        PWM.set_duty_cycle("P9_42",12)
    def pwm_Set(self,pwm1,pwm2,pwm3):
        #print ('rotate cw')
        PWM.set_duty_cycle(Motor.motor1,pwm1)
        PWM.set_duty_cycle(Motor.motor2,pwm2)
        PWM.set_duty_cycle(Motor.motor3,pwm3)


##    
##   
#flairs = Motor()
##
##
### The motor controller test
##key = '0'
##
##
#PWM.start(motor1,9,60,0)
#PWM.start(motor2,9,60,0)
#PWM.start(motor3,9,60,0)
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
