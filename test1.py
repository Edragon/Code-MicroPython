# main.py -- put your code here!
import pyb

while True:
    pyb.LED(2).on()
    pyb.delay(1000)
    pyb.LED(2).off()
    pyb.delay(1000)

