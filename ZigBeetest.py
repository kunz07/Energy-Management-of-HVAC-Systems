# FYP2017
# Program to establish ZigBee communication between raspberry Pi and arduino
# Complete control of HVAC elements based on commands sent from the Pi (TESTING)
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import serial
#import fuzzy

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
    return (hum, temp)

def level_1():
    h, t = getSensorData()
    print('humidity is: ',h)
    print('Temperature is: ',t)
    print('Running in level 1..')
    if (t > 35):
        ser.write('c'.encode())
        print('Cooler on')
    if (t < 15):
        ser.write('f'.encode())
        print('Heater on')
    if (h < 25):
        ser.write('h'.encode())
        print('Humidifier on')
    if (h > 80):
        ser.write('e'.encode())
        print('Exhaust on')
    time.sleep(300)

def level_2():
    h, t = getSensorData()
    print('humidity is: ',h)
    print('Temperature is: ',t)
    print('Running in level 2..')
    if (t > 32):
        ser.write('c'.encode())
        print('Cooler on')
    if (t < 18):
        ser.write('f'.encode())
        print('Heater on')
    if (h < 30):
        ser.write('h'.encode())
        print('Humidifier on')
    if (h > 70):
        ser.write('e'.encode())
        print('Exhaust on')
    time.sleep(300)

def level_3():
    h, t = getSensorData()
    print('humidity is: ',h)
    print('Temperature is: ',t)
    print('Running in level 3..')
    if (t > 30):
        ser.write('c'.encode())
        print('Cooler on')
    if (t < 20):
        ser.write('f'.encode())
        print('Heater on')
    if (h < 40):
        ser.write('h'.encode())
        print('Humidifier on')
    if (h > 60):
        ser.write('e'.encode())
        print('Exhaust on')
    time.sleep(300)

def level_4():
    h, t = getSensorData()
    print('humidity is: ',h)
    print('Temperature is: ',t)
    print('Running in level 4..')
    if (t > 28):
        ser.write('c'.encode())
        print('Cooler on')
    if (t < 22):
        ser.write('f'.encode())
        print('Heater on')
    if (h < 25):
        ser.write('h'.encode())
        print('Humidifier on')
    if (h > 50):
        ser.write('e'.encode())
        print('Exhaust on')
    time.sleep(300)


def getLevel():
    return 2 #int(fuzzy.level)

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
