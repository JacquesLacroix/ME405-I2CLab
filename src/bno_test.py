"""! 
@file bno_test.py

"""

from pyb import I2C, Pin
import time

OPR_MODE_REG = 0x3D # OPR_MODE register addr 
BNO055_I2C_ADDR = 0x28 # BNO055 register addr

i2c = I2C(0, I2C.CONTROLLER, baudrate = 100000)

devices = i2c.scan()

if BNO055_I2C_ADDR in devices:
    
    write_register(OPR_MODE_REG, 0x0C)
    
    time.sleep(1)
    
else:
    pass


