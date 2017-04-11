# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from forecastiopy import *
import datetime
import sys
from ubidots import ApiClient
import time
import webbrowser
from threading import Thread
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os.path
import serial

class MovieSplashScreen(QSplashScreen):

    def __init__(self, movie, parent = None):
    
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())
        
        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)
        
    def showEvent(self, event):
        self.movie.start()
    
    def hideEvent(self, event):
        self.movie.stop()
    
    def paintEvent(self, event):
    
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)
    
    def sizeHint(self):
    
        return self.movie.scaledSize()
    
    def mousePressEvent(self, mouse_event):
        pass
        
class Ui_system(object):
    done1 = False
    done2 = False
    done3 = False
    t = 0
    c = 0
    b = 0
    eco = 0
    roomt = 0
    roomh = 0
    def setupUi(self, system):
        system.setObjectName("system")
        system.resize(800, 600)
        system.setWindowTitle("Energy Management System")
        system.setStyleSheet("background-color: rgb(44, 0, 30);")
        self.Fuzzy_system = QtWidgets.QWidget()
        self.Fuzzy_system.setEnabled(True)
        self.Fuzzy_system.setGeometry(QtCore.QRect(0, 0, 800, 538))
        self.Fuzzy_system.setObjectName("Fuzzy_system")
        self.title_1 = QtWidgets.QLabel(self.Fuzzy_system)
        self.title_1.setGeometry(QtCore.QRect(150, -20, 503, 85))
        self.title_1.setStyleSheet("font: 36pt \"Peace Sans\";\n"
"color: rgb(233, 84, 32);")
        self.title_1.setObjectName("title_1")
        self.time_hours = QtWidgets.QLabel(self.Fuzzy_system)
        self.time_hours.setGeometry(QtCore.QRect(576, 60, 121, 121))
        self.time_hours.setStyleSheet("font: 76pt \"Slim Joe\";\n"
"color:rgb(238, 247, 251);")
        self.time_hours.setObjectName("time_hours")
        self.time_min = QtWidgets.QLabel(self.Fuzzy_system)
        self.time_min.setGeometry(QtCore.QRect(710, 80, 67, 41))
        self.time_min.setStyleSheet("font: 26pt \"Big John\";\n"
"color:rgb(238, 247, 251);")
        self.time_min.setText("")
        self.time_min.setObjectName("time_min")

        self.time_hours.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.time_min.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(1000)
        self.timer1.timeout.connect(self.Time)
        self.timer1.start()
        
        self.date = QtWidgets.QLabel(self.Fuzzy_system)
        self.date.setGeometry(QtCore.QRect(700, 130, 101, 21))
        self.date.setStyleSheet("font: 10pt \"Big John\";\n"
"color:rgb(238, 247, 251);")
        self.date.setText("")
        self.date.setObjectName("date")

        self.date.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.Date)
        self.timer2.start()
        
        self.run_system = QtWidgets.QPushButton(self.Fuzzy_system)
        self.run_system.setGeometry(QtCore.QRect(230, 480, 361, 51))
        self.run_system.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Big John\";")
        self.run_system.setObjectName("run_system")

        self.run_system.clicked.connect(self.Run_System)
        
        self.avg_temp = QtWidgets.QLabel(self.Fuzzy_system)
        self.avg_temp.setGeometry(QtCore.QRect(0, 100, 121, 51))
        self.avg_temp.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgbrgb(85, 85, 255);")
        self.avg_temp.setObjectName("avg_temp")

        self.avg_temp.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.temp_icon = QtWidgets.QLabel(self.Fuzzy_system)
        self.temp_icon.setGeometry(QtCore.QRect(340, 110, 32, 32))
        self.temp_icon.setStyleSheet("font: 26pt \"Big John\";\n"
"color:rgb(174, 167, 159)")
        self.temp_icon.setObjectName("temp_icon")
        self.avg_cc = QtWidgets.QLabel(self.Fuzzy_system)
        self.avg_cc.setGeometry(QtCore.QRect(0, 170, 121, 51))
        self.avg_cc.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(85, 85, 255);")
        self.avg_cc.setObjectName("avg_cc")

        self.avg_cc.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.avg_batt = QtWidgets.QLabel(self.Fuzzy_system)
        self.avg_batt.setGeometry(QtCore.QRect(0, 240, 121, 51))
        self.avg_batt.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(85, 85, 255);")
        self.avg_batt.setObjectName("avg_batt")

        self.avg_batt.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(1000 * 900)
        self.timer3.timeout.connect(self.Update_Battery)
        self.timer3.start()
        
        self.battery_percent = QtWidgets.QPushButton(self.Fuzzy_system)
        self.battery_percent.setGeometry(QtCore.QRect(120, 250, 221, 32))
        self.battery_percent.setStyleSheet("font: 75 11pt \"Moon\";\n"
"color: rgb(200, 226, 240);")

        self.battery_percent.clicked.connect(self.Batt_Percent)
        
        self.battery_percent.setObjectName("battery_percent")        
        self.batt_icon = QtWidgets.QLabel(self.Fuzzy_system)
        self.batt_icon.setGeometry(QtCore.QRect(340, 250, 32, 32))
        self.batt_icon.setStyleSheet("font: 26pt \"Big John\";\n"
"color:rgb(174, 167, 159)")
        self.batt_icon.setObjectName("batt_icon")
        self.cloud_icon = QtWidgets.QLabel(self.Fuzzy_system)
        self.cloud_icon.setGeometry(QtCore.QRect(340, 180, 32, 32))
        self.cloud_icon.setStyleSheet("font: 26pt \"Big John\";\n"
"color:rgb(174, 167, 159)")
        self.cloud_icon.setObjectName("cloud_icon")
        self.average_cloud_cover = QtWidgets.QPushButton(self.Fuzzy_system)
        self.average_cloud_cover.setGeometry(QtCore.QRect(120, 180, 221, 32))
        self.average_cloud_cover.setStyleSheet("font: 75 11pt \"Moon\";\n"
"color: rgb(200, 226, 240);")
        self.average_cloud_cover.setObjectName("average_cloud_cover")

        self.average_cloud_cover.clicked.connect(self.Avg_CC)
        
        self.defuzz = QtWidgets.QLabel(self.Fuzzy_system)
        self.defuzz.setGeometry(QtCore.QRect(240, 380, 161, 71))
        self.defuzz.setStyleSheet("font: 40pt \"Big John\";\n"
"color:rgb(238, 247, 251);")
        self.defuzz.setObjectName("defuzz")        
        self.defuzzification = QtWidgets.QPushButton(self.Fuzzy_system)
        self.defuzzification.setGeometry(QtCore.QRect(50, 400, 179, 32))
        self.defuzzification.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color: rgb(34, 139, 34)")
        self.defuzzification.setObjectName("defuzzification")

        self.defuzzification.clicked.connect(self.Defuzz)
        
        self.economy_level = QtWidgets.QPushButton(self.Fuzzy_system)
        self.economy_level.setGeometry(QtCore.QRect(450, 400, 179, 32))
        self.economy_level.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color: rgb(34, 139, 34)")
        self.economy_level.setObjectName("economy_level")

        self.economy_level.clicked.connect(self.Eco)
        
        self.temperature = QtWidgets.QPushButton(self.Fuzzy_system)
        self.temperature.setGeometry(QtCore.QRect(500, 200, 161, 26))
        self.temperature.setStyleSheet("color:rgb(200, 226, 240);\n"
"font: 75 11pt \"Moon\";")
        self.temperature.setObjectName("temperature")
        self.average_temperature = QtWidgets.QPushButton(self.Fuzzy_system)
        self.average_temperature.setGeometry(QtCore.QRect(120, 110, 221, 32))
        self.average_temperature.setStyleSheet("font: 75 11pt \"Moon\";\n"
"color: rgb(200, 226, 240);")
        self.average_temperature.setObjectName("average_temperature")

        self.average_temperature.clicked.connect(self.Avg_temp)
        
        self.cloud_cover = QtWidgets.QPushButton(self.Fuzzy_system)
        self.cloud_cover.setGeometry(QtCore.QRect(500, 270, 161, 26))
        self.cloud_cover.setStyleSheet("color:rgb(200, 226, 240);\n"
"font: 75 11pt \"Moon\";")
        self.cloud_cover.setObjectName("cloud_cover")

        self.cloud_cover.clicked.connect(self.DarkSky)
        
        self.temp = QtWidgets.QLabel(self.Fuzzy_system)
        self.temp.setGeometry(QtCore.QRect(662, 180, 131, 61))
        self.temp.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(233, 99, 94);")
        self.temp.setObjectName("temp")

        self.temp.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.eco_level = QtWidgets.QLabel(self.Fuzzy_system)
        self.eco_level.setGeometry(QtCore.QRect(640, 380, 61, 71))
        self.eco_level.setStyleSheet("font: 40pt \"Big John\";\n"
"color:rgb(238, 247, 251);")
        self.eco_level.setObjectName("eco_level")
        self.cc = QtWidgets.QLabel(self.Fuzzy_system)
        self.cc.setGeometry(QtCore.QRect(662, 250, 131, 61))
        self.cc.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(233, 99, 94);")
        self.cc.setObjectName("cc")

        self.cc.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.refresh_current = QtWidgets.QToolButton(self.Fuzzy_system)
        self.refresh_current.setGeometry(QtCore.QRect(610, 330, 88, 31))
        self.refresh_current.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color: rgb(34, 139, 34)")
        self.refresh_current.setObjectName("refresh_current")

        self.refresh_current.clicked.connect(self.loading2)

        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(1000 * 3600)
        self.timer4.timeout.connect(self.Update_Current)
        self.timer4.start()
        
        self.refresh_current_2 = QtWidgets.QToolButton(self.Fuzzy_system)
        self.refresh_current_2.setGeometry(QtCore.QRect(150, 300, 88, 31))
        self.refresh_current_2.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color: rgb(34, 139, 34)")
        self.refresh_current_2.setObjectName("refresh_current_2")

        self.refresh_current_2.clicked.connect(self.loading1)
        
        self.title_1.raise_()
        self.time_hours.raise_()
        self.time_min.raise_()
        self.date.raise_()
        self.run_system.raise_()
        self.avg_temp.raise_()
        self.avg_cc.raise_()
        self.avg_batt.raise_()
        self.defuzz.raise_()
        self.average_temperature.raise_()
        self.temp_icon.raise_()
        self.average_cloud_cover.raise_()
        self.cloud_icon.raise_()
        self.battery_percent.raise_()
        self.batt_icon.raise_()
        self.cloud_cover.raise_()
        self.temp.raise_()
        self.defuzzification.raise_()
        self.economy_level.raise_()
        self.eco_level.raise_()
        self.temperature.raise_()
        self.cc.raise_()
        self.refresh_current.raise_()
        self.refresh_current_2.raise_()
        system.addItem(self.Fuzzy_system, "")
        self.Room_Conditions = QtWidgets.QWidget()
        self.Room_Conditions.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.Room_Conditions.setObjectName("Room_Conditions")
        self.title_2 = QtWidgets.QLabel(self.Room_Conditions)
        self.title_2.setGeometry(QtCore.QRect(130, -20, 521, 85))
        self.title_2.setStyleSheet("font: 36pt \"Peace Sans\";\n"
"color: rgb(233, 84, 32);")
        self.title_2.setObjectName("title_2")
        self.room_temp = QtWidgets.QLabel(self.Room_Conditions)
        self.room_temp.setGeometry(QtCore.QRect(2, 90, 131, 61))
        self.room_temp.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(238, 247, 251);")
        self.room_temp.setObjectName("room_temp")

        self.room_temp.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.room_humidity = QtWidgets.QPushButton(self.Room_Conditions)
        self.room_humidity.setGeometry(QtCore.QRect(490, 110, 161, 26))
        self.room_humidity.setStyleSheet("color:rgb(233, 99, 94);\n"
"font: 75 11pt \"Moon\";")
        self.room_humidity.setObjectName("room_humidity")

        self.room_humidity.clicked.connect(self.Room_hum)
        
        self.room_humidity_2 = QtWidgets.QLabel(self.Room_Conditions)
        self.room_humidity_2.setGeometry(QtCore.QRect(660, 90, 131, 61))
        self.room_humidity_2.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(238, 247, 251);")
        self.room_humidity_2.setObjectName("room_humidity_2")

        self.room_humidity_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.room_temperature = QtWidgets.QPushButton(self.Room_Conditions)
        self.room_temperature.setGeometry(QtCore.QRect(140, 110, 161, 26))
        self.room_temperature.setStyleSheet("color:rgb(233, 99, 94);\n"
"font: 75 11pt \"Moon\";")
        self.room_temperature.setObjectName("room_temperature")

        self.room_temperature.clicked.connect(self.Room_temp)
        
        self.heater_on = QtWidgets.QLabel(self.Room_Conditions)
        self.heater_on.setGeometry(QtCore.QRect(230, 310, 61, 61))
        self.heater_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.heater_on.setObjectName("heater_on")
        self.cooler_on = QtWidgets.QLabel(self.Room_Conditions)
        self.cooler_on.setGeometry(QtCore.QRect(230, 380, 61, 61))
        self.cooler_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.cooler_on.setObjectName("cooler_on")
        self.heater_off = QtWidgets.QLabel(self.Room_Conditions)
        self.heater_off.setGeometry(QtCore.QRect(300, 310, 61, 61))
        self.heater_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);\n"
