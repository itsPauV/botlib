#!/usr/bin/python3

from botlib import *
from readchar import readkey, key
from math import cos

bp = Motor._bp
power = 0
steer = 0

def stop():
    import time

    global bp
    global power

    print('stopping...')

    step_down = (t for t in (cos(i/100.) for i in range(1, 314, 15)) if 0 < t)
    for step in step_down:
        power *= step
        bp.set_motor_power(bp.PORT_B, power)
        time.sleep(0.2)

    power = 0
    bp.set_motor_power(bp.PORT_B, power)

def main():
    global bp
    global power
    global steer

    print('Up/Down: manage speed, Left/Right: manage direction, Space: stop, Backspace: exit')

    while True:
        inp = readkey()
        if inp == key.DOWN:
            power -= 10
            if power < -100:
                power = -100
        elif inp == key.UP:
            power += 10
            if 100 < power:
                power = 100
        elif inp == key.RIGHT:
            steer += 10
            if 40 < steer:
                steer = 40
            bp.set_motor_position(bp.PORT_D, steer)
        elif inp == key.LEFT:
            steer -= 10
            if steer < -40:
                steer = -40
            bp.set_motor_position(bp.PORT_D, steer)
        elif inp == key.SPACE:
            stop()
        elif inp == key.BACKSPACE:
            stop()
            print('bye...')
            exit()
        else:
            continue
        bp.set_motor_power(bp.PORT_B, power)

if __name__ == '__main__':
    main()