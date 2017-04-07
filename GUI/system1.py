# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'system.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_system(object):
    def setupUi(self, system):
        system.setObjectName("system")
        system.resize(800, 600)
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
        self.time_hours.setGeometry(QtCore.QRect(576, 60, 121, 135))
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
        self.avg_temp = QtWidgets.QLabel(self.Fuzzy_system)
        self.avg_temp.setGeometry(QtCore.QRect(0, 100, 121, 51))
        self.avg_temp.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgbrgb(85, 85, 255);")
        self.avg_temp.setObjectName("avg_temp")
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
        self.avg_batt = QtWidgets.QLabel(self.Fuzzy_system)
        self.avg_batt.setGeometry(QtCore.QRect(0, 240, 121, 51))
        self.avg_batt.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(85, 85, 255);")
        self.avg_batt.setObjectName("avg_batt")
        self.battery_percent = QtWidgets.QPushButton(self.Fuzzy_system)
        self.battery_percent.setGeometry(QtCore.QRect(120, 250, 221, 32))
        self.battery_percent.setStyleSheet("font: 75 11pt \"Moon\";\n"
"color: rgb(200, 226, 240);")
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
        self.economy_level = QtWidgets.QPushButton(self.Fuzzy_system)
        self.economy_level.setGeometry(QtCore.QRect(450, 400, 179, 32))
        self.economy_level.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color: rgb(34, 139, 34)")
        self.economy_level.setObjectName("economy_level")
        self.temperature = QtWidgets.QPushButton(self.Fuzzy_system)
        self.temperature.setGeometry(QtCore.QRect(500, 230, 161, 26))
        self.temperature.setStyleSheet("color:rgb(200, 226, 240);\n"
"font: 75 11pt \"Moon\";")
        self.temperature.setObjectName("temperature")
        self.average_temperature = QtWidgets.QPushButton(self.Fuzzy_system)
        self.average_temperature.setGeometry(QtCore.QRect(120, 110, 221, 32))
        self.average_temperature.setStyleSheet("font: 75 11pt \"Moon\";\n"
"color: rgb(200, 226, 240);")
        self.average_temperature.setObjectName("average_temperature")
        self.cloud_cover = QtWidgets.QPushButton(self.Fuzzy_system)
        self.cloud_cover.setGeometry(QtCore.QRect(500, 300, 161, 26))
        self.cloud_cover.setStyleSheet("color:rgb(200, 226, 240);\n"
"font: 75 11pt \"Moon\";")
        self.cloud_cover.setObjectName("cloud_cover")
        self.temp = QtWidgets.QLabel(self.Fuzzy_system)
        self.temp.setGeometry(QtCore.QRect(662, 210, 131, 61))
        self.temp.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(233, 99, 94);")
        self.temp.setObjectName("temp")
        self.eco_level = QtWidgets.QLabel(self.Fuzzy_system)
        self.eco_level.setGeometry(QtCore.QRect(640, 380, 61, 71))
        self.eco_level.setStyleSheet("font: 40pt \"Big John\";\n"
"color:rgb(238, 247, 251);")
        self.eco_level.setObjectName("eco_level")
        self.cc = QtWidgets.QLabel(self.Fuzzy_system)
        self.cc.setGeometry(QtCore.QRect(662, 280, 131, 61))
        self.cc.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(233, 99, 94);")
        self.cc.setObjectName("cc")
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
        system.addItem(self.Fuzzy_system, "")
        self.Room_Conditions = QtWidgets.QWidget()
        self.Room_Conditions.setGeometry(QtCore.QRect(0, 0, 800, 538))
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
        self.room_humidity = QtWidgets.QPushButton(self.Room_Conditions)
        self.room_humidity.setGeometry(QtCore.QRect(490, 110, 161, 26))
        self.room_humidity.setStyleSheet("color:rgb(233, 99, 94);\n"
"font: 75 11pt \"Moon\";")
        self.room_humidity.setObjectName("room_humidity")
        self.room_humidity_2 = QtWidgets.QLabel(self.Room_Conditions)
        self.room_humidity_2.setGeometry(QtCore.QRect(660, 90, 131, 61))
        self.room_humidity_2.setStyleSheet("font: 75 32pt \"Moon\";\n"
"color:rgb(238, 247, 251);")
        self.room_humidity_2.setObjectName("room_humidity_2")
        self.room_temperature = QtWidgets.QPushButton(self.Room_Conditions)
        self.room_temperature.setGeometry(QtCore.QRect(140, 110, 161, 26))
        self.room_temperature.setStyleSheet("color:rgb(233, 99, 94);\n"
"font: 75 11pt \"Moon\";")
        self.room_temperature.setObjectName("room_temperature")
        self.heater_on = QtWidgets.QLabel(self.Room_Conditions)
        self.heater_on.setGeometry(QtCore.QRect(230, 340, 61, 61))
        self.heater_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.heater_on.setObjectName("heater_on")
        self.cooler_on = QtWidgets.QLabel(self.Room_Conditions)
        self.cooler_on.setGeometry(QtCore.QRect(230, 410, 61, 61))
        self.cooler_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.cooler_on.setObjectName("cooler_on")
        self.heater_off = QtWidgets.QLabel(self.Room_Conditions)
        self.heater_off.setGeometry(QtCore.QRect(300, 340, 61, 61))
        self.heater_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);\n"
