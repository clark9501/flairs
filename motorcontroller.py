import Adafruit_BBIO.PWM as PWM


R = 8 # Length of the Moment Arm

##The Following Functions Provide Basic Control for the Motor System of FLAIRs
class Motor:
    # Use P8_13, P9_14, and P9_16 to send the PWM signals
    motor1 = "P8_13"
    motor2 = "P9_14"
    motor3 = "P9_16"

    # Please Change the following settings based on ESC setup.
    duty_stop = 9
    duty_full_forward = 10.5
    duty_full_backward = 7.5

    def _init_(self):
        #Initialize the PWM generators
        print 'Initialized'
        #(Motor, Duty Frequency, Polarity)
        #Check the ESC setup for frequency
        PWM.start(Motor.motor1,Motor.duty_stop,15)
        PWM.start(Motor.motor2,Motor.duty_stop,15)
        PWM.start(Motor.motor3,Motor.duty_stop,15)

    def shutdown(self):
        #Kill both motor and signals
        PWM.stop(Motor.motor1)
        PWM.stop(Motor.motor2)
        PWM.stop(Motor.motor3)
        PWM.cleanup()

    def stop(self)
        #Set all motors to neutral
        PWM.set_duty_cycle(Motor.motor1,Motor.duty_stop)
        PWM.set_duty_cycle(Motor.motor2,Motor.duty_stop)
        PWM.set_duty_cycle(Motor.motor3,Motor.duty_stop)


    # Following are the basic movement function that enables the robot to move forward,
    # right,left,back with respect to its robotic reference frame with a specified generated force.
    
    # Solely used for test purpose.

    def going_right()
        PWM.set_duty_cycle(Motor.motor1,8.4)
        PWM.set_duty_cycle(Motor.motor2,9.6)
        PWM.set_duty_cycle(Motor.motor3,9.8)

    def going_forward()
        PWM.set_duty_cycle(Motor.motor1,9.7)
        PWM.set_duty_cycle(Motor.motor2,9.7)
        PWM.set_duty_cycle(Motor.motor3,0)

    def going_backward()
        PWM.set_duty_cycle(Motor.motor1,8.3)
        PWM.set_duty_cycle(Motor.motor2,8.3)
        PWM.set_duty_cycle(Motor.motor3,0)

    def going_left()
        PWM.set_duty_cycle(Motor.motor1,9.6)
        PWM.set_duty_cycle(Motor.motor2,8.4)
        PWM.set_duty_cycle(Motor.motor3,8.2)

    def rotate_counterclockwise()
        PWM.set_duty_cycle(Motor.motor1,9.7)
        PWM.set_duty_cycle(Motor.motor2,8.3)
        PWM.set_duty_cycle(Motor.motor3,9.7)

    def rotate_clockwise()
        PWM.set_duty_cycle(Motor.motor1,8.3)
        PWM.set_duty_cycle(Motor.motor2,9.7)
        PWM.set_duty_cycle(Motor.motor3,8.3)


# The motor controller test
key = '0'
while key!='q':
    key = raw_input(">")
    if key == 'w':
        Motor.going_forward()
    elif key == 's':
        Motor.going_backward()
    elif key == 'a':
        Motor.going_left()
    elif key == 's':
        Motor.going_right()
    elif key == 'j':
        Motor.rotate_counterclockwise()
    elif key == 'k':
        Motor.rotate_clockwise()
    elif key == 'l':
        Motor.stop()
    elif key == 'o':
        Motor.shutdown()


PWM.cleanup()

        
