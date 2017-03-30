# FYP2017
# Program to establish ZigBee communication between raspberry Pi and arduino
# Complete control of HVAC elements based on commands sent from the Pi
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import serial
import Fuzzy

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
    if (t > 35):
        ser.write('c'.encode())
    if (t < 15):
        ser.write('f'.encode())
    if (h < 25):
        ser.write('h'.encode())
    if (h > 80):
        ser.write('e'.encode())
    time.sleep(300)

def level_2():
    h, t = getSensorData()
    if (t > 32):
        ser.write('c'.encode())
    if (t < 18):
        ser.write('f'.encode())
    if (h < 30):
        ser.write('h'.encode())
    if (h > 70):
        ser.write('e'.encode())
    time.sleep(300)

def level_3():
    h, t = getSensorData()
    if (t > 30):
        ser.write('c'.encode())
    if (t < 20):
        ser.write('f'.encode())
    if (h < 40):
        ser.write('h'.encode())
    if (h > 60):
        ser.write('e'.encode())
    time.sleep(300)

def level_4():
    h, t = getSensorData()
    if (t > 27):
        ser.write('c'.encode())
    if (t < 22):
        ser.write('f'.encode())
    if (h < 25):
        ser.write('h'.encode())
    if (h > 50):
        ser.write('e'.encode())
    time.sleep(300)
def getLevel():
    return (int(fuzzy.level))

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
