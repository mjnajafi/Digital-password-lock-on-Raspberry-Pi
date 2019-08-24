#Mohammad Javad NajafiRad
#E-mail: mjnajafi@yahoo.com
#Linkedin: https://www.linkedin.com/in/mjnajafi/

#This file is for launch and test the LCD


#import library
import time                         #import delay time
import RPi.GPIO as GPIO             #connect to RPi Pins
from RPLCD import CharLCD           #connect to LCD. showing character
from RPLCD import cleared           #connect to LCD. clear LCD
GPIO.setwarnings(False)             #disable warnings
 

#define pins
lcd = CharLCD(cols=16, rows=2, pin_rw=None,     #16*2 LCD
              pin_rs=7, pin_e=8,                #pin_reset and pin_enable
              pins_data=[25,24,23,18],          #pin_data 
              numbering_mode=GPIO.BCM)          #BCM mode

              
#main loop
while True:                                   #unlimited loop
    lcd.cursor_pos=(0,0)                      #define start point column=0 row=0
    lcd.write_string('Mohammad Javad')        #sample text
    time.sleep(1)                             #delay time
    with cleared(lcd):
        lcd.write_string(u'')                 #clear LCD

    lcd.cursor_pos=(1,0)                      #define start point: column=0 row=1
    lcd.write_string('Najafi Rad')            #sample text
    time.sleep(1)                             #delay time
    with cleared(lcd):
        lcd.write_string(u'')                 #clear LCD

    
    
