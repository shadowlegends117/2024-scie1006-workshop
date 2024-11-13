import datetime
print(f'Hello, now is {datetime.datetime.now()}')
from pymongo import MongoClient
import datetime

# Your URI copied from the MongoDB Atlas website
# Replace <password> with the password you created for your database user
uri = 'mongodb+srv://db:<password>@cluster0...:27017/'
client = MongoClient(uri)
db = client.database      
# Create a record variable to store the sensor data
record = {
   "sensor_id": 1,
   "temp": temperature,
   "humi": humidity,
   "date": datetime.datetime.now(),
}

# Insert the record into the sensors collection
db.sensors.insert_one(record)
from smbus2 import SMBus
import time
from pymongo import MongoClient
import datetime

# Your URI copied from the MongoDB Atlas website
# Replace <password> with the password you created for your database user
uri = 'mongodb+srv://db:<password>@cluster0...:27017/'
client = MongoClient(uri)
db = client.database

bus = SMBus(7)

# The code block inside the while True loop repeats continuously until 
# you press Ctrl+C in the terminal
while True:
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

   # Exercise code: Read and print the humidity data from the sensor
   humidity = ...
   print(...)         
   
   record = {
      "sensor_id": 1,
      "temp": temperature,
      "humi": humidity,
      "date": datetime.datetime.now(),
   }
   
   db.sensors.insert_one(record)
   
   # wait for 60 seconds
   time.sleep(60) 
  
