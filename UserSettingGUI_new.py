# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 1024)
        MainWindow.setStyleSheet("QWidget#MainWindow {background-image: url(back.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(20, 20, 560, 1004))
        self.verticalWidget.setStyleSheet("background-image: url(:/background/grid.png);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.padding_1 = QtWidgets.QLabel(self.verticalWidget)
        self.padding_1.setStyleSheet("")
        self.padding_1.setObjectName("padding_1")
        self.verticalLayout_4.addWidget(self.padding_1)
        self.padding_3 = QtWidgets.QLabel(self.verticalWidget)
        self.padding_3.setText("")
        self.padding_3.setObjectName("padding_3")
        self.verticalLayout_4.addWidget(self.padding_3)
        self.password_title = QtWidgets.QLabel(self.verticalWidget)
        self.password_title.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.password_title.setObjectName("password_title")
        self.verticalLayout_4.addWidget(self.password_title)
        self.padding_2 = QtWidgets.QLabel(self.verticalWidget)
        self.padding_2.setText("")
        self.padding_2.setObjectName("padding_2")
        self.verticalLayout_4.addWidget(self.padding_2)
        self.voice_title = QtWidgets.QLabel(self.verticalWidget)
        self.voice_title.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.voice_title.setObjectName("voice_title")
        self.verticalLayout_4.addWidget(self.voice_title)
        self.padding_4 = QtWidgets.QLabel(self.verticalWidget)
        self.padding_4.setText("")
        self.padding_4.setObjectName("padding_4")
        self.verticalLayout_4.addWidget(self.padding_4)
        self.padding_5 = QtWidgets.QLabel(self.verticalWidget)
        self.padding_5.setText("")
        self.padding_5.setObjectName("padding_5")
        self.verticalLayout_4.addWidget(self.padding_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.padding_6 = QtWidgets.QLabel(self.verticalWidget)
        self.padding_6.setStyleSheet("")
        self.padding_6.setText("")
        self.padding_6.setObjectName("padding_6")
        self.horizontalLayout.addWidget(self.padding_6)
        self.back = QtWidgets.QLabel(self.verticalWidget)
        self.back.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.back.setObjectName("back")
        self.horizontalLayout.addWidget(self.back)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.padding_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.password_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">비밀번호 설정</span></p></body></html>"))
        self.voice_title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">소리 설정</span></p></body></html>"))
        self.back.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">뒤로</span></p></body></html>"))

#import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

