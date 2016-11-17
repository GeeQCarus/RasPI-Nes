# DO NOT TRY TO RUN THIS PY SCRIPT IT WILL FAIL!

# get more info from:
# http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/  
  
import RPi.GPIO as GPIO              # import RPi.GPIO module    
  
# choose BCM
GPIO.setmode(GPIO.BCM)               # BCM for GPIO numbering  

  
# Set up Inputs  
GPIO.setup(16, GPIO.IN)     # set Read kill app
GPIO.setup(20, GPIO.IN)     # set Read Reboot PI 
GPIO.setup(21, GPIO.IN)     # set Read Shutdown PI 




# then 2 options, the while and the interrupt

#option 1

#end of option 1
#********************************************
# option 2
while(1)
# Switch Outputs  

  
if GPIO.input(16):
    print("Pin 11 is HIGH")

    
    
#enf of option 2
  



# inspired by http://raspi.tv/2013/rpi-gpio-basics-7-rpi-gpio-cheat-sheet-and-pointers-to-rpi-gpio-advanced-tutorials
