# FYP2017
# Program to send room temperature and humidity to ThingSpeak
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import serial
import sys
from ubidots import ApiClient

f = open('Ubidots_APIkey.txt', 'r')
apikey = f.readline().strip()
f.close()
api = ApiClient(token = apikey)

try:
    roomtemp = api.get_variable("58d763b8762542260a851bd1")
    roomhumidity = api.get_variable("58d763c57625422609b8d088")
except ValueError:
    print('Unable to obtain variable')
    

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
 
# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)
 
def sendData():
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
    
if __name__ == "__main__":
    while True:
        sendData()
        time.sleep(5)
