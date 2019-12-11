# Program to control indicator lights on the shelter based on time of arrival
#
# Resources:
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
#

import RPi.GPIO as GPIO
import time
import json

relay = 10

GPIO.setmode( GPIO.BOARD )
GPIO.setup( relay, GPIO.OUT )

# Main loop
try :
  while True:
    time.sleep(1)
    with open ('BusTime.json') as json_file :
      jsonTime = json.loads(json_file)
      print( jsonTime )
      time = jsonTime['firstTime']
      
      if time < 1 :
        GPIO.output( relay, 0 )
      
  except: KeyboardInterrupt
  
  finally: 
    GPIO.cleanup()
    print("Program ended")
