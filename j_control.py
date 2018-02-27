import Adafruit_BBIO.PWM as PWM
import motorcontroller 
import math
import Frame_Mapping
#import gyro

from mpu6050 import mpu6050
import time


# Sensor position
#sensor = mpu6050(0x68)



rot_coeff = 1 # Define the coefficient that scales the magnitude of the rotaitonal vector



# Function: The controller read the input from the joystick and poll the IMU.
# Then it decompose the force and generate corresponding PWM signal that would
# generate thrust/torque in the direction designated by user.

#Initialize the System

# flairs = motorcontroller.Motor()


#   def read_joystick()
#   poll the control signal input, return a translational direction in terms of angle alpha and
#   and magnitude m, as well as a rotational vector indicator rot.

def read_joystick():
    alpha = 0
    m = 1.5
    rot = 0




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

#acc_data = sensor.get_accel_data()
#gyro_data = sensor.get_gyro_data()
#pos_data = {}
#pos_data['x'] = acc_data['x']
#pos_data['y'] = acc_data['y']
#pos_data['z'] = gyro_data['z']
#delta_t=0.02
#posin0 = {'x':0, 'y':0, 'z':0}
#posout = gyro.pos_int(pos_data,delta_t,posin0)
        



while key != 0:  # this is based on the controller options we have

    if key == 1000:
        key = 0
    
    key = key + 0.1

   # gyro_data = sensor.get_gyro_data()
    #acc_data = sensor.get_accel_data()
    #pos_data['x'] = acc_data['x']
    #pos_data['y'] = acc_data['y']
    #pos_data['z'] = gyro_data['z']
    #posout = gyro.pos_int(pos_data,delta_t,posout)
    #print(posout)
    alpha = 0
    m = 1.5
    rot = 0
    #beta = posout['z']*math.pi/180

    #alpha,m,rot = read_joystick()

    beta = math.pi/2	    
    gamma = alpha - beta

    fx = math.cos(gamma)*m
    fy = math.sin(gamma)*m
    tau = rot_coeff*rot

    decomp = Frame_Mapping.force_decomp(fx,fy,tau,gamma)
    print(decomp)
    f1 = decomp[0]
    f2 = decomp[1]
    f3 = decomp[2]

    PWM1 = force_mapping(f1)
    PWM2 = force_mapping(f2)
    PWM3 = force_mapping(f3)

    flairs.pwm_set(PWM1,PWM2,PWM3)
    print(PWM1,PWM2,PWM3)
    time.sleep(delta_t)

    
PWM.cleanup()
    






