import Adafruit_BBIO.PWM as PWM
import time
import curses
import motorcontroller
#from curses import wrapper

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(True)
curses.noecho()
PWM.cleanup()
PWM.start("P8_13",11,60,0)
PWM.start("P9_14",11,60,0)
PWM.start("P9_42",11,60,0)
tstart = time.time()

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
while c != ord('h'):
    c = stdscr.getch()
    if c == ord('w'):
	print('w')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.5:
		pwm1 = pwm1+0.20
	if pwm2 <= 11.5:
		pwm2 = pwm2+0.052
	elif pwm2 <= 12.2:
		pwm2 = pwm2+0.062
	pwm3 = 11
    elif c == ord('d'):
	print('d')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.5:
		pwm1 = pwm1+0.1
	if pwm2 >= 9.8:
		pwm2 = pwm2-0.062
	if pwm3 >= 9.6:
		pwm3 = pwm3-0.054
    elif c == ord('a'):
	print('a')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.65	:
		pwm1 = pwm1+0.25
	if pwm2 <= 11.8:
		pwm2 = pwm2+0.07
	if pwm3 <= 12.4:
		pwm3 = pwm3+0.47
    elif c == ord('x'):
	print('x')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.65:
		pwm1 = pwm1-0.155
	if pwm2 >= 10.3:
		pwm2 = pwm2-0.058
	elif pwm2 >= 9.75:
		pwm2 = pwm2-0.062
	pwm3 = 11
    elif c == ord('q'):
	print('q')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.4:
		pwm1 = pwm1+0.1
	if pwm2 <= 12.2:
		pwm2 = pwm2+0.062
	if pwm3 >= 9.7:
		pwm3 = pwm3-0.054
    elif c == ord('e'):
	print('e')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.5:
		pwm1 = pwm1+0.1
	if pwm2 <= 12.4:
		pwm2 = pwm2+0.062
	if pwm3 <= 12.3:
		pwm3 = pwm3+0.054
    elif c == ord('z'):
	print('z')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.9:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.6:
		pwm2 = pwm2-0.062
	if pwm3 >= 9.7:
		pwm3 = pwm3-0.054
    elif c == ord('c'):
	print('c')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.6:
		pwm1 = pwm1-0.1
	if pwm2 >= 9.9:
		pwm2 = pwm2-0.062
	if pwm3 <= 12.3:
		pwm3 = pwm3+0.054	
    elif c == ord('j'):
	print('j')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 <= 12.1:
		pwm1 = pwm1+0.1
	if pwm2 >= 10.1:
		pwm2 = pwm2-0.062
	if pwm3 <= 11.7:
		pwm3 = pwm3+0.054	
    elif c == ord('k'):
	print('k')
	flairs.pwm_Set(pwm1,pwm2,pwm3)
	if pwm1 >= 9.9:
		pwm1 = pwm1-0.1
	if pwm2 <= 11.9:
		pwm2 = pwm2+0.062
	if pwm3 >= 10.3:
		pwm3 = pwm3-0.064	
    elif c == ord('i'):
	print('i')
	flairs.motor1_test()
    elif c == ord('o'):
	print('o')
	flairs.motor2_test()
    elif c == ord('p'):
	print('p')
	flairs.motor3_test()
    else:
	print('no ip')
	flairs.stop()
	pwm1 = 11
	pwm2 = 11
	pwm3 = 11
    time.sleep(.033)
#wrapper(main)

PWM.cleanup()
stdscr.nodelay(False)
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
print('all done')

