# FYP2017
# Program to send average forecastof temperature and cloud cover to ThingSpeak
# Author: Kunal Jagadeesh
# License: Public Domain


from forecastiopy import *
import datetime
import sys
import urllib.request
import urllib.parse
import time

hour = 3600

def sendForecast():
    f = open('DS_APIkey.txt','r')
    apikey = f.read()
    f.close()

    Bangalore = [12.9716, 77.5946]

    fio = ForecastIO.ForecastIO(apikey,
                                units=ForecastIO.ForecastIO.UNITS_SI,
                                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                latitude=Bangalore[0], longitude=Bangalore[1],
                                )
    tempc = 0
    clouds = 0
    if fio.has_hourly() is True:
        hourly = FIOHourly.FIOHourly(fio)
        for hour in range(0, 48):
            tempc = tempc + float(str(hourly.get_hour(hour)['temperature']))
            clouds = clouds + float(str(hourly.get_hour(hour)['cloudCover']))
    else:
        print('No Hourly data')

    tempc = round(tempc / 48, 2)
    clouds = round(clouds / 48, 2)

    #Send Data to ThingSpeak
    fl = open('TS_APIkey.txt','r')
    api_key = fl.read()
    params = urllib.parse.urlencode({'key': api_key ,
                                       'field1': tempc ,
                                       'field2': clouds
                                            })
    params = params.encode('utf-8')
    fh = urllib.request.urlopen("https://api.thingspeak.com/update", data=params)
    fh.close()

if __name__ == "__main__":
    while True:
        sendForecast()
        time.sleep(hour * 24)
    
