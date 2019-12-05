# Program to control lights in the shelter depending on detected motion
#
# Resources:
# https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio
#

import RPi.GPIO as GPIO
import time

pir = 11    # PIR Motion sensor connected to pin 11 of RPi
relay = 12  # Relay outputs connected to pin 12 of RPi
relayTimer = 1000

GPIO.setmode( GPIO.BOARD )
GPIO.setup( pir, GPIO.IN )
GPIO.setup( relay, GPIO.OUT )

# Main loop
while True:
  if ( relayTimer > 0 ) :
    GPIO.output( relay, 1 ) 
    if ( GPIO.input( pir ) ) :
      relayTimer = 1000
    else :
      relayTimer = relayTimer - 1
  else :
    if ( GPIO.input ( pir ) ) :
      GPIO.output( relay, 1 )
      relayTimer = 1000
    else :
      GPIO.output( relay, 0 )
      
  time.sleep(1)
