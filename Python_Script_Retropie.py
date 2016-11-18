#working code!


import os as os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# these will run in another thread when our events are detected
def my_callback(channel):
    os.system("pkill retroarch")

def my_callback2(channel):
    os.system("sudo reboot")

    
GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback, bouncetime=300)
GPIO.add_event_detect(20, GPIO.RISING, callback=my_callback2, bouncetime=300)

try:
    print "Waiting for rising edge on port 24"
    GPIO.wait_for_edge(21, GPIO.RISING)
    os.system("sudo halt")

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit


