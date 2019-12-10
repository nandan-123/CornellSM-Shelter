# Program to collect data from the Renogy Rover charge controller and stores in a data file as json string

# Uses the Solarshed library https://github.com/corbinbs/solarshed
# Resource: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/

import json
import time
from solarshed.controllers.renogy_rover import RenogyRover

controller = RenogyRover( '/dev/ttyUSB0', 1 )

try:
  while True :
    time.sleep(10)
  
    data = {}
  
    current_time = time.localtime()
    time_str = time.strftime("%H:%M:%S", current_time)
    data['time'] = time_str
  
    data['model'] = controller.model()
    data['battery_percentage'] = controller.battery_percentage()
    data['battery_voltage'] = controller.battery_voltage()
    data['battery_temp'] = controller.battery_temperature()
    #data['controller_temp'] = controller.temperature()
    data['load_voltage'] = controller.load_voltage()
    data['load_current'] = controller.load_current()
    data['load_power'] = controller.load_power()
    data['charging_status'] = controller.charging_status_label()
    data['solar_voltage'] = controller.solar_voltage()
    data['solar_current'] = controller.solar_current()
    data['solar_power'] = controller.solar_power()
    data['power_gen_today'] = controller.power_generation_today()
    data['charge_amh_today'] = controller.charging_amp_hours_today()
    data['discharge_amh_today'] = controller.discharging_amp_hours_today()
  
    with open('SolarData.json', 'w') as outfile:
      json.dump(data, outfile)
  
#except: KeyboardInterrupt

finally: 
  print("Program ended")
  
