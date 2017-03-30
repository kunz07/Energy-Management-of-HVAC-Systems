# FYP2017
# Program to read battery voltage and display it on OLED
# Author: Kunal Jagadeesh
# License: Public Domain

import time

# OLED modules
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 32

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Initialize library.
disp.begin()
time.sleep(10)

width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Main program loop.
time.sleep(3)
# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
value = mcp.read_adc(0)
volts = ((value*3.3)) / float(1023) #voltage divider voltage
volts = volts * 5.7 #actual voltage
volts = round(volts,2)
if (volts >=13.6):
    batt = 100
    print('100% Battery')
    draw.text((0, 0), 'Battery percent at: ',font=font, fill = 255)
    draw.text((50, 20),str(batt) , font=font, fill = 255)
    disp.image(image)
    disp.display()
    time.sleep(1)
elif (volts > 11.6):
    batt = round ((volts - 11.6) * 50,1)
    print(batt,'% Battery')
    draw.text((10, 0), 'Battery percent at: ',font=font, fill = 255)
    draw.text((45, 20),str(batt) , font=font, fill = 255)
    disp.image(image)
    disp.display()
    time.sleep(1)
else:
    print('Connection Error')
    draw.text((55, 10),':(' , font=font, fill = 255)
    disp.image(image)
    disp.display()
    # Print the ADC values.
    # Pause time.
    time.sleep(1)
    

