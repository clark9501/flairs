import Adafruit_BBIO.PWM as PWM
import motorcontroller 
import math
import Frame_Mapping
from Tkinter import Tk

import logging
import sys
import time

from Adafruit_BNO055 import BNO055
PWM.cleanup()


#New Sensor activation
bno = BNO055.BNO055(rst='P9_12')

# Enable verbose debug logging if -v is passed as a parameter.
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')




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

def addToClipBoard(text):
    command = 'echo' + text.strip() + '| clip'
    os.system(command)


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

delta_t=0.025


#PWM.stop("P8_13")
#PWM.stop("P8_19")
#PWM.stop("P9_42")

        
#PWM.start("P8_13",9,60,0)
#PWM.start("P8_19",9,60,0)
#PWM.start("P9_42",9,60,0)

##attempt at velocity:
#accel = 0
#while accel <3:
#    sys,gyro,accel,mag = bno.get_calibration_status()
#    print(accel)
vel = [0,0,0]
prevaccel = [0,0,0]
totv = []
tstart = time.time()
while time.time()-tstart<5:
    cal= bno.get_calibration_status()
    print(cal)
print("3")
time.sleep(.5)
print("2")
time.sleep(.5)
print("1")
time.sleep(.5)

prevt = time.time()
tstart = prevt
key = 0
while time.time()-tstart<10:  # this is based on the controller options we have    
    #heading, roll, pitch = bno.read_euler()
    #print("Rotation:" + str(heading))
    #time.sleep(.05)
    
    curraccel = bno.read_linear_acceleration()
    currt = time.time()
    for x in range(0,2):
#        if abs(curraccel[x]) > 0.03:
        vel[x] = round(vel[x]+((round(curraccel[x],2) + round(prevaccel[x],2))/2)*(currt - prevt)*100,1)
   # print(curraccel)
    prevaccel = curraccel

    totv.append(vel[0])
    key = key + 1
    #time.sleep(.1)
    prevt = currt
    
    #print(vel)
    #alpha = 0
    #m = 1.5
    #rot = 0
    #beta = heading*math.pi/180
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
print(time.time()-tstart)
print(totv)
avvel = sum(totv)/len(totv)
#root = Tk()
#root.withdraw()
#root.clipboard_clear()
#root.clipboard_append(str(totv))
#root.update()
#root.destroy()
print(avvel)

PWM.stop("P8_13")
PWM.stop("P8_19")
PWM.stop("P9_42")
PWM.cleanup()






