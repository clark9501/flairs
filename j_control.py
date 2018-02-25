import Adafruit_BBIO.PWM as PWM
import motorcontroller 
import math
import Frame_Mapping  


rot_coeff = 1 # Define the coefficient that scales the magnitude of the rotaitonal vector



# Function: The controller read the input from the joystick and poll the IMU.
# Then it decompose the force and generate corresponding PWM signal that would
# generate thrust/torque in the direction designated by user.

#Initialize the System

flairs = motorcontroller.Motor()


#   def read_joystick()
#   poll the control signal input, return a translational direction in terms of angle alpha and
#   and magnitude m, as well as a rotational vector indicator rot.

#   def read_IMU()
#   poll the reading of the IMU, return a vector [x,y,beta] describing the coordinate of the robot
#   and the direction it is facing.



# The force mapping function takes a force value and returns the corresponding PWM output.
# Further test is needed to improve this function

def force_mapping(force):
    if force > 2 and force<10:
        PWM = 9.25+(force-10)/1.6
    elif force < -2 and force > -10:
        PWM = 8.75 - (force+10)/1.6
    else:
        PWM = 9

    return PWM
        


key = 1

#   Target Angle in robot frame

while key != 0:  # this is based on the controller options we have 

    alpha,m,rot,key = read_joystick()
    x,y,beta = read_IMU()

    gamma = alpha - beta

    fx = cos(gamma)*m
    fy = sin(gamma)*m
    tau = rot_coeff*rot

    decomp = force_decomp(fx,fy,tau,gamma)
    
    f1 = decomp[1][1]
    f2 = decomp[1][2]
    f3 = decomp[1][3]

    PWM1 = force_mapping(f1)
    PWM2 = force_mapping(f2)
    PWM3 = force_mapping(f3)

    flairs.pwm_set(PWM1,PWM2,PWM3)

    
    
PWM.cleanup()
    






