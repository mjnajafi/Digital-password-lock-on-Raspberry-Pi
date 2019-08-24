#Mohammad Javad NajafiRad
#E-mail: mjnajafi@yahoo.com
#Linkedin: https://www.linkedin.com/in/mjnajafi/

#This file is for testing Keypad. When every key is pressed, will print in cmd.

#import library
import time                        #import delay time
from pad4pi import rpi_gpio        #connect to keypad
import RPi.GPIO as GPIO            #connect to RPi
GPIO.setwarnings(False)            #disable warnings

#define Pins
KEYPAD=[
    [1,2,3,"A"]
    [4,5,6,"B"]
    [7,8,9,"C"]
    ["*",0,"#","D"]
    ]

ROW_PINS=[21,20,16,12]
COL_PINS=[26,19,13,6]


factory=rpi_gpio.KeypadFactory()              #connect Pins to default library
keypad=factory.create_keypad(keypad=KEYPAD,
                             row_pins=ROW_PINS, col_pins=COL_PINS)

def printKey(key):
    print (key)


#main loop
while True:                                    #unlimited loop
    keypad.registerKeyPressHandler(printKey)   #get key
    time.sleep(.5)                             #delay 500ms
    keypad.clearKeyPressHandlers()             #clear key
