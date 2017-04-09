# FYP2017
# Program to send average forecastof temperature and cloud cover to ThingSpeak
# Author: Kunal Jagadeesh
# License: Public Domain


from forecastiopy import *
import datetime
import sys
from ubidots import ApiClient
import time

hour = 3600

f = open('Ubidots_APIkey.txt', 'r')
apikey = f.readline().strip()
f.close()
api = ApiClient(token = apikey)

try:
    temp = api.get_variable("58d76383762542260cf36d8f")
    cloud_cover = api.get_variable("58d76394762542260a851a05")
except ValueError:
    print('Unable to obtain variable')
    
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

    try:
        temp.save_value({'value': tempc})
        cloud_cover.save_value({'value': clouds})
        print('Value',tempc,'and',clouds, 'sent')
        time.sleep(2)
    except:
        print('Value not sent')
	
    return(tempc, clouds)

if __name__ == "__main__":
    while True:
        temp, clouds = sendForecast()
        time.sleep(5)
    
