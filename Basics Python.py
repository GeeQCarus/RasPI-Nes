# DO NOT TRY TO RUN THIS PY SCRIPT IT WILL FAIL!
#the only use of this py script is to teach how to use your py

# get more info from:
# http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/  
  
import RPi.GPIO as GPIO              # import RPi.GPIO module    
  
# choose BOARD or BCM ****  I prefer BCP
GPIO.setmode(GPIO.BCM)               # BCM for GPIO numbering  
GPIO.setmode(GPIO.BOARD)             # BOARD for P1 pin numbering  


 
# Set up Inputs  
GPIO.setup(port_or_pin, GPIO.IN)     # this will be triggered by the 3.3v logic output of the arduino
GPIO.setup(port_or_pin, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  similar to the arduino neet to attach to a button and ground
GPIO.setup(port_or_pin, GPIO.IN,  pull_up_down=GPIO.PUD_UP)   # input with pull-up  similar to the arduino neet to attach to a button and ground  

# using Inputs  
if GPIO.input(16):
    print("enter a terminal command")



# Set up Outputs  
GPIO.setup(port_or_pin, GPIO.OUT)               # set port/pin as an output     
GPIO.setup(port_or_pin, GPIO.OUT, initial=1)    # set initial value option (1 or 0)  
  
# Switch Outputs  
GPIO.output(port_or_pin, 1)     # set an output port/pin value to 1/GPIO.HIGH/True    
GPIO.output(port_or_pin, 0)     # set an output port/pin value to 0/GPIO.LOW/False  


#**************************************************************************

#!/usr/bin/env python2.7  
# script by Alex Eames http://RasPi.tv  
  
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
  
# GPIO 23 & 24 set up as inputs. One pulled up, the other down.  
# 23 will go to GND when button pressed and 24 will go to 3V3 (3.3V)  
# this enables us to demonstrate both rising and falling edge detection  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def my_callback(channel):  
    print "Rising edge detected on port 24 - even though, in the main thread,"  
    print "we are still waiting for a falling edge - how cool?\n"  
  
print "Make sure you have a button connected so that when pressed"  
print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"  
print "You will also need a second button connected so that when pressed"  
print "it will connect GPIO port 24 (pin 18) to 3V3 (pin 1)"  
raw_input("Press Enter when ready\n>")  
  
# The GPIO.add_event_detect() line below set things up so that  
# when a rising edge is detected on port 24, regardless of whatever   
# else is happening in the program, the function "my_callback" will be run  
# It will happen even while the program is waiting for  
# a falling edge on the other button.  
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)  
  
try:  
    print "Waiting for falling edge on port 23"  
    GPIO.wait_for_edge(23, GPIO.FALLING)  
    print "Falling edge detected. Here endeth the second lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
    
    

  



# inspired by http://raspi.tv/2013/rpi-gpio-basics-7-rpi-gpio-cheat-sheet-and-pointers-to-rpi-gpio-advanced-tutorials
