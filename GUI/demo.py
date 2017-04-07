# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ToolBox(object):
    def setupUi(self, ToolBox):
        ToolBox.setObjectName("ToolBox")
        ToolBox.resize(349, 315)
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 349, 253))
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 99, 27))
        self.pushButton.setObjectName("pushButton")
        ToolBox.addItem(self.page, "")
        self.page1 = QtWidgets.QWidget()
        self.page1.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page1.setObjectName("page1")
        ToolBox.addItem(self.page1, "")

        self.retranslateUi(ToolBox)
        ToolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ToolBox)

    def retranslateUi(self, ToolBox):
        _translate = QtCore.QCoreApplication.translate
        ToolBox.setWindowTitle(_translate("ToolBox", "ToolBox"))
        self.pushButton.setText(_translate("ToolBox", "PushButton"))
        ToolBox.setItemText(ToolBox.indexOf(self.page), _translate("ToolBox", "Page 1"))
        ToolBox.setItemText(ToolBox.indexOf(self.page1), _translate("ToolBox", "Page 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolBox = QtWidgets.QToolBox()
    ui = Ui_ToolBox()
    ui.setupUi(ToolBox)
    ToolBox.show()
    sys.exit(app.exec_())

