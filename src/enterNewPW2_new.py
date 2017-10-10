# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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


        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setEnabled(True)
        self.gridWidget.setGeometry(QtCore.QRect(20, 20, 560, 1004))
        #self.gridWidget.setStyleSheet("background-image: url(:/background/grid.png);")
        self.gridWidget.setStyleSheet("QWidget#self.gridWidget {background-image: url(grid.png);}")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pad_star = QtWidgets.QLabel(self.gridWidget)
        self.pad_star.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_star.setObjectName("pad_star")
        self.gridLayout.addWidget(self.pad_star, 5, 0, 1, 1)
        self.pad_9 = QtWidgets.QLabel(self.gridWidget)
        self.pad_9.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_9.setObjectName("pad_9")
        self.gridLayout.addWidget(self.pad_9, 4, 2, 1, 1)
        self.pad_sharp = QtWidgets.QLabel(self.gridWidget)
        self.pad_sharp.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_sharp.setObjectName("pad_sharp")
        self.gridLayout.addWidget(self.pad_sharp, 5, 2, 1, 1)
        self.pad_3 = QtWidgets.QLabel(self.gridWidget)
        self.pad_3.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_3.setObjectName("pad_3")
        self.gridLayout.addWidget(self.pad_3, 2, 2, 1, 1)
        self.pad_5 = QtWidgets.QLabel(self.gridWidget)
        self.pad_5.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_5.setObjectName("pad_5")
        self.gridLayout.addWidget(self.pad_5, 3, 1, 1, 1)
        self.pad_2 = QtWidgets.QLabel(self.gridWidget)
        self.pad_2.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_2.setObjectName("pad_2")
        self.gridLayout.addWidget(self.pad_2, 2, 1, 1, 1)
        self.pad_7 = QtWidgets.QLabel(self.gridWidget)
        self.pad_7.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_7.setObjectName("pad_7")
        self.gridLayout.addWidget(self.pad_7, 4, 0, 1, 1)
        self.pad_1 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.pad_1.setFont(font)
        self.pad_1.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_1.setObjectName("pad_1")
        self.gridLayout.addWidget(self.pad_1, 2, 0, 1, 1)
        self.pad_4 = QtWidgets.QLabel(self.gridWidget)
        self.pad_4.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_4.setObjectName("pad_4")
        self.gridLayout.addWidget(self.pad_4, 3, 0, 1, 1)
        self.pad_6 = QtWidgets.QLabel(self.gridWidget)
        self.pad_6.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_6.setObjectName("pad_6")
        self.gridLayout.addWidget(self.pad_6, 3, 2, 1, 1)
        self.pad_8 = QtWidgets.QLabel(self.gridWidget)
        self.pad_8.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_8.setObjectName("pad_8")
        self.gridLayout.addWidget(self.pad_8, 4, 1, 1, 1)
        self.pad_0 = QtWidgets.QLabel(self.gridWidget)
        self.pad_0.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_0.setObjectName("pad_0")
        self.gridLayout.addWidget(self.pad_0, 5, 1, 1, 1)
        self.pad_conf = QtWidgets.QLabel(self.gridWidget)
        self.pad_conf.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_conf.setObjectName("pad_conf")
        self.gridLayout.addWidget(self.pad_conf, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.more = QtWidgets.QLabel(self.gridWidget)
        self.more.setStyleSheet("border-style: solid;\n"
                                "border-color: rgb(255, 255, 255);\n"
                                "border-width: 10px;")
        self.more.setObjectName("more")
        self.gridLayout.addWidget(self.more, 6, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pad_star.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">*</span></p></body></html>"))
        self.pad_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">9</span></p></body></html>"))
        self.pad_sharp.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">#</span></p></body></html>"))
        self.pad_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">3</span></p></body></html>"))
        self.pad_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">5</span></p></body></html>"))
        self.pad_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">2</span></p></body></html>"))
        self.pad_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">7</span></p></body></html>"))
        self.pad_1.setText(_translate("MainWindow", "<html>\n"
"<head/>\n"
"<body>\n"
"<p align=\"center\" >\n"
"<span style=\" font-size:72pt; color:#ffffff; \">1</span>\n"
"</p>\n"
"</body>\n"
"</html>"))
        self.pad_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">4</span></p></body></html>"))
        self.pad_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">6</span></p></body></html>"))
        self.pad_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">8</span></p></body></html>"))
        self.pad_0.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">0</span></p></body></html>"))
        self.pad_conf.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">설정</span></p></body></html>"))
        self.more.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">한번 더</span></p><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">입력해주세요</span></p></body></html>"))


#import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