"")
        self.heater_off.setObjectName("heater_off")
        self.cooler_off = QtWidgets.QLabel(self.Room_Conditions)
        self.cooler_off.setGeometry(QtCore.QRect(300, 410, 61, 61))
        self.cooler_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);")
        self.cooler_off.setObjectName("cooler_off")
        self.heater = QtWidgets.QLabel(self.Room_Conditions)
        self.heater.setGeometry(QtCore.QRect(90, 360, 131, 31))
        self.heater.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color:rgb(85, 85, 255);")
        self.heater.setObjectName("heater")
        self.cooler = QtWidgets.QLabel(self.Room_Conditions)
        self.cooler.setGeometry(QtCore.QRect(90, 430, 131, 31))
        self.cooler.setStyleSheet("color:rgb(85, 85, 255);\n"
"font: 11pt \"Peace Sans\";")
        self.cooler.setObjectName("cooler")
        self.dehumid_on = QtWidgets.QLabel(self.Room_Conditions)
        self.dehumid_on.setGeometry(QtCore.QRect(490, 410, 61, 61))
        self.dehumid_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.dehumid_on.setObjectName("dehumid_on")
        self.humid_off = QtWidgets.QLabel(self.Room_Conditions)
        self.humid_off.setGeometry(QtCore.QRect(420, 340, 61, 61))
        self.humid_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);")
        self.humid_off.setObjectName("humid_off")
        self.humid_on = QtWidgets.QLabel(self.Room_Conditions)
        self.humid_on.setGeometry(QtCore.QRect(490, 340, 61, 61))
        self.humid_on.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(0, 255, 0);")
        self.humid_on.setObjectName("humid_on")
        self.dehumid_off = QtWidgets.QLabel(self.Room_Conditions)
        self.dehumid_off.setGeometry(QtCore.QRect(420, 410, 61, 61))
        self.dehumid_off.setStyleSheet("font: 75 26pt \"Moon\";\n"
"color: rgb(255, 0, 0);")
        self.dehumid_off.setObjectName("dehumid_off")
        self.humidifier = QtWidgets.QLabel(self.Room_Conditions)
        self.humidifier.setGeometry(QtCore.QRect(560, 360, 121, 31))
        self.humidifier.setStyleSheet("font: 11pt \"Peace Sans\";\n"
"color:rgb(85, 85, 255);")
        self.humidifier.setObjectName("humidifier")
        self.dehumidifier = QtWidgets.QLabel(self.Room_Conditions)
        self.dehumidifier.setGeometry(QtCore.QRect(560, 430, 121, 31))
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
        system.addItem(self.Room_Conditions, "")

        self.retranslateUi(system)
        system.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(system)

    def retranslateUi(self, system):
        _translate = QtCore.QCoreApplication.translate
        system.setWindowTitle(_translate("system", "ToolBox"))
        self.title_1.setText(_translate("system", "SYSTEM VARIABLES"))
        self.time_hours.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.run_system.setText(_translate("system", "RUN SYSTEM"))
        self.avg_temp.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.temp_icon.setText(_translate("system", "<html><head/><body><p><img src=\":/icons/Icons/thermometer.png\"/></p></body></html>"))
        self.avg_cc.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.avg_batt.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.battery_percent.setText(_translate("system", "BATTERY PERCENTAGE"))
        self.batt_icon.setText(_translate("system", "<html><head/><body><p><img src=\":/icons/Icons/battery.png\"/></p></body></html>"))
        self.cloud_icon.setText(_translate("system", "<html><head/><body><p><img src=\":/icons/Icons/cloudy.png\"/></p></body></html>"))
        self.average_cloud_cover.setText(_translate("system", "AVERAGE CLOUD COVER"))
        self.defuzz.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.defuzzification.setText(_translate("system", "DEFUZZIFICATION"))
        self.economy_level.setText(_translate("system", "ECONOMY LEVEL"))
        self.temperature.setText(_translate("system", "TEMPERATURE"))
        self.average_temperature.setText(_translate("system", "AVERAGE TEMPERATURE"))
        self.cloud_cover.setText(_translate("system", "CLOUD COVER"))
        self.temp.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.eco_level.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.cc.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        system.setItemText(system.indexOf(self.Fuzzy_system), _translate("system", "Page 1"))
        self.title_2.setText(_translate("system", "ROOM CONDITIONS"))
        self.room_temp.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.room_humidity.setText(_translate("system", "HUMIDITY"))
        self.room_humidity_2.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.room_temperature.setText(_translate("system", "TEMPERATURE"))
        self.heater_on.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.cooler_on.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.heater_off.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.cooler_off.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.heater.setText(_translate("system", "<html><head/><body><p align=\"right\">HEATER</p></body></html>"))
        self.cooler.setText(_translate("system", "<html><head/><body><p align=\"right\">COOLER</p></body></html>"))
        self.dehumid_on.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.humid_off.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.humid_on.setText(_translate("system", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.dehumid_off.setText(_translate("system", "<html><head/><body><p><br/></p></body></html>"))
        self.humidifier.setText(_translate("system", "HUMIDIFIER"))
        self.dehumidifier.setText(_translate("system", "DEHUMIDIFIER"))
        self.running.setText(_translate("system", "<html><head/><body><p align=\"center\">RUNNING IN ECONOMY LEVEL</p></body></html>"))
        self.run_eco_level.setText(_translate("system", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        system.setItemText(system.indexOf(self.Room_Conditions), _translate("system", "Page 2"))

    def Time(self):
        self.time_hours.setText(QtCore.QTime.currentTime().toString("h"))
        self.time_min.setText(QtCore.QTime.currentTime().toString("mm"))

    def Date(self):
        self.date.setText(QtCore.QDate.currentDate().toString("ddd, MMM d"))
        
import system_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    system = QtWidgets.QToolBox()
    ui = Ui_system()
    ui.setupUi(system)
    system.show()
    sys.exit(app.exec_())

