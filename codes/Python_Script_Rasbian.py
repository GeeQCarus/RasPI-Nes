
  
import RPi.GPIO as GPIO  # import RPi.GPIO module    
  

GPIO.setmode(GPIO.BCM) # set to BCM numbering
  
# Set up Inputs  
GPIO.setup(16, GPIO.IN)     # set Read kill app 
GPIO.setup(20, GPIO.IN)     # set Read Reboot PI 
GPIO.setup(21, GPIO.IN)     # set Read Shutdown PI 


while(1)  # create an infinite loop because 1 = TRUE, and while it is true it will run, we don't offer an exit so it will loop all day waiting for inputs!
  
if GPIO.input(16):
    print("sudo reboot\n") # no predefined app to kill, setup to reboot anyhow you can delete this line if you wont use it!

else:	
if GPIO.input(20):
    print("sudo reboot\n")  # safely reboot the system

else:	
if GPIO.input(21):
    print("sudo halt\n") # safely shutdown the system

    
  

