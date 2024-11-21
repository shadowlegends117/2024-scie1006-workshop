from pymongo import MongoClient
import datetime
import pyttsx3

# Your URI copied from the MongoDB Atlas website
# Replace <password> with the password you created for your database user
uri = 'mongodb+srv://adrianlamyc:aVdgzKgHl8dQqHt7@cluster0.zhbxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(uri)
db = client.database      

# Exercise code: Read and print the humidity data from the sensor
# Fill out the ... below
from smbus2 import SMBus
import time
bus = SMBus(7)

engine = pyttsx3.init()
engine.say("Program started")
engine.runAndWait()

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

    engine = pyttsx3.init()
    engine.say(u'Temperature is now {0:.1f}°'.format(temperature))
    engine.runAndWait()

    humidity = humi / (2**20) * 100
    # print(humidity)
    print(u'Humidity: {0:.1f}%'.format(humidity))
    # Exercise: Output humidity value with speech
    # Fill out the ... below
    engine = pyttsx3.init()
    engine.say(u'Humidity: {0:.1f}%'.format(humidity))
    engine.runAndWait()
    # Create a record variable to store the sensor data
    record = {
        "sensor_id": 1,
        "temp": temperature,
        "humi": humidity,
        "date": datetime.datetime.now(),
    }

    # Insert the record into the sensors collection
    db.sensors.insert_one(record)

    # wait for 60 seconds
    time.sleep(60) 
