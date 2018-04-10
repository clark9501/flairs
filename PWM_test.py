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
while c != ord('h'):
    c = stdscr.getch()
    if c == ord('w'):
	print('w')
	flairs.forward()
    elif c == ord('a'):
	print('a')
	flairs.left()
    elif c == ord('d'):
	print('d')
	flairs.right()
    elif c == ord('x'):
	print('x')
	flairs.backward()
    elif c == ord('q'):
	print('q')
	flairs.diag1()
    elif c == ord('e'):
	print('e')
	flairs.diag2()
    elif c == ord('z'):
	print('z')
 	flairs.diag3()
    elif c == ord('c'):
	print('c')
	flairs.diag4()
    elif c == ord('j'):
	print('j')
	flairs.rotate_ccw
    elif c == ord('k'):
	print('k')
	flairs.rotate_cw
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
    time.sleep(.033)
#wrapper(main)

PWM.cleanup()
stdscr.nodelay(False)
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
print('all done')

