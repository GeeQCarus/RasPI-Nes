# taken from http://raspi.tv/2013/rpi-gpio-basics-7-rpi-gpio-cheat-sheet-and-pointers-to-rpi-gpio-advanced-tutorials

# RPi.GPIO Basics cheat sheet - Don't try to run this. It'll fail!  
# Alex Eames http://RasPi.TV  
# http://RasPi.TV/?p=4320  
  
# RPi.GPIO Official Documentation   
# http://sourceforge.net/p/raspberry-gpio-python/wiki/Home/  
  
import RPi.GPIO as GPIO              # import RPi.GPIO module    
  
# choose BOARD or BCM  
GPIO.setmode(GPIO.BCM)               # BCM for GPIO numbering  
GPIO.setmode(GPIO.BOARD)             # BOARD for P1 pin numbering  
  
# Set up Inputs  
GPIO.setup(port_or_pin, GPIO.IN)     # set port/pin as an input  
GPIO.setup(port_or_pin, GPIO.IN,  pull_up_down=GPIO.PUD_DOWN) # input with pull-down  
GPIO.setup(port_or_pin, GPIO.IN,  pull_up_down=GPIO.PUD_UP)   # input with pull-up   
  
# Set up Outputs  
GPIO.setup(port_or_pin, GPIO.OUT)               # set port/pin as an output     
GPIO.setup(port_or_pin, GPIO.OUT, initial=1)    # set initial value option (1 or 0)  
  
# Switch Outputs  
GPIO.output(port_or_pin, 1)     # set an output port/pin value to 1/GPIO.HIGH/True    
GPIO.output(port_or_pin, 0)     # set an output port/pin value to 0/GPIO.LOW/False    
  
# Read status of inputs OR outputs  
i = GPIO.input(port_or_pin)     # read status of pin/port and assign to variable i  
if GPIO.input(port_or_pin):     # use input status directly in program logic  
  
# Clean up on exit  
GPIO.cleanup()  
  
# What Raspberry Pi revision are we running?  
GPIO.RPI_REVISION    #  0 = Compute Module, 1 = Rev 1, 2 = Rev 2, 3 = Model B+  
  
# What version of RPi.GPIO are we running?  
GPIO.VERSION  
  
# What Python version are we running?  
import sys; sys.version  
