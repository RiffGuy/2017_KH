# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
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
        self.gridWidget.setStyleSheet("background-image: url(:/background/grid.png);")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pad_star = QtWidgets.QLabel(self.gridWidget)
        self.pad_star.setStyleSheet("border-style: solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-width: 10px;")
        self.pad_star.setObjectName("pad_star")
        self.gridLayout.addWidget(self.pad_star, 5, 0, 1, 1)

        self.recog = QtWidgets.QLabel(self.gridWidget)
        self.recog.setStyleSheet("")
        self.recog.setObjectName("recog")
        self.gridLayout.addWidget(self.recog, 3, 1, 1, 1)
        self.recog.hide()

        self.padding_9 = QtWidgets.QLabel(self.gridWidget)
        self.padding_9.setStyleSheet("")
        self.padding_9.setObjectName("padding_9")
        self.gridLayout.addWidget(self.padding_9, 4, 2, 1, 1)
        self.padding_11 = QtWidgets.QLabel(self.gridWidget)
        self.padding_11.setStyleSheet("")
        self.padding_11.setObjectName("padding_11")
        self.gridLayout.addWidget(self.padding_11, 5, 2, 1, 1)
        self.padding_3 = QtWidgets.QLabel(self.gridWidget)
        self.padding_3.setStyleSheet("")
        self.padding_3.setObjectName("padding_3")
        self.gridLayout.addWidget(self.padding_3, 2, 2, 1, 1)
        self.padding_5 = QtWidgets.QLabel(self.gridWidget)
        self.padding_5.setStyleSheet("")
        self.padding_5.setObjectName("padding_5")
        self.gridLayout.addWidget(self.padding_5, 3, 1, 1, 1)
        self.padding_2 = QtWidgets.QLabel(self.gridWidget)
        self.padding_2.setStyleSheet("")
        self.padding_2.setObjectName("padding_2")
        self.gridLayout.addWidget(self.padding_2, 2, 1, 1, 1)
        self.padding_7 = QtWidgets.QLabel(self.gridWidget)
        self.padding_7.setStyleSheet("")
        self.padding_7.setObjectName("padding_7")
        self.gridLayout.addWidget(self.padding_7, 4, 0, 1, 1)
        self.padding_1 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.padding_1.setFont(font)
        self.padding_1.setStyleSheet("")
        self.padding_1.setObjectName("padding_1")
        self.gridLayout.addWidget(self.padding_1, 2, 0, 1, 1)
        self.padding_4 = QtWidgets.QLabel(self.gridWidget)
        self.padding_4.setStyleSheet("")
        self.padding_4.setObjectName("padding_4")
        self.gridLayout.addWidget(self.padding_4, 3, 0, 1, 1)
        self.padding_6 = QtWidgets.QLabel(self.gridWidget)
        self.padding_6.setStyleSheet("")
        self.padding_6.setObjectName("padding_6")
        self.gridLayout.addWidget(self.padding_6, 3, 2, 1, 1)
        self.padding_8 = QtWidgets.QLabel(self.gridWidget)
        self.padding_8.setStyleSheet("")
        self.padding_8.setObjectName("padding_8")
        self.gridLayout.addWidget(self.padding_8, 4, 1, 1, 1)
        self.padding_10 = QtWidgets.QLabel(self.gridWidget)
        self.padding_10.setStyleSheet("")
        self.padding_10.setObjectName("padding_10")
        self.gridLayout.addWidget(self.padding_10, 5, 1, 1, 1)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pad_star.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">*</span></p></body></html>"))
        self.padding_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.padding_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pad_conf.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">설정</span></p></body></html>"))
        self.recog.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\"> speak your voice</span></p></body></html>"))

#import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

