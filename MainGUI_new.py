from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *
import sys
import threading
import time
from PyQt5.QtWidgets import QFrame

from StartGUI_new  import  Ui_MainWindow as StartGUI
from EnterPW_new import  Ui_MainWindow as EnterPWGUI
from UserSettingGUI_new import  Ui_MainWindow as UserSettingGUI
from enterNewPW_new import  Ui_MainWindow as enterNewPWGUI
from enterNewPW2_new import  Ui_MainWindow as enterNewPW2GUI
from VoiceEnrollGUI_new import  Ui_MainWindow as VoiceEnrollGUI
import pir
import suvomoter
import util
import threading
import cnn

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.PWstatus = 0 #0 is start, 1 is pwSetting
        self.inputNum=''
        self.checkNum=''
        self.startUI = StartGUI()
        self.pwEnterUI = EnterPWGUI()
        self.usersettingUI = UserSettingGUI()
        self.enternewPWUI = enterNewPWGUI()
        self.enternewPW2UI = enterNewPW2GUI()
        self.voiceEnroll = VoiceEnrollGUI()
        self.pirThread = pir.pir()
        self.pirThread.start()
        self.sv=suvomoter.suvomoter()
        
        self.start(1)

    def start(self,event):
        self.PWstatus = 0
        self.startUI.setupUi(self)
        self.startUI.pad_conf.mousePressEvent = self.usersetting
        self.startUI.pad_star.mousePressEvent = self.pwEnter
        self.show()

    def pwCheck(self,enterNum):
        pwFile = open('pw.txt','r')
        pw=pwFile.readline()
        pwFile.close()
        pw = pw[3:]
        self.inputNum = self.inputNum + '\n'
        print ('pw is ',pw)
        print ('input num is ',self.inputNum)

        if pw==self.inputNum:
            print ('PW Right!!')
            if (self.PWstatus == 0):
                # open the door
                self.start(1)
                QApplication.instance().processEvents()
                self.sv.open()
            elif self.PWstatus == 1:
                # go to recheck pw page
                self.changePW(1)

            elif (self.PWstatus == 2):
                # check PW to setting voice enroll
                self.voiceSetting()
        else:
            print ('PW Wrong!!')
            self.start(1)




    def pwEnter(self,event):

        self.inputNum=''
        self.pwEnterUI.setupUi(self)
        self.pwEnterUI.pad_conf.mousePressEvent = self.usersetting
        self.pwEnterUI.pad_star.mousePressEvent = self.pwCheck
        self.pwEnterUI.pad_1.mousePressEvent = self.num1Clicked
        self.pwEnterUI.pad_2.mousePressEvent = self.num2Clicked
        self.pwEnterUI.pad_3.mousePressEvent = self.num3Clicked
        self.pwEnterUI.pad_4.mousePressEvent = self.num4Clicked
        self.pwEnterUI.pad_5.mousePressEvent = self.num5Clicked
        self.pwEnterUI.pad_6.mousePressEvent = self.num6Clicked
        self.pwEnterUI.pad_7.mousePressEvent = self.num7Clicked
        self.pwEnterUI.pad_8.mousePressEvent = self.num8Clicked
        self.pwEnterUI.pad_9.mousePressEvent = self.num9Clicked
        self.pwEnterUI.pad_0.mousePressEvent = self.num0Clicked
        self.pwEnterUI.pad_sharp.mousePressEvent = self.numSharpClicked
        self.show()


    def usersetting(self,event):
        self.PWstatus = 1
        self.usersettingUI.setupUi(self)
        self.usersettingUI.back.mousePressEvent = self.start
        self.usersettingUI.password_title.mousePressEvent = self.pwEnter
        self.usersettingUI.voice_title.mousePressEvent = self.voiceSettingPWEnter

        self.show()

    def voiceSettingPWEnter(self,event):
        self.PWstatus = 2
        self.pwEnter(1)

    def voiceSetting(self):
        self.voiceEnroll.setupUi(self)
        self.voiceEnroll.back.mousePressEvent = self.start
        self.voiceEnroll.start.mousePressEvent = self.voiceRecord
        self.voiceEnroll.record.hide()
        self.show()

    def voiceRecord(self,event):
        #predict.enroll_account(chunk=1024, seconds=2)
        #t = nn.nn()
        #t.start()
        #self.voiceEnroll.setupUi(self)
        self.voiceEnroll.record.show()
        QApplication.instance().processEvents()
        #util.enroll_account(8196, 2)
        #np = cnn.CNN()
        #print np.nb_classes
        #t = threading.Thread(target=np.train)
        #t.start()
        time.sleep(60)
        #self.voiceEnroll.record.hide()
        QApplication.instance().processEvents()
        #self.show()
        
        
        self.start(1)


    def changePW(self,event):
        self.inputNum = ''
        self.enternewPWUI.setupUi(self)
        #self.enternewPWUI.label_back.mousePressEvent = self.start
        self.enternewPWUI.pad_star.mousePressEvent = self.changePW2
        self.enternewPWUI.pad_1.mousePressEvent = self.num1Clicked
        self.enternewPWUI.pad_2.mousePressEvent = self.num2Clicked
        self.enternewPWUI.pad_3.mousePressEvent = self.num3Clicked
        self.enternewPWUI.pad_4.mousePressEvent = self.num4Clicked
        self.enternewPWUI.pad_5.mousePressEvent = self.num5Clicked
        self.enternewPWUI.pad_6.mousePressEvent = self.num6Clicked
        self.enternewPWUI.pad_7.mousePressEvent = self.num7Clicked
        self.enternewPWUI.pad_8.mousePressEvent = self.num8Clicked
        self.enternewPWUI.pad_9.mousePressEvent = self.num9Clicked
        self.enternewPWUI.pad_0.mousePressEvent = self.num0Clicked
        self.enternewPWUI.pad_sharp.mousePressEvent = self.numSharpClicked
        self.show()

    def changePW2(self,event):
        self.checkNum = self.inputNum
        self.inputNum = ''
        self.enternewPW2UI.setupUi(self)
        #self.enternewPW2UI.label_back.mousePressEvent = self.start
        self.enternewPW2UI.pad_star.mousePressEvent = self.pwChange
        self.enternewPW2UI.pad_1.mousePressEvent = self.num1Clicked
        self.enternewPW2UI.pad_2.mousePressEvent = self.num2Clicked
        self.enternewPW2UI.pad_3.mousePressEvent = self.num3Clicked
        self.enternewPW2UI.pad_4.mousePressEvent = self.num4Clicked
        self.enternewPW2UI.pad_5.mousePressEvent = self.num5Clicked
        self.enternewPW2UI.pad_6.mousePressEvent = self.num6Clicked
        self.enternewPW2UI.pad_7.mousePressEvent = self.num7Clicked
        self.enternewPW2UI.pad_8.mousePressEvent = self.num8Clicked
        self.enternewPW2UI.pad_9.mousePressEvent = self.num9Clicked
        self.enternewPW2UI.pad_0.mousePressEvent = self.num0Clicked
        self.enternewPW2UI.pad_sharp.mousePressEvent = self.numSharpClicked
        self.show()



    def pwChange(self,event):
        if self.inputNum==self.checkNum:
            pwFile = open('pw.txt', 'w')
            self.newpw = 'PW:'+self.inputNum+'\n'
            pwFile.write(self.newpw)
            pwFile.close()
            self.start(1)
        else:
            self.changePW(1)



    def num1Clicked(self,event):
        self.inputNum = self.inputNum + '1'
        print (self.inputNum)
    def num2Clicked(self,event):
        self.inputNum = self.inputNum + '2'
        print (self.inputNum)
    def num3Clicked(self,event):
        self.inputNum = self.inputNum + '3'
        print (self.inputNum)
    def num4Clicked(self,event):
        self.inputNum = self.inputNum + '4'
        print (self.inputNum)
    def num5Clicked(self,event):
        self.inputNum = self.inputNum + '5'
        print (self.inputNum)
    def num6Clicked(self,event):
        self.inputNum = self.inputNum + '6'
        print (self.inputNum)
    def num7Clicked(self,event):
        self.inputNum = self.inputNum + '7'
        print (self.inputNum)
    def num8Clicked(self,event):
        self.inputNum = self.inputNum + '8'
        print (self.inputNum)
    def num9Clicked(self,event):
        self.inputNum = self.inputNum + '9'
        print (self.inputNum)
    def num0Clicked(self,event):
        self.inputNum = self.inputNum + '0'
        print (self.inputNum)
    def numSharpClicked(self,event):
        self.inputNum = self.inputNum + '#'
        print (self.inputNum)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())