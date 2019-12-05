# Program to control lights in the shelter depending on detected motion
#
# Resources:
# https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio
#

import RPi.GPIO as GPIO
import time

pir = 11    # PIR Motion sensor connected to pin 11 of RPi
relay = 8  # Relay outputs connected to pin 12 of RPi
relayTimer = 10
relayOn = False

GPIO.setmode( GPIO.BOARD )
GPIO.setup( pir, GPIO.IN )
GPIO.setup( relay, GPIO.OUT )

print("Sensor Active, press Ctrl+C to exit")
time.sleep(1)

# Main loop
try: 
  while True:
    if ( relayTimer > 0 ) :
      GPIO.output( relay, 0 )
      relayOn = True 
      if ( GPIO.input( pir ) ) :
        relayTimer = 10
        print("Motion")
      else :
        relayTimer = relayTimer - 1
    else :
      if ( GPIO.input ( pir ) ) :
        GPIO.output( relay, 0 )
        relayOn = True
        relayTimer = 10
        print("Motion")
      else :
        GPIO.output( relay, 1 )
        relayOn = False
      
    time.sleep(1)
    if ( relayOn ) :
      print("LED on")
    else:
      print("LED off")
    
except: KeyboardInterrupt

finally: 
  GPIO.cleanup()
  print("Program ended")
