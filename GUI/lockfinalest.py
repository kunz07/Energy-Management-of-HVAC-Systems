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
        self.username = QtWidgets.QLabel(UserText)
        self.username.setGeometry(QtCore.QRect(85, 260, 77, 17))
        self.username.setStyleSheet("color: rgb(233, 84, 32);")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(UserText)
        self.password.setGeometry(QtCore.QRect(85, 300, 73, 17))
        self.password.setStyleSheet("color: rgb(233, 84, 32);")
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(UserText)
        self.login.setGeometry(QtCore.QRect(155, 350, 75, 27))
        self.login.setStyleSheet("color: rgb(255, 255, 255);")
        self.login.setObjectName("login")

        self.login.clicked.connect(self.Login)
        
        self.time = QtWidgets.QLabel(UserText)
        self.time.setGeometry(QtCore.QRect(300, 100, 91, 31))
        self.time.setStyleSheet("font: 75 22pt \"NanumGothic\";\n"
"color: rgb(119, 33, 111);")
        self.time.setObjectName("time")
        self.time.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(1000)
        self.timer1.timeout.connect(self.Time)
        self.timer1.start()
        
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
        font.setFamily("Waree")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.fuzzysystem.setFont(font)
        self.fuzzysystem.setStyleSheet("font: 75 22pt \"Waree\";")
        self.fuzzysystem.setObjectName("fuzzysystem")
        self.date = QtWidgets.QLabel(UserText)
        self.date.setGeometry(QtCore.QRect(260, 150, 131, 21))
        self.date.setStyleSheet("font: 25 12pt \"Ubuntu\";\n"
"color: rgb(174, 167, 159);")
        self.date.setText("")
        self.date.setObjectName("date")
        self.date.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(1000)
        self.timer2.timeout.connect(self.Date)
        self.timer2.start()
        
        self.usertext = QtWidgets.QLineEdit(UserText)
        self.usertext.setGeometry(QtCore.QRect(165, 260, 140, 19))
        self.usertext.setStyleSheet("background-color: rgb(44, 0, 30);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"border: none")
        self.usertext.setPlaceholderText("Enter Username")
        self.usertext.setObjectName("usertext")

        self.usertext.setMaxLength(10)
        
        self.passtext = QtWidgets.QLineEdit(UserText)
        self.passtext.setGeometry(QtCore.QRect(165, 300, 140, 19))
        self.passtext.setStyleSheet("background-color: rgb(44, 0, 30);\n"
"border: none")
        self.passtext.setPlaceholderText("Enter Password")
        self.passtext.setObjectName("passtext")

        self.passtext.setMaxLength(10)
        self.passtext.setEchoMode(2)
        
        self.message = QtWidgets.QLineEdit(UserText)
        self.message.setGeometry(QtCore.QRect(80, 320, 221, 27))
        self.message.setStyleSheet("border : none\n"
"")
        self.message.setObjectName("message")
        
        self.message.setAlignment(QtCore.Qt.AlignHCenter)

        self.retranslateUi(UserText)
        QtCore.QMetaObject.connectSlotsByName(UserText)

    def retranslateUi(self, UserText):
        _translate = QtCore.QCoreApplication.translate
        UserText.setWindowTitle(_translate("UserText", "Dialog"))
        self.username.setText(_translate("UserText", "Username :"))
        self.password.setText(_translate("UserText", "Password :"))
        self.login.setText(_translate("UserText", "Login"))
        self.time.setText(_translate("UserText", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.fuzzysystem.setText(_translate("UserText", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#e95420;\">FUZZY SYSTEM</span></p></body></html>"))
        self.usertext.setToolTip(_translate("UserText", "<html><head/><body><p><br/></p></body></html>"))

    def Time(self):
        self.time.setText(QtCore.QTime.currentTime().toString("hh:mm"))

    def Date(self):
        self.date.setText(QtCore.QDate.currentDate().toString())
        
    def Login(self):
        username = self.usertext.text()
        password = self.passtext.text()
        allow = ['kunal', 'kamran', 'vidya']
        if(username.lower() == "fyp2017" and password.lower() in allow):
            self.message.setText("Access Granted")
        else:
            self.message.setText("Wrong Password! Try Again")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserText = QtWidgets.QDialog()
    ui = Ui_UserText()
    ui.setupUi(UserText)
    UserText.show()
    sys.exit(app.exec_())

