from mpu6050 import mpu6050
import time



sensor = mpu6050(0x68)

def pos_int(data_in,delta_t,posin):
#       print(data_in['x'])
        acx=Kalman(0.1,0.001,0.001,0.0000001,data_in['x'])
        acy=Kalman(0.1,0.001,0.001,0.0000001,data_in['y'])
        acz=Kalman(0.1,0.001,0.001,0.0000001,data_in['z'])


        posx = posin['x']
        velocityx = acx*delta_t
        newposx = posx + velocityx #(0.5*acx)*delta_t**2
        posx = newposx

        posy = posin['y']
        velocityy = acy*delta_t
        newposy = posy + velocityy #(0.5*acy)*delta_t**2
        posy = newposy

        posz = posin['z']
        velocityz = acz*delta_t
        newposz = posz + velocityz #(0.5*acz)*delta_t**2
        posz = newposz


        return {'x':posx,'y':posy,'z':posz}



def Kalman(q,r,p,int_val,measurement):
        _q=q
        _r=r
        _p=p
        _x=int_val
        _p = _p + _q
        _k = _p / (_p +_r)
        _x = _x + _k * (measurement - _x)
        _p = (1.0 - _k) * _p
        return _x

acc_data = sensor.get_accel_data()
delta_t=0.02
posin0 = {'x':0, 'y':0, 'z':0}
posout = pos_int(acc_data,delta_t,posin0)

while True:
        gyro_data = sensor.get_gyro_data()
        posout = pos_int(gyro_data,delta_t,posout)
        time.sleep(delta_t)
        print(posout)

