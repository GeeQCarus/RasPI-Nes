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



    
    

  



# inspired by http://raspi.tv/2013/rpi-gpio-basics-7-rpi-gpio-cheat-sheet-and-pointers-to-rpi-gpio-advanced-tutorials
