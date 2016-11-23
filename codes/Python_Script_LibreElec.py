#working code!

# start with the following 2 lines, remove the # 1)etc....

# 1)  mkdir /script
# 2)  nano /script/gpioscript.py

#copy the following code until the next commented line

import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')

import os as os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# these will run in another thread when our events are detected
def my_callback(channel):
        os.system("reboot")
def my_callback2(channel):
        os.system("reboot")

GPIO.add_event_detect(16, GPIO.RISING, callback=my_callback, bouncetime=300)
GPIO.add_event_detect(20, GPIO.RISING, callback=my_callback2, bouncetime=300)

try:
        print "Waiting for rising edge on port 24"
        GPIO.wait_for_edge(21, GPIO.RISING)
        os.system("halt")

except KeyboardInterrupt:

        GPIO.cleanup() # clean up GPIO on CTRL+C exit

GPIO.cleanup()           # clean up GPIO on normal exit



http://www.barryhubbard.com/raspberry-pi/howto-raspberry-pi-openelec-power-wake-shutdown-button-using-gpio/

mkdir /storage/script
nano /storage/script/gpioscript.py 

nano /storage/.config/autostart.sh
python /storage/script/gpioscript.py &

test python /storage/script/gpioscript.py

# type nano /etc/rc.local

#highlight the line right before :" exit 0 "
#type :         python /script/gpioscript.py &
