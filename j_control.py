import Adafruit_BBIO.PWM as PWM
import motorcontroller 
import math
import Frame_Mapping
import gyro

from mpu6050 import mpu6050
import time
PWM.cleanup()


#Sensor position
sensor = mpu6050(0x68)



rot_coeff = 1 # Define the coefficient that scales the magnitude of the rotaitonal vector



# Function: The controller read the input from the joystick and poll the IMU.
# Then it decompose the force and generate corresponding PWM signal that would
# generate thrust/torque in the direction designated by user.

#Initialize the System

flairs = motorcontroller.Motor()


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
    if force > 0.5 and force<10:
        PWM = 9.25+(force)/5
    elif force < -0.5 and force > -10:
        PWM = 8.75 + (force)/5
    else:
        PWM = 9

    return PWM
        


key = 1

#   Target Angle in robot frame

##calibration loop for velocity test:
delta_t=0.025
acc_data = sensor.get_accel_data()
gyro_data = sensor.get_gyro_data()
posin0 = {'x':0,'y':0,'z':0}
pos_data = {}
pos_data['x'] = 100*acc_data['x']
pos_data['y'] = 100*acc_data['y']
pos_data['z'] = gyro_data['z']
posout = gyro.pos_int(pos_data,delta_t,posin0)
#time.sleep(1)
tstart = time.time()
#PWM.stop("P8_13")
#PWM.stop("P8_19")
#PWM.stop("P9_42")

        
#PWM.start("P8_13",9,60,0)
#PWM.start("P8_19",9,60,0)
#PWM.start("P9_42",9,60,0)

while key < 100:  # this is based on the controller options we have    
    t1 = time.time()
    key = key + 0.025
    print("Rotation:" + str(round(posout['z'],5)))
    gyro_data = sensor.get_gyro_data()
    acc_data = sensor.get_accel_data()
    pos_data['x'] = 100*acc_data['x']
    pos_data['y'] = 100*acc_data['y']
    pos_data['z'] = gyro_data['z']
    #time.sleep(delta_t)
    t2 = time.time()
    posout = gyro.pos_int(pos_data,(t2-t1),posout)
    #posout['x'] = posout['x']# - calxfin
    #posout['y'] = posout['y']# - calyfin
    #avxv.append(posout['x'])
    #avyv.append(posout['y'])
    #print(t2-t1)
    #print(posout)
    #alpha = 0
    #m = 1.5
    #rot = 0
    #beta = posout['z']*math.pi/180
    #beta = math.pi/2
    #alpha,m,rot = read_joystick()
 
    #gamma = alpha - beta

    #fx = math.cos(gamma)*m
    #fy = math.sin(gamma)*m
    #tau = rot_coeff*rot

    #decomp = Frame_Mapping.force_decomp(fx,fy,tau,gamma)
    #print(decomp)
    #f1 = decomp[0]
    #f2 = decomp[1]
    #f3 = decomp[2]

    #PWM1 = force_mapping(float(f1))
    #PWM2 = force_mapping(float(f2))
    #PWM3 = force_mapping(float(f3))



    #flairs.pwm_set(PWM1,PWM2,PWM3)
    #print(PWM1,PWM2,PWM3)

tend = time.time()    
average_velocity = [sum(avxv)/len(avxv),sum(avyv)/len(avyv)]
print("X velocity:" + str(average_velocity[0]) + "  Y velocity:" + str(average_velocity[1]))
print("time elapsed:" + str(tend-tstart))
PWM.stop("P8_13")
PWM.stop("P8_19")
PWM.stop("P9_42")
PWM.cleanup()






