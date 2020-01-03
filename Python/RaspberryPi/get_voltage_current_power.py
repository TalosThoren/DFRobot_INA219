# -*- coding: utf-8 -*-

'''
file get_voltage_current_power.py
SEN0291 Wattmeter Sensor
This sensor can detect Voltage ,Current,and Power
The module has four I2C, these addresses are:

ADDRESS 1  0x40   A0 = 0  A1 = 0
ADDRESS 2  0x41   A0 = 1  A1 = 0
ADDRESS 3  0x44   A0 = 0  A1 = 1
ADDRESS 4  0x45   A0 = 1  A1 = 1

Copyright    [DFRobot](http://www.dfrobot.com), 2016
Copyright    GNU Lesser General Public License
version  V1.0
date  2019-2-27
'''
import time
import logging
from DFRobot_INA219 import INA219

'''
Revise the following two paramters according to actual reading of the INA219 and the multimeter
for linearly calibration
'''
logging.basicConfig( filename="./testing.log" )

ina219_reading_mA = 1000
ext_meter_reading_mA = 1000

#Change I2C address by dialing DIP switch
ina = INA219(1, INA219.INA219_I2C_ADDRESS4)

#begin return True if succeed, otherwise return False
while not ina.begin():
    time.sleep(2)

ina.linear_cal(ina219_reading_mA, ext_meter_reading_mA)

def main():
    logger = logging.getLogger('ina219_sensor')
    logger.setLevel( logging.INFO )

    while True:
        time.sleep(1)
        sensorValues = _readSensorValues()
        logger.info( "%s", sensorValues )

def _readSensorValues():
    sensorValues = {
        "ShuntVoltage": ina.get_shunt_voltage_mV(),
        "BusVoltage": ina.get_bus_voltage_V(),
        "CurrentMilliAmps": ina.get_current_mA(),
        "PowerMilliWatts": ina.get_power_mW()
    }
    return sensorValues


if __name__ == "__main__":
    main()
