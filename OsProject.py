#!/usr/bin/python3
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
'''
TODO
-- reset edit line for start time
-- reset edit line for need time
''' 
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "CPU Scheduling Algorithms Simulation"
        self.top = 100
        self.left = 1000
        self.width = 800
        self.height = 500

        self.flag = False
        self.firstTime= True

        self.numberOfProcess = 0
        self.timeForEachProcess = []
        self.startingTime = []
        self.nums = [] # Number on ruler
        self.processLabel = []
        self.processStartLineEdit = []
        self.processTimeLineEdit = []
        self.enterStart = QLabel(self)
        self.enterTime = QLabel(self)
        self.trueSequence = []
        self.trueBurstTime= []
        self.priority = []
        self.nop = 0 # Number of process

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.screenSize = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.setGeometry(0, 0, self.screenSize.width(), self.screenSize.height())
        #self.setGeometry(self.left, self.top, self.width, self.height)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        space = 30
        titleLabel = QLabel("CPU Scheduling Algorithms Simulation", self)
        titleLabel.move(50, space)
        algorithmsLabel = QLabel("Algorithms : ", self)
        algorithmsLabel.move(50, space+30)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("FCFS")
        self.comboBox.addItem("RR")
        self.comboBox.addItem("Three-level Queue Scheduling")
        self.comboBox.addItem("SRTN")
        self.comboBox.move (140, space+25)
        numberOfProcessLabel = QLabel("Number of Process (1-10)", self)
        numberOfProcessLabel.move(50, space+70)
        self.numberOfProcessET = QLineEdit(self)
        self.numberOfProcessET.move(225,space+65)
        simulateBtn = QPushButton("Simulate",self)
        simulateBtn.move(50, space+100)
        simulateBtn.clicked.connect(self.SimulateClicked)
        self.runBtn = QPushButton("Run", self)
        self.runBtn.move(50, 220)
        self.runBtn.resize(0,0)
        self.hideStuff()

        self.show()

    def SimulateClicked(self):
        self.flag = False 
        print("flag: ",self.flag)
        if not self.firstTime:
            for i in range(self.nop):
                self.processStartLineEdit[i].setText("")
                self.processTimeLineEdit[i].setText("")
            
            self.clearStuff()

        self.update()

        self.nop = self.numberOfProcessET.text()
        if self.nop == "": self.nop = 0
        self.nop = int(self.nop)
        self.enterStart.setText("Enter process value for start time :  ")
        self.enterStart.adjustSize()
        self.enterStart.move(50, 160)

        self.enterTime.setText("Enter burst time :  ")
        self.enterTime.adjustSize()
        self.enterTime.move(50, 190)
        
        # Display start time and time
        j = 260
        for i in range(self.nop):
            self.processStartLineEdit[i].resize(24,24)
            self.processTimeLineEdit[i].resize(24,24)

        self.runBtn.resize(80,24)
        self.runBtn.clicked.connect(self.Run)

    def Run(self):
        self.nop = self.numberOfProcessET.text()
        if self.nop == "": self.nop = 0
        self.nop = int(self.nop)
        for i in range(self.nop):
            a = int(self.processStartLineEdit[i].text())
            b = int(self.processTimeLineEdit[i].text())
            self.startingTime.append(a)
            self.timeForEachProcess.append(b)

        if self.comboBox.currentText()=="FCFS":
            print("FCFS")
            self.FCFS()
        elif self.comboBox.currentText()=="RR":
            print("RR")
            self.RR()
        elif self.comboBox.currentText()=="TLQS":
            print("TLQS")
            self.TLQS()
        else:
            print("SRTN")
            self.SRTN()
        self.flag = True
        self.update()


    def paintEvent(self, event):
        if self.flag:
            color = [(255, 64, 0), (255, 128, 0), (255, 191, 0),
                    (255, 255, 0), (128, 255, 0), (0, 255, 191),
                    (0, 191, 255), (0, 128, 255), (128, 0, 255), (255, 0, 255)]
            painter = QPainter(self)
            painter.begin(self)
            painter.setPen(QPen(Qt.white, -1, Qt.SolidLine))

            letsMovetogether = 100
            # Color bars
            tailPos = 50
            j = 0
            for i in self.trueSequence:
                r = color[j][0]
                g = color[j][1]
                b = color[j][2]
                painter.setBrush(QColor(r, g, b))
                painter.drawRect(tailPos, (200+letsMovetogether), i*30, 30)

                # Process label
                p = "P" + str(self.trueBurstTime[j])
                self.processLabel[j].setText(p)
                midBar = tailPos+((i*30)/2)
                self.processLabel[j].move(midBar-7, 207+letsMovetogether)
                self.processLabel[j].adjustSize()
                tailPos += i*30
                j += 1


            # Ruler
            rulerPos = 50
            sumTime = sum(self.timeForEachProcess)
            for i in range(sumTime+1):
                painter.setBrush(QColor(0,0,0))
                painter.drawRect(rulerPos, 235+letsMovetogether, 1, 15)
                self.nums[i].setText(str(i))
                self.nums[i].move(rulerPos-3, 250+letsMovetogether)
                self.nums[i].adjustSize()
                rulerPos += 30

            painter.drawRect(50, 242.5+letsMovetogether, sumTime*30, 1)
            self.firstTime = False
            painter.end()

        else:
            painter = QPainter(self)
            painter.begin(self)
            painter.setPen(QPen(Qt.white, -1, Qt.SolidLine))
            painter.drawRect(0, 300, self.screenSize.width(), 900)
            for j in range(len(self.trueSequence)):
                # Process label
                p = ""
                self.processLabel[j].setText(p)

            sumTime = sum(self.timeForEachProcess)
            for i in range(sumTime+1):
                self.nums[i].setText("")

            painter.end()


    def FCFS(self):
        a = list(set(self.startingTime))
        
        for i in a:
            for j in range(self.nop):
                if self.startingTime[j] == i:
                    self.trueSequence.append(self.timeForEachProcess[j])
                    self.trueBurstTime.append(j)

    def RR(self):
        pass
    
    def TLQS(self):
        pass

    def SRTN(self):
        pass

    def hideStuff(self):
        j = 280
        # LineEdit for starting time each process
        for i in range(10):
            self.st = QLineEdit(self)
            self.st.resize(0, 0)
            self.st.move(j, 155)
            self.processStartLineEdit.append(self.st)

            self.t = QLineEdit(self)
            self.t.resize(0, 0)
            self.t.move(j, 185)
            j += 30
            self.processTimeLineEdit.append(self.t)
            
        # Number for ruler
        for i in range(100):
            self.num = QLabel("", self)
            self.nums.append(self.num)

        # Label for each process
        for i in range(10):
            self.pro = QLabel("",self)
            self.processLabel.append(self.pro)

    def clearStuff(self):
        for i,j,k,l in zip(self.processStartLineEdit,self.processTimeLineEdit,self.nums,self.processLabel,):
            i.resize(0,0)
            j.resize(0,0)
            l.setText("")
        
        for k in self.nums:
            k.setText("")


        self.trueBurstTime.clear()
        self.trueSequence.clear()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
