# Exercise code: Read and print the humidity data from the sensor
# Fill out the ... below
from smbus2 import SMBus
import time

import datetime
print(f'Hello, now is {datetime.datetime.now()}')

bus = SMBus(7)

# trigger the sensor to do measurement
bus.write_i2c_block_data(0x38, 0xAC, [0x33, 0x00])
# wait for 0.5 seconds 
time.sleep(0.5)
# read data from the sensor
data = bus.read_i2c_block_data(0x38, 0x00, 8)

temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
humi = ((data[1] << 16) | (data[2] << 8) | data[3]) >> 4

temperature = temp / (2**20) * 200 - 50
print(u'Temperature: {0:.1f}°C'.format(temperature))

humidity = humi / (2**20) * 100
print(u'humidity.format(humidity))

