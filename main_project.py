#Written By: Mohammad Javad NajafiRad
#E-mail: mjnajafi@yahoo.com
#Linkedin: https://www.linkedin.com/in/mjnajafi/


#Import Library

import time                         #import delay time
from pad4pi import rpi_gpio         #connect to keypad
from RPLCD import CharLCD           #connect to LCD. showing character
from RPLCD import cleared           #connect to LCD. clear LCD
import RPi.GPIO as GPIO             #connect to RPi
GPIO.setmode(GPIO.BCM)              #set BCM mode
GPIO.setwarnings(False)             #disable warnings
GPIO.setup(14,GPIO.OUT)             #config LED as output
GPIO.output(14,GPIO.LOW)            #set low for LED

#Define Pins

print ("run...")

lcd = CharLCD(cols=16, rows=2, pin_rw=None,     #16*2 LCD
              pin_rs=7, pin_e=8,                #pin_reset and pin_enable
              pins_data=[25,24,23,18],          #pin_data 
              numbering_mode=GPIO.BCM)          #BCM mode

KEYPAD=[
    [1,2,3,"A"]
    [4,5,6,"B"]
    [7,8,9,"C"]
    ["*",0,"#","D"]
    ]

ROW_PINS=[21,20,16,12]
COL_PINS=[26,19,13,6]


factory=rpi_gpio.KeypadFactory()               #set deafult Keypad 
keypad=factory.create_keypad(keypad=KEYPAD,
                             row_pins=ROW_PINS, col_pins=COL_PINS)

time.sleep(1)                                 #delay at beginning

lcd.cursor_pos=(0,0)  
with cleared(lcd):
        lcd.write_string(u'')                 #clear LCD at beginnig
lcd.cursor_pos=(1,0)   
with cleared(lcd):
        lcd.write_string(u'')

lcd.cursor_pos=(0,0)                          #define start point column=0 row=0
lcd.write_string('Raspberry Pi')              #sample text
time.sleep(2)                                 #delay time
    
lcd.cursor_pos=(0,0)                          #define start point column=0 row=0
lcd.write_string('Insert Password')           #sample text
                          
lcd.cursor_pos=(1,0)                          #define start point column=0 row=1

password="1234"                               #default password
i=0
h=""
password_flag=0


def printKey(key):
    global i
    global h
    global password_flag  
    h +=str(key)                              #show the entered password at 2th row
    lcd.cursor_pos=(1,0)
    lcd.write_string(h)
    time.sleep(.5)

    i +=1
    if i==4:
        if h==password:
            lcd.cursor_pos=(0,0)                      
            lcd.write_string('Password True')
            lcd.cursor_pos=(1,0)                  #clear 2th row      
            lcd.write_string('             ')
            password_flag==1
        else:
            lcd.cursor_pos=(0,0)                      
            lcd.write_string('Password False')
            lcd.cursor_pos=(1,0)                  #clear 2th row      
            lcd.write_string('             ')
            time.sleep(3)
            lcd.cursor_pos=(0,0)                   
            lcd.write_string('Insert Password')
            i=0
            h=""

            
#Main Loop
            
while True:                                    #unlimited loop
    keypad.registerKeyPressHandler(printKey)   #get key
    time.sleep(.5)                             #delay 500ms
    keypad.clearKeyPressHandlers()             #clear key

    if password_flag==1:
        GPIO.output(14,GPIO.HIGH)              #if password is True, turn on the LED
        time.sleep(10)
        break
    

