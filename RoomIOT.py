# FYP2017
# Program to send room temperature and humidity to ThingSpeak
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import serial
import sys
import urllib.request
import urllib.parse

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
    # Send to ThingSpeak
    f = open('TS_APIkey.txt','r')
    api_key = f.read()
    params = urllib.parse.urlencode({'key': api_key ,
                                   'field4': temp ,
                                   'field5': hum
                                        })
    params = params.encode('utf-8')
    fh = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)
    fh.close()

if __name__ == "__main__":
    while True:
        sendData()
        time.sleep(300)
