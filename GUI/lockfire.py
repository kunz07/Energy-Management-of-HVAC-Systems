# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lockscreen.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserText(object):
    def setupUi(self, UserText):
        UserText.setObjectName("UserText")
        UserText.resize(400, 388)
        UserText.setStyleSheet("background-color: rgb(44, 0, 30);")
        self.login = QtWidgets.QPushButton(UserText)
        self.login.setGeometry(QtCore.QRect(179, 350, 75, 27))
        self.login.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Big John\";")
        self.login.setObjectName("login")
        self.line = QtWidgets.QFrame(UserText)
        self.line.setGeometry(QtCore.QRect(250, 140, 140, 3))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background-color: rgb(174, 167, 159);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fuzzysystem = QtWidgets.QLabel(UserText)
        self.fuzzysystem.setGeometry(QtCore.QRect(40, 10, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Peace Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fuzzysystem.setFont(font)
        self.fuzzysystem.setStyleSheet("font: 22pt \"Peace Sans\";")
        self.fuzzysystem.setObjectName("fuzzysystem")
        self.message = QtWidgets.QLabel(UserText)
        self.message.setGeometry(QtCore.QRect(100, 320, 221, 20))
        self.message.setStyleSheet("font: 10pt \"Ubuntu Mono\";\n"
"color: rgb(255, 0, 0);")
        self.message.setObjectName("message")
        self.widget = QtWidgets.QWidget(UserText)
        self.widget.setGeometry(QtCore.QRect(239, 150, 151, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.date = QtWidgets.QLabel(self.widget)
        self.date.setStyleSheet("font: 12pt \"Ubuntu\";\n"
"color: rgb(174, 167, 159);")
        self.date.setText("")
        self.date.setObjectName("date")
        self.horizontalLayout.addWidget(self.date)
        self.widget1 = QtWidgets.QWidget(UserText)
        self.widget1.setGeometry(QtCore.QRect(280, 100, 111, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.time = QtWidgets.QLabel(self.widget1)
        self.time.setStyleSheet("font: 20pt \"Ubuntu\";\n"
"color: rgb(119, 33, 111);")
        self.time.setObjectName("time")
        self.horizontalLayout_2.addWidget(self.time)
        self.widget2 = QtWidgets.QWidget(UserText)
        self.widget2.setGeometry(QtCore.QRect(70, 250, 273, 34))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.username = QtWidgets.QLabel(self.widget2)
        self.username.setStyleSheet("color: rgb(233, 84, 32);\n"
"font: 75 11pt \"Moon\";")
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.usertext = QtWidgets.QLineEdit(self.widget2)
        self.usertext.setStyleSheet("background-color: rgb(44, 0, 30);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"border: none")
        self.usertext.setText("")
        self.usertext.setObjectName("usertext")
        self.horizontalLayout_3.addWidget(self.usertext)
        self.widget3 = QtWidgets.QWidget(UserText)
        self.widget3.setGeometry(QtCore.QRect(70, 290, 278, 34))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.password = QtWidgets.QLabel(self.widget3)
        self.password.setStyleSheet("color: rgb(233, 84, 32);\n"
"font: 25 11pt \"Moon\";")
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.passtext = QtWidgets.QLineEdit(self.widget3)
        self.passtext.setStyleSheet("background-color: rgb(44, 0, 30);\n"
"border: none")
        self.passtext.setText("")
        self.passtext.setObjectName("passtext")
        self.horizontalLayout_4.addWidget(self.passtext)

        self.retranslateUi(UserText)
        QtCore.QMetaObject.connectSlotsByName(UserText)

    def retranslateUi(self, UserText):
        _translate = QtCore.QCoreApplication.translate
        UserText.setWindowTitle(_translate("UserText", "Dialog"))
        self.login.setText(_translate("UserText", "Login"))
        self.fuzzysystem.setText(_translate("UserText", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#e95420;\">FUZZY SYSTEM</span></p></body></html>"))
        self.message.setText(_translate("UserText", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/calendar.png\"/></p></body></html>"))
        self.label_3.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/clock.png\"/></p></body></html>"))
        self.time.setText(_translate("UserText", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.label_4.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/user.png\"/></p></body></html>"))
        self.username.setText(_translate("UserText", "Username :"))
        self.usertext.setToolTip(_translate("UserText", "<html><head/><body><p><br/></p></body></html>"))
        self.label_5.setText(_translate("UserText", "<html><head/><body><p><img src=\":/icons/Icons/door-key.png\"/></p></body></html>"))
        self.password.setText(_translate("UserText", "Password :"))

import lockscreen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserText = QtWidgets.QDialog()
    ui = Ui_UserText()
    ui.setupUi(UserText)
    UserText.show()
    sys.exit(app.exec_())

