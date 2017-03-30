# FYP2017
# Program to send battery status to ThingSpeak channel
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import sys
from ubidots import ApiClient

f = open('Ubidots_APIkey.txt', 'r')
apikey = f.readline().strip()
f.close()
api = ApiClient(token = apikey)

try:
    variable1 = api.get_variable("58d763aa762542260cf36f24")

except ValueError:
    print('Unable to obtain variable')

def sendBattery(x):
    try:
        batt = x
        variable1.save_value({'value': batt})
        print('Value ',batt, ' sent')
        time.sleep(2)
    except:
        print('Value not sent')

if __name__ == "__main__":
    x = 40
    while True:
        sendBattery(x)
        x = x - 5
        time.sleep(5)
        if x < 5:
            break

