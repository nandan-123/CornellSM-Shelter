# CornellSM-Shelter
Sustainable Mobility - Shelter

##Electrical Integration
This semester, all the segments of the electrical system of the bus shelter were tested individually and integrated into a single system. The system functions with a Raspberry Pi as the main computer. The various segments of this system are as follows: 
Collect data from the Renogy Rover solar charge controller about solar power, battery consumption, etc.
Display real-time information about incoming buses on an LCD screen in the shelter
Control the lights inside the shelter depending on activity computed based on input from a motion sensor
Indicator lights outside the shelter that glow depending on time before the next bus arrives

#Solar data collection
After a thorough investigation of various solar charge controllers last year, we finalized the Renogy Rover Li 40A MPPT Charge Controller. It is an MPPT (Maximum Power Point Tracking) controller that minimizes wastage of solar energy. The controller connects easily to the Raspberry Pi and communicates using the RS-232 protocol. We used the Solarshed Python library (https://github.com/corbinbs/solarshed) to establish a connection with the charge controller and obtain information about important factors about the solar power system like charging status, load power, solar power, solar current, battery voltage, etc. 

All the data obtained from the charge controller is temporarily stored in the Raspberry Pi storage in a text file in the form of a JSON string. The structure of this JSON string is as follows: 
{
  “charging_status”: 0.8, 
  “load_power”: 34, 
  “solar_power”: 50,
  “power_today” : 16
} 

This text file is used by the Javascript program running on the Raspberry Pi for the information display as described in the next section. In the future, this data can be stored on a cloud database for reference and analysis. 

#Information Display

#Efficient power control
In order to manage power consumption in the shelter so that the solar power generated sufficiently accounts for all the energy consumed, we implemented a smart power control. This system ensures that the electrical components of the shelter like the LCD display and overhead lights are turned off when the shelter has been inactive for a long time. This was done using a PIR (Passive InfraRed) Motion Sensor which simply detects whether a human has moved in or out of its range. We decided on using the HC-SR501 sensor module which is easy to set up with a Raspberry Pi. When the sensor doesn’t detect any movement in its range for a long time, the system turns off the lights inside the shelter and puts the LCD display on standby until the sensor detects any motion again. The lights are controlled using a relay module in which the 5V relays are operated by the Raspberry Pi, which disconnects the lights from the power supply when required. The Pi also sends an internal standby signal to the LCD display to turn it off.
