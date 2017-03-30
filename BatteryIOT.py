# FYP2017
# Program to send battery status to ThingSpeak channel
# Author: Kunal Jagadeesh
# License: Public Domain

import time
import sys
import urllib.request
import urllib.parse

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Main program loop.
def sendBattery():
    time.sleep(3)
    value = mcp.read_adc(0)
    volts = ((value*3.3)) / float(1023) #voltage divider voltage
    volts = volts * 5.7 #actual voltage
    volts = round(volts,2)
    if (volts >=13.6):
        batt = 100
        time.sleep(1)
        f = open('TS_APIkey.txt','r')
        api_key = f.read()
        params = urllib.parse.urlencode({'key': api_key ,
                                   'field3': batt ,
                                        })
        params = params.encode('utf-8')
        fh = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)
        fh.close()
    else:
        batt = round ((volts))
        time.sleep(1)
        f = open('TS_APIkey.txt','r')
        api_key = f.read()
        params = urllib.parse.urlencode({'key': api_key ,
                                   'field3': batt ,
                                        })
        params = params.encode('utf-8')
        fh = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)
        fh.close()
    print("Value Sent", batt)

if __name__ == "__main__":
    while True:
        sendBattery()
        time.sleep(900)
        
    

