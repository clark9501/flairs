import Adafruit_BBIO.PWM as PWM
import time
import curses
import motorcontroller
import sys
#from curses import wrapper
import Adafruit_BBIO.ADC as ADC
ADC.setup()
sensorPin="P9_40"
from Adafruit_BNO055 import BNO055
bno=BNO055.BNO055(rst="P9_12")
bus = 2
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.noecho()
PWM.cleanup()
PWM.start("P8_13",11,60,0)
PWM.start("P9_14",11,60,0)
PWM.start("P9_42",11,60,0)
tstart = time.time()
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055')

#def main(stdscr):
    # Clear screen
#    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
#    for i in range(0, 11):
#        v = i-10
#        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

#    stdscr.refresh()
#    stdscr.getkey()

flairs = motorcontroller.Motor()
stdscr.nodelay(True)
c = stdscr.getch()
debounce = True
pwm1 = 11
pwm2 = 11
pwm3 = 11
ocount=0
while c != ord('h'):
    c = stdscr.getch()
    if c == ord('x'):
#	print('w')
	stdscr.addstr(2,1,'Backward                          ')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.5:
		pwm1 = pwm1+0.20
	if pwm2 <= 11.5:
		pwm2 = pwm2+0.052
	elif pwm2 <= 12.2:
		pwm2 = pwm2+0.062
	pwm3 = 11
    elif c == ord('a'):
#	print('d')
	stdscr.addstr(2,1,'Left                         ')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.35:
		pwm1 = pwm1-0.23
	if pwm2 >= 10.2:
		pwm2 = pwm2-0.07
	if pwm3 >= 9.6:
		pwm3 = pwm3-0.42
    elif c == ord('d'):
#	print('a')
	stdscr.addstr(2,1,'Right                          ')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.65	:
		pwm1 = pwm1+0.25
	if pwm2 <= 11.8:
		pwm2 = pwm2+0.07
	if pwm3 <= 12.4:
		pwm3 = pwm3+0.47
    elif c == ord('w'):
#	print('x')
	stdscr.addstr(2,1,'Forward                     ')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.65:
		pwm1 = pwm1-0.155
	if pwm2 >= 10.3:
		pwm2 = pwm2-0.058
	elif pwm2 >= 9.75:
		pwm2 = pwm2-0.062
	pwm3 = 11
    elif c == ord('q'):
#	print('q')
	stdscr.addstr(2,1,'q')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.4:
		pwm1 = pwm1+0.1
	if pwm2 <= 12.2:
		pwm2 = pwm2+0.062
	if pwm3 >= 9.7:
		pwm3 = pwm3-0.054
    elif c == ord('e'):
#	print('e')
	stdscr.addstr(2,1,'e')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.5:
		pwm1 = pwm1+0.1
	if pwm2 <= 12.4:
		pwm2 = pwm2+0.062
	if pwm3 <= 12.3:
		pwm3 = pwm3+0.054
    elif c == ord('z'):
#	print('z')
	stdscr.addstr(2,1,'z')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.9:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.6:
		pwm2 = pwm2-0.062
	if pwm3 >= 9.7:
		pwm3 = pwm3-0.054
    elif c == ord('c'):
#	print('c')
	stdscr.addstr(2,1,'c')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.6:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.9:
		pwm2 = pwm2-0.062
	if pwm3 <= 12.3:
		pwm3 = pwm3+0.054	
    elif c == ord('j'):
#	print('j')
	stdscr.addstr(2,1,'Rotate Counter-Clockwise       ')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.1:
		pwm1 = pwm1+0.1
	if pwm2 >= 10.1:
		pwm2 = pwm2-0.062
	if pwm3 <= 11.7:
		pwm3 = pwm3+0.054	
    elif c == ord('k'):
#	print('k')
	stdscr.addstr(2,1,'Rotate Clockwise         ')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.9:
		pwm1 = pwm1-0.1
	if pwm2 <= 11.9:
		pwm2 = pwm2+0.062
	if pwm3 >= 10.3:
		pwm3 = pwm3-0.064	
    elif c == ord('i'):
#	print('i')
	stdscr.addstr(2,1,'Test Motor 1                   ')
	flairs.motor1_test()
    elif c == ord('o'):
#	print('o')
	stdscr.addstr(2,1,'Test Motor 2                    ')
	flairs.motor2_test()
    elif c == ord('p'):
#	print('p')
	stdscr.addstr(2,1,'Test Motor 3                        ')
	flairs.motor3_test()
    else:
#	print('no ip')
	stdscr.addstr(2,1,'no input                        ')
	flairs.stop()
	pwm1 = 11
	pwm2 = 11
	pwm3 = 11
    if ocount == 15:
        signal=ADC.read(sensorPin)
        voltage=1.8*signal
        distance=voltage*149.77+2.252
        stdscr.addstr(1,1,"Distance: " + str(distance) + " in")
	ocount=0
    if ocount == 66:
	heading,roll,pitch = bno.read_euler()
    	stdscr.addstr(3,1,'Heading: ' + str(heading) + 'deg     ')
	stdscr.addstr(4,1,'Roll: ' + str(roll) + 'deg     ')
	stdscr.addstr(5,1,'Pitch: ' + str(pitch) + 'deg      ')
    ocount=ocount+1
    stdscr.refresh()
    time.sleep(.033)
    
#wrapper(main)

PWM.cleanup()
stdscr.nodelay(False)
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
print('all done')