"")
        self.heater_off.setObjectName("heater_off")
        self.cooler_off = QtWidgets.QLabel(self.Room_Conditions)
        self.cooler_off.setGeometry(QtCore.QRect(300, 380, 61, 61))
        self.cooler_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);")
        self.cooler_off.setObjectName("cooler_off")
        self.heater = QtWidgets.QLabel(self.Room_Conditions)
        self.heater.setGeometry(QtCore.QRect(150, 330, 71, 31))
        self.heater.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color:rgb(85, 85, 255);")
        self.heater.setObjectName("heater")
        self.cooler = QtWidgets.QLabel(self.Room_Conditions)
        self.cooler.setGeometry(QtCore.QRect(150, 400, 71, 31))
        self.cooler.setStyleSheet("color:rgb(85, 85, 255);\n"
"font: 11pt \"Peace Sans\";")
        self.cooler.setObjectName("cooler")
        self.dehumid_on = QtWidgets.QLabel(self.Room_Conditions)
        self.dehumid_on.setGeometry(QtCore.QRect(490, 380, 61, 61))
        self.dehumid_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.dehumid_on.setObjectName("dehumid_on")
        self.humid_off = QtWidgets.QLabel(self.Room_Conditions)
        self.humid_off.setGeometry(QtCore.QRect(420, 310, 61, 61))
        self.humid_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);")
        self.humid_off.setObjectName("humid_off")
        self.humid_on = QtWidgets.QLabel(self.Room_Conditions)
        self.humid_on.setGeometry(QtCore.QRect(490, 310, 61, 61))
        self.humid_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.humid_on.setObjectName("humid_on")
        self.dehumid_off = QtWidgets.QLabel(self.Room_Conditions)
        self.dehumid_off.setGeometry(QtCore.QRect(420, 380, 61, 61))
        self.dehumid_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);")
        self.dehumid_off.setObjectName("dehumid_off")
        self.humidifier = QtWidgets.QLabel(self.Room_Conditions)
        self.humidifier.setGeometry(QtCore.QRect(560, 330, 101, 31))
        self.humidifier.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color:rgb(85, 85, 255);")
        self.humidifier.setObjectName("humidifier")
        self.dehumidifier = QtWidgets.QLabel(self.Room_Conditions)
        self.dehumidifier.setGeometry(QtCore.QRect(560, 400, 121, 31))
        self.dehumidifier.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color:rgb(85, 85, 255);")
        self.dehumidifier.setObjectName("dehumidifier")
        self.running = QtWidgets.QLabel(self.Room_Conditions)
        self.running.setGeometry(QtCore.QRect(230, 170, 331, 41))
        self.running.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 14pt \"Big John\";")
        self.running.setObjectName("running")
        self.run_eco_level = QtWidgets.QLabel(self.Room_Conditions)
        self.run_eco_level.setGeometry(QtCore.QRect(350, 220, 81, 61))
        self.run_eco_level.setStyleSheet("font: 40pt \"Big John\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.run_eco_level.setObjectName("run_eco_level")
        self.run_eco_level.setText("--")

        self.run_eco_level.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.open_ubidots = QtWidgets.QPushButton(self.Room_Conditions)
        self.open_ubidots.setGeometry(QtCore.QRect(230, 460, 361, 51))
        self.open_ubidots.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Big John\";")
        self.open_ubidots.setObjectName("open_ubidots")

        self.open_ubidots.clicked.connect(self.Open_ubidots)
        
        system.addItem(self.Room_Conditions, "")

        self.retranslateUi(system)
        system.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(system)

    def retranslateUi(self, system):
        _translate = QtCore.QCoreApplication.translate
        system.setWindowTitle(_translate("system", "ToolBox"))
        self.title_1.setText(_translate("system", "SYSTEM VARIABLES"))
        self.time_hours.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.run_system.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">COMPUTE ECONOMY LEVEL</span></p></body></html>"))
        self.run_system.setText(_translate("system", "RUN SYSTEM"))
        self.avg_temp.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.temp_icon.setText(_translate("system", "<html><head/><body><p><img src=\":/icons/Icons/thermometer.png\"/></p></body></html>"))
        self.avg_cc.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.avg_batt.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.battery_percent.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420;\">VIEW PLOT</span></p></body></html>"))
        self.battery_percent.setText(_translate("system", "BATTERY PERCENTAGE"))
        self.batt_icon.setText(_translate("system", "<html><head/><body><p><img src=\":/icons/Icons/battery.png\"/></p></body></html>"))
        self.cloud_icon.setText(_translate("system", "<html><head/><body><p><img src=\":/icons/Icons/cloudy.png\"/></p></body></html>"))
        self.average_cloud_cover.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420;\">VIEW PLOT</span></p></body></html>"))
        self.average_cloud_cover.setText(_translate("system", "AVERAGE CLOUD COVER"))
        self.defuzz.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.defuzzification.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">COMPUTE VALUE</span></p></body></html>"))
        self.defuzzification.setText(_translate("system", "DEFUZZIFICATION"))
        self.economy_level.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">OPEN LOG DATA</span></p></body></html>"))
        self.economy_level.setText(_translate("system", "ECONOMY LEVEL"))
        self.temperature.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420;\">WEATHER FORECAST</span></p></body></html>"))
        self.temperature.setText(_translate("system", "TEMPERATURE"))
        self.average_temperature.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420; border:none;\">VIEW PLOT</span></p></body></html>"))
        self.average_temperature.setText(_translate("system", "AVERAGE TEMPERATURE"))
        self.cloud_cover.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420;\">WEATHER FORECAST</span></p></body></html>"))
        self.cloud_cover.setText(_translate("system", "CLOUD COVER"))
        self.temp.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.eco_level.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.cc.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.refresh_current.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">REFRESH DATA</span></p></body></html>"))
        self.refresh_current.setText(_translate("system", "REFRESH"))
        self.refresh_current_2.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">REFRESH DATA</span></p></body></html>"))
        self.refresh_current_2.setText(_translate("system", "REFRESH"))
        system.setItemText(system.indexOf(self.Fuzzy_system), _translate("system", "Page 1"))
        self.title_2.setText(_translate("system", "ROOM CONDITIONS"))
        self.room_temp.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.room_humidity.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420;\">VIEW PLOT</span></p></body></html>"))
        self.room_humidity.setText(_translate("system", "HUMIDITY"))
        self.room_humidity_2.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.room_temperature.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600; color:#e95420;\">VIEW PLOT</span></p></body></html>"))
        self.room_temperature.setText(_translate("system", "TEMPERATURE"))
        self.heater_on.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.cooler_on.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.heater_off.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.cooler_off.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.heater.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">HEATER STATUS</span></p></body></html>"))
        self.heater.setText(_translate("system", "<html><head/><body><p align=\"right\">HEATER</p></body></html>"))
        self.cooler.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">COOLER STATUS</span></p></body></html>"))
        self.cooler.setText(_translate("system", "<html><head/><body><p align=\"right\">COOLER</p></body></html>"))
        self.dehumid_on.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.humid_off.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.humid_on.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.dehumid_off.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.humidifier.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">HUMIDIFIER STATUS</span></p></body></html>"))
        self.humidifier.setText(_translate("system", "HUMIDIFIER"))
        self.dehumidifier.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">DEHUMIDIFIER STATUS</span></p></body></html>"))
        self.dehumidifier.setText(_translate("system", "DEHUMIDIFIER"))
        self.running.setText(_translate("system", "<html><head/><body><p align=\"center\">RUNNING IN ECONOMY LEVEL</p></body></html>"))
        self.run_eco_level.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">VIEW PLOT</span></p></body></html>"))
        self.run_eco_level.setText(_translate("system", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.open_ubidots.setToolTip(_translate("system", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Moon\'; font-size:9pt; font-weight:600; color:#e95420;\">OPEN IN WEB BROWSER</span></p></body></html>"))
        self.open_ubidots.setText(_translate("system", "OPEN UBIDOTS"))
        system.setItemText(system.indexOf(self.Room_Conditions), _translate("system", "Page 2"))
        
    def Time(self):
        self.time_hours.setText(QtCore.QTime.currentTime().toString("h"))
        self.time_min.setText(QtCore.QTime.currentTime().toString("mm"))

    def Date(self):
        self.date.setText(QtCore.QDate.currentDate().toString("ddd, MMM d"))
        
    def loading1(self):
        
        self.done1 = False
        movie = QMovie("Icons/loading.gif")
        splash = MovieSplashScreen(movie)
        splash.setMask(splash.mask())
        splash.show()

        test1 = Thread(target = self.Update_Average).start()

        while not self.done1:
            app.processEvents()
               
        splash.finish(system)

    def Update_Average(self):
        
        f = open('Ubidots_APIkey.txt', 'r')
        apikey = f.readline().strip()
        f.close()
        api = ApiClient(token = apikey)

        try:
            temp = api.get_variable("58d76383762542260cf36d8f")
            cloud_cover = api.get_variable("58d76394762542260a851a05")
            batt = api.get_variable("58d763aa762542260cf36f24")
        except ValueError:
            print('Unable to obtain variable')

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

        self.t = round(tempc / 48, 2)
        self.c = round(clouds / 48, 2)
        self.b = 10
        try:
            temp.save_value({'value': self.t})
            cloud_cover.save_value({'value': self.c})
            batt.save_value({'value': self.b})
            time.sleep(1)
        except:
            print('Value not sent')
        
        self.avg_temp.setText('{:0.01f}°'.format(self.t))
        self.avg_cc.setText('{}%'.format(int(self.c*100)))
        self.avg_batt.setText('{}%'.format(self.b))
        
        self.done1 = True

    def loading2(self):
        
        self.done2 = False
        movie = QMovie("Icons/loading.gif")
        splash = MovieSplashScreen(movie)
        splash.setMask(splash.mask())
        splash.show()

        test = Thread(target = self.Update_Current).start()

        while not self.done2:
            app.processEvents()
               
        splash.finish(system)

        
    def Update_Current(self):
        f = open('DS_APIkey.txt','r')
        apikey = f.read()
        f.close()

        Bangalore = [12.9716, 77.5946]

        fio = ForecastIO.ForecastIO(apikey,
                                    units=ForecastIO.ForecastIO.UNITS_SI,
                                    lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                    latitude=Bangalore[0], longitude=Bangalore[1],
                                    )
        if fio.has_currently() is True:
            currently = FIOCurrently.FIOCurrently(fio)
            self.temp.setText('{:0.01f}°'.format(currently.temperature))
            self.cc.setText('{}%'.format(int(currently.cloudCover * 100)))
        else:
            print('No Currently data')

        self.done2 = True
   
    def Update_Battery(self):
        f = open('Ubidots_APIkey.txt', 'r')
        apikey = f.readline().strip()
        f.close()
        api = ApiClient(token = apikey)

        try:
            batt = api.get_variable("58d763aa762542260cf36f24")
        except ValueError:
            print('Value Error')
            
        battery = 40
        
        try:
            batt.save_value({'value': battery})
            time.sleep(1)
        except:
            print('Unable to connect to Ubidots batt')
        
        self.avg_batt.setText('{}%'.format(battery))

    def DarkSky(self):
        webbrowser.open('https://darksky.net', new = 2)

    def Batt_Percent(self):
        webbrowser.open('https://app.ubidots.com/ubi/getchart/page/R2kbUV5P5DSJVlXdTfMOXflxNtM', new = 2)

    def Avg_CC(self):
        webbrowser.open('https://app.ubidots.com/ubi/getchart/page/0f62Hh2lV0PMO8-p_X7DYFyNnd4', new = 2)

    def Avg_temp(self):
        webbrowser.open('https://app.ubidots.com/ubi/getchart/page/DlD6wC0uiipZzD3nbBT_Xty6myk', new = 2)

    def Defuzz(self):
        # New Antecedent/Consequent objects hold universe variables and membership
        # functions
        batt_percent = ctrl.Antecedent(np.arange(0, 100, 1), 'Battery_percentage')
        temp = ctrl.Antecedent(np.arange(15, 30, 1), 'Temperature')
        cloud_cover = ctrl.Antecedent(np.arange(0, 1, 0.01), 'Cloud_cover')
        eco_level = ctrl.Consequent(np.arange(1, 4, 0.01), 'Economy_level')

        # Battery membership function population
        batt_percent['Low_battery'] = fuzz.trapmf(batt_percent.universe, [0, 0, 20, 30])
        batt_percent['Medium_battery'] = fuzz.trapmf(batt_percent.universe, [20, 25, 75, 80])
        batt_percent['High_battery'] = fuzz.trapmf(batt_percent.universe, [75, 80, 100, 100])

        # Temperature membership function population
        temp['Low_temperature'] = fuzz.trapmf(temp.universe, [0, 0, 18, 20])
        temp['Medium_temperature'] = fuzz.trapmf(temp.universe, [18, 20, 24, 26])
        temp['High_temperature'] = fuzz.trapmf(temp.universe, [24 , 26, 30, 30])

        # Cloud_cover membership function population
        cloud_cover['Minimum_clouds'] = fuzz.trapmf(cloud_cover.universe, [0, 0, 0.20, 0.25])
        cloud_cover['Medium_clouds'] = fuzz.trapmf(cloud_cover.universe, [0.20, 0.25, 0.65, 0.70])
        cloud_cover['High_clouds'] = fuzz.trapmf(cloud_cover.universe, [0.65, 0.70, 1, 1])

        # Custom membership functions can be built interactively with a familiar,
        # Pythonic API
        eco_level['Critical'] = fuzz.trimf(eco_level.universe, [0, 1.0, 2.0])
        eco_level['Alert'] = fuzz.trimf(eco_level.universe, [1.75, 2.25, 2.75])
        eco_level['Normal'] = fuzz.trimf(eco_level.universe, [2.5, 3.0, 3.5])
        eco_level['Economyless'] = fuzz.trimf(eco_level.universe, [3.25, 4.0, 5.0])

        # Rules
        rule1 = ctrl.Rule(batt_percent['Low_battery'] &
                          (~temp['High_temperature']),
                          eco_level['Critical'])
        rule2 = ctrl.Rule(batt_percent['Low_battery'] &
                          temp['High_temperature'] &
                          cloud_cover['High_clouds'],
                          eco_level['Critical'])
        rule3 = ctrl.Rule(batt_percent['Low_battery'] &
                          temp['High_temperature'] &
                          (~cloud_cover['High_clouds']),
                          eco_level['Alert'])
        rule4 = ctrl.Rule(batt_percent['Medium_battery'] &
                          temp['Low_temperature'] &
                          (~cloud_cover['High_clouds']),
                          eco_level['Alert'])
        rule5 = ctrl.Rule(batt_percent['Medium_battery'] &
                          temp['Low_temperature'] &
                          cloud_cover['High_clouds'],
                          eco_level['Critical'])
        rule6 = ctrl.Rule(batt_percent['Medium_battery'] &
                          (~temp['Low_temperature']) &
                          (~cloud_cover['High_clouds']),
                          eco_level['Normal'])
        rule7 = ctrl.Rule(batt_percent['Medium_battery'] &
                          (~temp['Low_temperature']) &
                          cloud_cover['High_clouds'],
                          eco_level['Alert'])
        rule8 = ctrl.Rule(batt_percent['High_battery'] &
                          temp['Low_temperature'] &
                          (~cloud_cover['High_clouds']),
                          eco_level['Normal'])
        rule9 = ctrl.Rule(batt_percent['High_battery'] &
                          temp['Low_temperature'] &
                          cloud_cover['High_clouds'],
                          eco_level['Alert'])
        rule10 = ctrl.Rule(batt_percent['High_battery'] &
                          (~temp['Low_temperature']) &
                          (~cloud_cover['High_clouds']),
                          eco_level['Economyless'])
        rule11 = ctrl.Rule(batt_percent['High_battery'] &
                          (~temp['Low_temperature']) &
                          cloud_cover['High_clouds'],
                          eco_level['Normal'])

        eco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4,
                                           rule5, rule6, rule7, rule8,
                                           rule9, rule10, rule11])

        eco_mode = ctrl.ControlSystemSimulation(eco_ctrl)

        # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
        # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
        
        eco_mode.input['Temperature'] = self.t
        eco_mode.input['Cloud_cover'] = self.c
        eco_mode.input['Battery_percentage'] = self.b

        # Crunch the numbers
        eco_mode.compute()

        defuzz = eco_mode.output['Economy_level']

        self.defuzz.setText(format(defuzz,'.2f'))
        self.eco = int(defuzz + 0.5)

    def Eco(self):
        if (self.eco < 1):
            self.eco = 1 
            self.eco_level.setNum(self.eco)
            self.run_eco_level.setNum(self.eco)
            filename1 = datetime.datetime.now().strftime("%Y.%m.%d_%H:%M")
            save_path = 'Logs/'
            complete_path = os.path.join(save_path, filename1+'.log')
            f = open(complete_path, 'w')
            if (self.t == 0) or (self.c == 0) or (self.b == 0):
                f.write('Data Unavailable, running in economy level 1')
            else:
                f.write('Average Temperature is: ' + str(self.t) + ' °C' + '\n')
                f.write('Average Cloud Cover is: ' + str(self.c) + ' %' + '\n')
                f.write('Battery level is: ' + str(self.b) + '%' + '\n')
                f.write('Economy Level is: ' + str(self.eco) + '\n')
                f.close()
                   
        else:
            self.eco_level.setNum(self.eco)
            self.run_eco_level.setNum(self.eco)
            filename1 = datetime.datetime.now().strftime("%Y.%m.%d_%H:%M")
            save_path = 'Logs/'
            complete_path = os.path.join(save_path, filename1+'.txt')
            f = open(complete_path, 'w')
            if (self.t == 0) or (self.c == 0) or (self.b == 0):
                f.write('Data Unavailable, running in economy level 1')
            else:
                f.write('Average Temperature is: ' + str(self.t) + ' °C' + '\n')
                f.write('Average Cloud Cover is: ' + str(self.c) + ' %' + '\n')
                f.write('Battery level is: ' + str(self.b) + ' % ' + '\n')
                f.write('Economy Level is: ' + str(self.eco) + '\n')
                f.close()
                                
    def Room_temp(self):
        f = open('Ubidots_APIkey.txt', 'r')
        apikey = f.readline().strip()
        f.close()
        api = ApiClient(token = apikey)

        try:
            roomtemp = api.get_variable("58d763b8762542260a851bd1")
        except ValueError:
            print('Unable to obtain variable')
            
        PORT = '/dev/ttyUSB0'
        BAUD_RATE = 9600
         
        # Open serial port
        ser = serial.Serial(PORT, BAUD_RATE)

        if ser.isOpen():
            ser.close()
        ser.open()
        ser.isOpen()
        ser.write('s'.encode())
        time.sleep(2)
        response = ser.readline().strip().decode()
        self.roomt = float(response[5:])

        try:
            roomtemp.save_value({'value': self.roomt})
            print('Value',roomt, 'sent')
            time.sleep(2)
        except:
            print('Value not sent')

        self.room_temp.setText(format(self.roomt,'.2f'))    
        webbrowser.open('https://app.ubidots.com/ubi/getchart/page/G284654CCK1E77kbBR7zmpBDNkw', new = 2)    

    def Room_hum(self):
        f = open('Ubidots_APIkey.txt', 'r')
        apikey = f.readline().strip()
        f.close()
        api = ApiClient(token = apikey)

        try:
            roomhumidity = api.get_variable("58d763c57625422609b8d088")
        except ValueError:
            print('Unable to obtain variable')
        
        PORT = '/dev/ttyUSB0'
        BAUD_RATE = 9600
         
        # Open serial port
        ser = serial.Serial(PORT, BAUD_RATE)
        
        if ser.isOpen():
            ser.close()
        ser.open()
        ser.isOpen()
        ser.write('s'.encode())
        time.sleep(2)
        response = ser.readline().strip().decode()
        self.roomh = float(response[:5])

        try:
            roomhumidity.save_value({'value': self.roomh})
            print('Value',self.roomh, 'sent')
            time.sleep(2)
        except:
            print('Value not sent')

        self.room_humidity_2.setText(format(self.roomh,'.2f'))
        webbrowser.open('https://app.ubidots.com/ubi/getchart/page/qgaJ95jUNq91E3aVxJsNo7NphbU', new = 2)    

    def Open_ubidots(self):
        webbrowser.open('https://app.ubidots.com/ubi/public/getdashboard/page/P8OAd8cR6dtoL6aO4AQ384euynE', new = 2)

    def Run_System(self):
        self.cooler_on.setText('')
        self.heater_on.setText('')
        self.humid_on.setText('')
        self.dehumid_on.setText('')
        self.cooler_off.setText('')
        self.heater_off.setText('')
        self.humid_off.setText('')
        self.dehumid_off.setText('')
        
        if (self.eco < 1):
            self.run_eco_level.setText('--')
        
        elif (self.eco == 1):
            t = self.roomt
            h = self.roomh
            
            if (t > 35):
                ser.write('c'.encode())
                self.cooler_on.setText('ON')
                self.heater_off.setText('OFF')
                
            if (t < 15):
                ser.write('f'.encode())
                self.heater_on.setText('ON')
                self.cooler_off.setText('OFF')
                
            if (h < 25):
                ser.write('h'.encode())
                self.humid_on.setText('ON')
                self.dehumid_off.setText('OFF')
                
            if (h > 80):
                ser.write('e'.encode())
                self.dehumid_on.setText('ON')
                self.humid_off.setText('OFF')

        elif (self.eco == 2):
            t = self.roomt
            h = self.roomh
            
            if (t > 32):
                ser.write('c'.encode())
                self.cooler_on.setText('ON')
                self.heater_off.setText('OFF')
                
            if (t < 18):
                ser.write('f'.encode())
                self.heater_on.setText('ON')
                self.cooler_off.setText('OFF')
                
            if (h < 30):
                ser.write('h'.encode())
                self.humid_on.setText('ON')
                self.dehumid_off.setText('OFF')
                
            if (h > 70):
                ser.write('e'.encode())
                self.dehumid_on.setText('ON')
                self.humid_off.setText('OFF')

        elif (self.eco == 3):
            t = self.roomt
            h = self.roomh
            
            if (t > 30):
                ser.write('c'.encode())
                self.cooler_on.setText('ON')
                self.heater_off.setText('OFF')
                
            if (t < 20):
                ser.write('f'.encode())
                self.heater_on.setText('ON')
                self.cooler_off.setText('OFF')
                
            if (h < 40):
                ser.write('h'.encode())
                self.humid_on.setText('ON')
                self.dehumid_off.setText('OFF')
                
            if (h > 60):
                ser.write('e'.encode())
                self.dehumid_on.setText('ON')
                self.humid_off.setText('OFF')
        

        elif (self.eco == 4):
            t = self.roomt
            h = self.roomh
            
            if (t > 27):
                ser.write('c'.encode())
                self.cooler_on.setText('ON')
                self.heater_off.setText('OFF')
                
            if (t < 22):
                ser.write('f'.encode())
                self.heater_on.setText('ON')
                self.cooler_off.setText('OFF')
                
            if (h < 25):
                ser.write('h'.encode())
                self.humid_on.setText('ON')
                self.dehumid_off.setText('OFF')
                
            if (h > 50):
                ser.write('e'.encode())
                self.dehumid_on.setText('ON')
                self.humid_off.setText('OFF')
            
            
import system_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    system = QtWidgets.QToolBox()
    ui = Ui_system()
    ui.setupUi(system)
    system.move(QApplication.desktop().screen().rect().center() - system.rect().center())
    system.show()
    sys.exit(app.exec_())
