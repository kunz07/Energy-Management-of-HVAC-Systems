# FYP2017
# Program to get average forecast of temperature and cloud cover for 2 days
# Author: Kunal Jagadeesh
# License: Public Domain

from forecastiopy import *
import datetime

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
