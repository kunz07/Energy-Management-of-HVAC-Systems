# FYP2017
# Program to establish ZigBee communication between raspberry Pi and arduino
# Complete control of HVAC elements based on commands sent from the Pi
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import serial
from ubidots import ApiClient

one = 1
zero = 0

f = open('Ubidots_APIkey.txt', 'r')
apikey = f.readline().strip()
f.close()
api = ApiClient(token = apikey)

try:
    roomtemp = api.get_variable("58d763b8762542260a851bd1")
    roomhumidity = api.get_variable("58d763c57625422609b8d088")
    cooler = api.get_variable("58d768e0762542260a855c7a")
    heater = api.get_variable("58d768eb7625422609b91152")
    humidifier = api.get_variable("58d768f8762542260cf3b292")
    exhaust = api.get_variable("58d76907762542260dfad769")
    
except ValueError:
    print('Unable to obtain variable')

cooler.save_value({'value': 0})
heater.save_value({'value': 0})
humidifier.save_value({'value': 0})
exhaust.save_value({'value': 0})
    
hour = 3600
PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
 
# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)
 
def getSensorData():
    if ser.isOpen():
        ser.close()
    ser.open()
    ser.isOpen()
    ser.write('s'.encode())
    time.sleep(2)
    response = ser.readline().strip().decode()
    hum = float(response[:5])
    temp = float(response[5:])

    try:
        roomtemp.save_value({'value': temp})
        roomhumidity.save_value({'value': hum})
        print('Value',temp,'and',hum, 'sent')
        time.sleep(2)
    except:
        print('Value not sent')
        
    return (hum, temp)

def level_1():
    h, t = getSensorData()
    if (t > 35):
        cooler.save_value({'value': one})
        time.sleep(2)
    if (t < 15):
        heater.save_value({'value': one})
        time.sleep(2)
    if (h < 25):
        humidifier.save_value({'value': one})
        time.sleep(2)
    if (h > 80):
        exhaust.save_value({'value': one})
        time.sleep(2)
    time.sleep(10)
    cooler.save_value({'value': 0})
    heater.save_value({'value': 0})
    humidifier.save_value({'value': 0})
    exhaust.save_value({'value': 0})

def level_2():
    h, t = getSensorData()
    if (t > 32):
        cooler.save_value({'value': one})
        time.sleep(2)
    if (t < 18):
        heater.save_value({'value': one})
        time.sleep(2)
    if (h < 30):
        humidifier.save_value({'value': one})
        time.sleep(2)
    if (h > 70):
        exhaust.save_value({'value': one})
        time.sleep(2)
    time.sleep(10)
    cooler.save_value({'value': 0})
    heater.save_value({'value': 0})
    humidifier.save_value({'value': 0})
    exhaust.save_value({'value': 0})

def level_3():
    h, t = getSensorData()
    if (t > 30):
        cooler.save_value({'value': one})
        time.sleep(2)
    if (t < 20):
        heater.save_value({'value': one})
        time.sleep(2)
    if (h < 40):
        humidifier.save_value({'value': one})
        time.sleep(2)
    if (h > 60):
        exhaust.save_value({'value': one})
        time.sleep(2)
    time.sleep(10)
    cooler.save_value({'value': 0})
    heater.save_value({'value': 0})
    humidifier.save_value({'value': 0})
    exhaust.save_value({'value': 0})

def level_4():
    h, t = getSensorData()
    if (t > 27):
        cooler.save_value({'value': one})
        time.sleep(2)
    if (t < 22):
        heater.save_value({'value': one})
        time.sleep(2)
    if (h < 25):
        humidifier.save_value({'value': one})
        time.sleep(2)
    if (h > 30):
        exhaust.save_value({'value': one})
        time.sleep(2)
    time.sleep(10)
    cooler.save_value({'value': 0})
    heater.save_value({'value': 0})
    humidifier.save_value({'value': 0})
    exhaust.save_value({'value': 0})
    
def getLevel():
    return 4

if __name__ == "__main__":
    level = getLevel()
    while True:
        if (level == 1):
            level_1()
        elif (level == 2):
            level_2()
        elif (level == 3):
            level_3()
        elif (level == 4):
            level_4()
        else:
            ser.write('x'.encode())
            break
