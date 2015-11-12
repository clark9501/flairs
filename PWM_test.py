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
PWM.start("P8_13",9,60,0)
PWM.start("P9_14",9,60,0)
PWM.start("P9_42",9,60,0)
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
	flairs.forward()
    elif c == ord('a'):
	flairs.left()
    elif c == ord('d'):
	flairs.right()
    elif c == ord('s'):
	flairs.backward()
    elif c == ord('q'):
	flairs.rotate_ccw()
    elif c == ord('e'):
	flairs.rotate_cw()
    elif c == ord('g'):
 	flairs.stop()
    time.sleep(0.01)
#wrapper(main)

PWM.cleanup()
stdscr.nodelay(False)
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
print('all done')

