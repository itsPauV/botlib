import brickpi3
import time
BP = brickpi3.BrickPi3()
BP.set_motor_power(BP.PORT_B, 20)
time.sleep(0.5)
BP.set_motor_power(BP.PORT_B, 0)
