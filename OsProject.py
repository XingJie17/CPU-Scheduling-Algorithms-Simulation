#!/usr/bin/python3
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

'''
TODO
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

        self.numberOfProcess = 0
        self.timeForEachProcess = []
        self.startingTime = []
        self.nums = [] # Number on ruler
        self.processLabel = []
        self.processStartLineEdit = []
        self.processTimeLineEdit = []
        self.priorityLineEdit = []
        self.enterStart = QLabel(self)
        self.enterTime = QLabel(self)
        self.enterPriority = QLabel(self)
        self.trueSequence = []
        self.trueBurstTime= []
        self.priority = []
        self.nop = 0 # Number of process
        self.count = 0
        self.simulateClicked = False # Prevent run from running by itself :(

        self.gc1 = [] # For TLQS
        self.gc2 = [] # For TLQS
        self.gc3 = [] # For TLQS

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
        self.comboBox.addItem("TLQS")
        self.comboBox.addItem("SRTN")
        self.comboBox.move (140, space+25)
        numberOfProcessLabel = QLabel("Number of Process (3-10)", self)
        numberOfProcessLabel.move(50, space+70)
        self.numberOfProcessET = QLineEdit(self)
        self.numberOfProcessET.move(225,space+65)


        simulateBtn = QPushButton("Simulate",self)
        simulateBtn.move(50, space+100)
        simulateBtn.clicked.connect(self.SimulateClicked)
        self.runBtn = QPushButton("Run", self)
        self.runBtn.move(50, 280)
        self.runBtn.resize(0,0)
        self.quantumLbl = QLabel("Quantum : ",self)
        self.quantumLbl.move(999,9999)
        self.quantumLE = QLineEdit(self)
        self.quantumLE.move(280, 245)
        self.quantumLE.resize(0,0)
        self.hideStuff()

        self.show()

        #self.SimulateClicked()

    def SimulateClicked(self):
        try:
            self.flag = False
            self.simulateClicked = True
            self.nop = self.numberOfProcessET.text()
            self.nop = int(self.nop)
            if self.nop < 3 or self.nop > 10:
                QMessageBox.question(self, 'ERROR', "Invalid process number", QMessageBox.Ok)

            else:
                for i in range(self.nop):
                    self.processStartLineEdit[i].setText("")
                    self.processTimeLineEdit[i].setText("")
                    self.priorityLineEdit[i].setText("")
                #for i in range(10):
                    #self.processStartLineEdit[i].setText("1")
                    #self.priorityLineEdit[i].setText("1")

                #self.processTimeLineEdit[0].setText("6")
                #self.processTimeLineEdit[1].setText("4")
                #self.processTimeLineEdit[2].setText("6")
                #self.processTimeLineEdit[3].setText("6")
                #self.processTimeLineEdit[4].setText("6")
                #self.processTimeLineEdit[5].setText("6")
                self.clearStuff()
                self.update()
     
                self.nop = self.numberOfProcessET.text()
                self.nop = int(self.nop)
                self.enterStart.setText("Enter process value for start time :  ")
                self.enterStart.adjustSize()
                self.enterStart.move(50, 160)
     
                self.enterTime.setText("Enter burst time :  ")
                self.enterTime.adjustSize()
                self.enterTime.move(50, 190)
     
                self.enterPriority.setText("Enter Priority :  ")
                self.enterPriority.adjustSize()
                self.enterPriority.move(50, 220)
     
                # Display start time and time
                for i in range(self.nop):
                    self.processStartLineEdit[i].resize(24,24)
                    self.processTimeLineEdit[i].resize(24,24)
                    self.priorityLineEdit[i].resize(24,24)
                
                if self.comboBox.currentText()=="TLQS" or self.comboBox.currentText()=="RR":
                    self.quantumLbl.move(50,250)
                    self.quantumLE.resize(24,24)
                        
                else:
                    self.quantumLbl.move(999,999)
                    self.quantumLE.resize(0,0)

     
                self.runBtn.resize(80,24)
                self.runBtn.clicked.connect(self.Run)

                #self.Run()

        except:
            QMessageBox.question(self, 'ERROR', "Invalid process number", QMessageBox.Ok)


    def Run(self):
        #if self.simulateClicked == True '''and self.count == 0''':
        #self.clearStuff()
        if self.simulateClicked == True:
            try:
                totalTime = 0
                findZero = 99
                for i in range(self.nop):
                    a = int(self.processStartLineEdit[i].text())
                    b = int(self.processTimeLineEdit[i].text())
                    c = int(self.priorityLineEdit[i].text())
                    if a == 0:
                        findZero = a
                    self.startingTime.append(a)
                    self.timeForEachProcess.append(b)
                    self.priority.append(c)
                    totalTime += b
                
                if findZero != 0:
                    QMessageBox.question(self, "ERROR", "Must have zero in startingTime",QMessageBox.Ok)
                    self.SimulateClicked()
                    return 0
    
                if totalTime > 60:
                    QMessageBox.question(self, 'ERROR', "Total time exceeds the limit", QMessageBox.Ok)
                    self.SimulateClicked()
                    return 0                
    
                else:
     
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
                        print("after SRTN")
                    self.flag = True
                    self.simulateClicked = False
                    self.count = 0
                    self.update()
            except:
                #self.simulateClicked = False
                print("exception>> simulatedClicked>> ", self.simulateClicked)
                self.timeForEachProcess.clear()
                #QMessageBox.question(self, 'ERROR', "Must enter all boxes", QMessageBox.Ok)

        else:
            #self.simulateClicked = True 
            print("else>> simulatedClicked>> ", self.simulateClicked)


    def paintEvent(self, event):
        if self.flag:

            #self.trueSequence = [0,2,3,0,1,4,5]
            #self.trueBurstTime = [5,6,6,1,4,6,6]
            
            color = [(255, 64, 0), (255, 128, 0), (255, 191, 0),
                    (255, 255, 0), (128, 255, 0), (0, 255, 191),
                    (0, 191, 255), (0, 128, 255), (128, 0, 255), (255, 0, 255)]
            painter = QPainter(self)
            painter.begin(self)
            painter.setPen(QPen(Qt.white, -1, Qt.SolidLine))

            letsMovetogether = 150
            mapColor = {}
            if self.comboBox.currentText()!="TLQS":
                uniqueTrueSequence = set(self.trueSequence)
                colorIndex = 0
                for i in uniqueTrueSequence:
                    mapColor[i] = colorIndex
                    colorIndex += 1
    
                # Color bars
                tailPos = 50
                j = 0
                for i,k in zip(self.trueBurstTime,self.trueSequence):
                    r = color[mapColor[k]][0]
                    g = color[mapColor[k]][1]
                    b = color[mapColor[k]][2]
                    painter.setBrush(QColor(r, g, b))
                    painter.drawRect(tailPos, (200+letsMovetogether), i*30, 30)
    
                    # Process label
                    p = "P" + str(self.trueSequence[j])
                    self.processLabel[j].setText(p)
                    midBar = tailPos+((i*30)/2)
                    self.processLabel[j].move(midBar-8, 207+letsMovetogether)
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
                    if i == 61:
                        break
    
                painter.drawRect(50, 242.5+letsMovetogether, sumTime*30, 1)
                painter.end()
            else:
                # ------------------------------ TLQS ---------------------------
                uniqueTrueSequence = []
                for i in self.gc1:
                    uniqueTrueSequence.append(i[0])
                for i in self.gc2:
                    uniqueTrueSequence.append(i[0])
                for i in self.gc3:
                    uniqueTrueSequence.append(i[0])
                uniqueTrueSequence = set(uniqueTrueSequence)
                colorIndex = 0
                for i in uniqueTrueSequence:
                    if i == -1:
                        pass
                    else:
                        mapColor[i] = colorIndex
                        colorIndex += 1
                
                # Color bars
                tailPos = 50
                j = 0
                k = 0
                # gc1
                for i in self.gc1:
                    if i[0] == -1:
                        r = 58
                        g = 58
                        b = 58

                    else:
                        r = color[mapColor[i[0]]][0]
                        g = color[mapColor[i[0]]][1]
                        b = color[mapColor[i[0]]][2]
                    painter.setBrush(QColor(r, g, b))
                    painter.drawRect(tailPos, (200+letsMovetogether), i[1]*30, 30)
    
                    # Process label
                    if i[0] == -1:
                        p = ""
                    else:
                        p = "P" + str(i[0])
                    self.processLabel[j].setText(p)
                    midBar = tailPos+((i[1]*30)/2)
                    self.processLabel[j].move(midBar-8, 207+letsMovetogether)
                    self.processLabel[j].adjustSize()
                    tailPos += i[1]*30
                    print(j,self.processLabel[j].text(),self.processLabel[j].pos(),(midBar))
                    j += 1
                    #for i in self.processLabel:
                        #print("processLbl >> ",i.text()) 

    
                print()
                # Ruler
                rulerPos = 50
                sumTime = sum(self.timeForEachProcess)
                for i in range(sumTime+1):
                    painter.setBrush(QColor(0,0,0))
                    painter.drawRect(rulerPos, 235+letsMovetogether, 1, 15)
                    self.nums[k].setText(str(i))
                    self.nums[k].move(rulerPos-3, 250+letsMovetogether)
                    self.nums[k].adjustSize()
                    k += 1
                    rulerPos += 30
                    if i == 61:
                        break
    
                painter.drawRect(50, 242.5+letsMovetogether, sumTime*30, 1)

                letsMovetogether += 100
                # gc 2
                tailPos = 50
                for i in self.gc2:
                    if (i[0]) == -1:
                        r = 58
                        g = 58
                        b = 58

                    else:
                        r = color[mapColor[i[0]]][0]
                        g = color[mapColor[i[0]]][1]
                        b = color[mapColor[i[0]]][2]
                    painter.setBrush(QColor(r, g, b))
                    painter.drawRect(tailPos, (200+letsMovetogether), i[1]*30, 30)
    
                    # Process label
                    if i[0] == -1:
                        p = ""
                    else:
                        p = "P" + str(i[0])
                    self.processLabel[j].setText(p)
                    midBar = tailPos+((i[1]*30)/2)
                    self.processLabel[j].move(midBar-8, 207+letsMovetogether)
                    self.processLabel[j].adjustSize()
                    tailPos += i[1]*30
                    print(j,self.processLabel[j].text(),self.processLabel[j],(midBar))
                    j += 1
    
                print()
                # Ruler
                rulerPos = 50
                sumTime = sum(self.timeForEachProcess)
                for i in range(sumTime+1):
                    painter.setBrush(QColor(0,0,0))
                    painter.drawRect(rulerPos, 235+letsMovetogether, 1, 15)
                    self.nums[k].setText(str(i))
                    self.nums[k].move(rulerPos-3, 250+letsMovetogether)
                    self.nums[k].adjustSize()
                    k += 1
                    rulerPos += 30
                    if i == 61:
                        break
    
                painter.drawRect(50, 242.5+letsMovetogether, sumTime*30, 1)

                letsMovetogether += 100
                # gc 3
                tailPos = 50
                for i in self.gc3:
                    if (i[0]) == -1:
                        r = 58
                        g = 58
                        b = 58

                    else:
                        r = color[mapColor[i[0]]][0]
                        g = color[mapColor[i[0]]][1]
                        b = color[mapColor[i[0]]][2]
                    painter.setBrush(QColor(r, g, b))
                    painter.drawRect(tailPos, (200+letsMovetogether), i[1]*30, 30)
    
                    # Process label
                    if i[0] == -1:
                        p = ""
                    else:
                        p = "P" + str(i[0])
                    self.processLabel[j].setText(p)
                    midBar = tailPos+((i[1]*30)/2)
                    self.processLabel[j].move(midBar-8, 207+letsMovetogether)
                    self.processLabel[j].adjustSize()
                    tailPos += i[1]*30
                    print(j,self.processLabel[j].text(),self.processLabel[j],(midBar))
                    j += 1
    
                print()
                # Ruler
                rulerPos = 50
                sumTime = sum(self.timeForEachProcess)
                for i in range(sumTime+1):
                    painter.setBrush(QColor(0,0,0))
                    painter.drawRect(rulerPos, 235+letsMovetogether, 1, 15)
                    self.nums[k].setText(str(i))
                    self.nums[k].move(rulerPos-3, 250+letsMovetogether)
                    self.nums[k].adjustSize()
                    k += 1
                    rulerPos += 30
                    if i == 61:
                        break
    
                painter.drawRect(50, 242.5+letsMovetogether, sumTime*30, 1)
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
        # FCFS for q2
        # find first process
        print("\n")
        print("---------- Q2 ---------")
        print()
        #q2 = {0: [6, 0, 3], 1: [4, 1, 3], 2: [6, 5, 1], 3: [6, 6, 1], 4: [6, 7, 5], 5: [6, 8, 6]}
        # process: burstTime, arrival, priority 
        q2 = {}
        for i in range(self.nop):
           q2[i] = [self.timeForEachProcess[i],self.startingTime[i],self.priority[i]] 

        print("q2: ",q2)

        totalTimeQ2 = 0
        for i in q2:
            totalTimeQ2 += q2[i][0]
        
        aa = totalTimeQ2
        minA = 99
        minP = 99
        for i in q2:
            if q2[i][1] <= minA:
                minA = q2[i][1]
                if q2[i][2] <= minP:
                    minP = q2[i][2]
                    current = i
    
        #print(q2[current])
        timeLine = q2[current][1]
        aa += timeLine
        #print("timeLine >> ",timeLine)
        ganttChart2 = []
        tempBurstTime = 0
        mcp = 6 # Max current priority
        mcpIndex = 99
        oldCurrent = 99
        startTimeLine = timeLine
        while timeLine < aa:
            tempBurstTime += 1
            a = ((current,startTimeLine, tempBurstTime))
            #print("oldCurrent >> ",oldCurrent, " current >> ",current)
            if current == oldCurrent:
                ganttChart2[len(ganttChart2)-1] = a
            else:
                ganttChart2.append(a)
            oldCurrent = current
            #totalTimeQ1 -= tempBurstTime
            q2[current][0] -= 1
            timeLine += 1
            #print(current,"burstTime of q >> ",q2[current][0])
            found = False
            for i in q2:
                if q2[i][1] == timeLine and q2[i][2] < mcp:
                    found = True
                    mcp = q2[i][2]
                    mcpIndex = i
            
            if not found:
                mcp = q2[current][2]
                mcpIndex = current 
    
            #print("mcp >> ",mcp)
            #print("mcpIndex >> ",mcpIndex)
            #print("current priority >> ",q2[current][2])
    
            if(q2[current][0] == 0):
                tempList = []
                #print("Q2 >> ",q2)
                
                for i in q2:
                    #print("another process >> ",i,q2[i])
                    if q2[i][1]<=timeLine and q2[i][0] != 0:
                        #print("---------- break point ----------")
                        tempList.append(i)
                    
                # Create list for priority
                tempPri = []
                for i in tempList:
                    tempPri.append(q2[i][2])
    
                if(len(tempPri) == 0): break
                # Find highest priority
                x = min(tempPri)
    
                # Count how many highest priority
                dupl = tempPri.count(x)
                #print("dup >> ",dupl)
    
                # if only 1, set current to it
                if dupl == 1:
                    for i in tempList:
                        if q2[i][2] == x:
                            current = i
                            break
                else:
                    # Create list for arrival time
                    tempArr = []
                    for i in tempList:
                        if q2[i][2] == x:
                            tempArr.append(q2[i][1])
    
                    # Find who comes first
                    y = min(tempArr)
                    #print("who come first >> ",y)
                    # set current to it
                    for i in tempList:
                        if q2[i][1] == y:
                            current = i
                            break
                    
                startTimeLine = timeLine
                tempBurstTime = 0
                
            elif q2[current][2] > mcp:
                #print("priority shift")
                current = mcpIndex
                startTimeLine = timeLine
                tempBurstTime = 0
    
            #print()
            #print("timeLine >> ",timeLine)
    
        #print("process - timeLine - burstTime")
        print("ganttChart2 >> ",ganttChart2)
        print("---------- Break point ----------")
        for i in ganttChart2:
            self.trueSequence.append(i[0])
            self.trueBurstTime.append(i[2])
    

    def RR(self):
        arrivalTime = self.startingTime
        priority = self.priority
        burstTime = self.timeForEachProcess
        quantum = int(self.quantumLE.text())

        #arrivalTime = [0,1,5,6,7,8]
        #priority = [3,3,1,1,5,6]
        #burstTime = [6,4,6,6,6,6]
        #quantum = 2
        
        numberOfProcess = len(arrivalTime)
        # Conver into int
        for i in range(numberOfProcess):
            arrivalTime[i] = int(arrivalTime[i])
            priority[i] = int(priority[i])
            burstTime[i] = int(burstTime[i])
        # Process
        process = []
        pn = 0
        totalTime = 0
        for i,j,k in zip(arrivalTime, priority, burstTime):
            process.append([pn,i,j,k])
            totalTime += k
            pn += 1
        print("process >> ",process)
        # Find first process
        minA = min(arrivalTime)
        firstProcess = []
        for i in process:
            if i[1]==minA:
                firstProcess = i
            
        print("firstProcess >> ",firstProcess)
        
        gc = []
    
        timeLine = 0
        if firstProcess[3] > quantum:
            for i in range(quantum):
                gc.append(firstProcess[0])
                firstProcess[3] -= 1
                timeLine += 1
        else:
            for i in range(firstProcess[0]):
                gc.append(firstProcess[0])
                firstProcess[3] -= 1
                timeLine += 1
        current = firstProcess[0]
        old = current
        print("frist old : ",old)
        print("\n\ngc >> ",gc,"\n\n")
        temp = []
        while (timeLine != totalTime):
            for i in process:
                if i[1] <= timeLine and i[3]!=0 and i[0] != old:
                    found = False
                    for j in temp:
                        if i[0]==j[0]:
                            found = True
                        
                    if not found:
                        temp.append(i)
        
            temp.sort(key = lambda t:t[2], reverse = False) 
            for i in process:
                if i[0] == old and i[3] != 0:
                    temp.append(i)
            current = temp[0][0]
            print (temp)
            print("old : ",old)
            print("current: ",current)
            print("timeLine : ", timeLine)
            print()
            if current != old:
                if temp[0][3] > quantum:
                    for i in range(quantum):
                        gc.append(temp[0][0])
                        temp[0][3] -= 1
                        timeLine += 1
                else:
                    for i in range(temp[0][3]):
                        gc.append(temp[0][0])
                        temp[0][3] -= 1
                        timeLine += 1
                del temp[0]
            elif len(temp)>1:
                if temp[1][3] > quantum:
                    for i in range(quantum):
                        gc.append(temp[1][0])
                        temp[1][3] -= 1
                        timeLine += 1
                    else:
                        for i in range(temp[0][3]):
                            gc.append(temp[0][0])
                            temp[0][3] -= 1
                            timeLine += 1
                    del temp[0]
            elif len(temp)==1:
                if temp[0][3] > quantum:
                    for i in range(quantum):
                        gc.append(temp[0][0])
                        temp[0][3] -= 1
                        timeLine += 1
                else:
                    for i in range(temp[0][3]):
                        gc.append(temp[0][0])
                        temp[0][3] -= 1
                        timeLine += 1
                del temp[0]
                

    
            old = current

        print(temp)
    
        print("gc >> ",gc)
        print("len >> ",len(gc))

        cp = 0
        pp = gc[0]
        for i in gc:
            if i == pp:
                cp += 1
            else:
                self.trueSequence.append(pp)
                self.trueBurstTime.append(cp)
                pp = i
                cp = 1
        
        self.trueSequence.append(pp)
        self.trueBurstTime.append(cp)
        
        print("trueSe : ",self.trueSequence)
        print("trueBr : ",self.trueBurstTime)
        
    def TLQS(self):
            
        arrivalTime = self.startingTime
        priority = self.priority
        burstTime = self.timeForEachProcess
        quantum = int(self.quantumLE.text())

        #arrivalTime = [0,1,5,6,7,8]
        #priority = [3,3,1,1,5,6]
        #burstTime = [6,4,6,6,6,6]
        #quantum = 2

        numberOfProcess = len(arrivalTime)
        # Conver into int
        for i in range(numberOfProcess):
            arrivalTime[i] = int(arrivalTime[i])
            priority[i] = int(priority[i])
            burstTime[i] = int(burstTime[i])
    
        print("arrivalTime >> ",arrivalTime)
        print("priority >> ",priority)
        print("burstTime >> ",burstTime,"\n")
        tempTrueSequence = []
        for i in range(numberOfProcess):
            tempTrueSequence.append(i)
            
    
        # Check how many queues
        un_priority = list(set(priority))
        print(un_priority)
        queue = 0
        if (1 in un_priority) or (2 in un_priority):
            queue += 1
        if (3 in un_priority) or (4 in un_priority):
            queue += 1
        if (5 in un_priority) or (6 in un_priority):
            queue += 1
    
        print("Queue >> ", queue,"\n")
    
        # Add processes to queues
        q1 = {}
        q2 = {}
        q3 = {}
        # For final
        q1f = {}
        q2f = {}
        q3f = {}
        # Process in queue
        pq1 = []
        pq2 = []
        pq3 = []
        for i in range(numberOfProcess):
            j = burstTime[i], arrivalTime[i], priority[i]
            if priority[i] == 1 or priority[i] == 2: #print(1) 
                q1[tempTrueSequence[i]] = list(j)
                q1f[tempTrueSequence[i]] = list(j)
                pq1.append(tempTrueSequence[i])
            elif priority[i] == 3 or priority[i] == 4:  #print(2)
                q2[tempTrueSequence[i]] = list(j)
                q2f[tempTrueSequence[i]] = list(j)
                pq2.append(tempTrueSequence[i])
            elif priority[i] == 5 or priority[i] == 6:  #print(3)
                q3[tempTrueSequence[i]] = list(j)
                q3f[tempTrueSequence[i]] = list(j)
                pq3.append(tempTrueSequence[i])
        
        if len(q1) == 0:
            q1 = q2.copy()
            q2.clear()
        if len(q2) == 0:
            q2 = q3.copy()
            q3.clear()
            print("q3 len: ",len(q3))
        if len(q2) == 0 and len(q3)==0:
            QMessageBox.question(self, 'ERROR', "Must have at least 2 layers", QMessageBox.Ok)
            return 0
        
        print("q1 >> ",q1)
        print("q2 >> ",q2)
        print("q3 >> ",q3)
    
    
        totalTime = 0
        
        for i in q1:
            totalTime += q1[i][0]
        for i in q2:
            totalTime += q2[i][0]
        for i in q3:
            totalTime += q3[i][0]
        
        print("totalTime >> ", totalTime)
    
        # Round Robin for Queue 1
        '''
        Steps:
        1. Find least arrival time
        2. Find highest priority
        3. Check quantum:
        4. Add to the gantt chart
        5. Check current timeline
        6. Check if there is any process that that starting time is less than or equal to
            the current timeline
        7. Add that process into the Queue (check arrival time and priority first)
        8. Add the process that's on the top list to the gantt chart
        9. Repeat step 3
        '''
    
        #q1 = {0: [6, 0, 3], 1: [4, 1, 3], 2: [6, 5, 1], 3: [6, 6, 1], 4: [6, 7, 5], 5: [6, 8, 6]}
        print("\n")
        print("---------- Q1 ---------")
        print()
        ganttChart1 = {}
        wait = []
        current = 0
        totalTimeQ1 = 0
        timeLine = 0
        for i in q1:
            totalTimeQ1 += q1[i][0]
    
        minA = 99
        minP = 2
        for i in q1:
            if q1[i][1] <= minA:
                minA = q1[i][1]
                if q1[i][2] <= minP:
                    minP = q1[i][2]
                    current = i
    
        timeLine = q1[current][1]
        #print("current >> ",current)
        count = 12
        tempBurstTime = 0
        for i in range(q1[current][0]):
            if tempBurstTime < quantum:
                tempBurstTime += 1
            else:
                break
    
        q1[current][0] = q1[current][0] - tempBurstTime
        a = list((current,tempBurstTime))
        ganttChart1[totalTimeQ1] = a
        #ganttChart11.append((current,q1[current][1],tempBurstTime))
        #print("ganttChart1 >> ",ganttChart1)
        timeLine += ganttChart1[totalTimeQ1][1]
        #print("timeLine >> ",timeLine)
        totalTimeQ1 -= tempBurstTime
        #print("totalTimeQ1 >> ",totalTimeQ1)
    
        while totalTimeQ1 > 0 and count > 0: 
            for i in q1:
                if i != current and q1[i][1] <= timeLine:
                    wait.append(i)
            
            #print("wait >> ",wait)
            #print()
            tempBurstTime = 0
            for i in range(q1[wait[0]][0]):
                if tempBurstTime < quantum:
                    tempBurstTime += 1
                else:
                    break
    
            q1[wait[0]][0] -= tempBurstTime
            q1[wait[0]][1] += tempBurstTime
            a = list((wait[0],tempBurstTime))
            ganttChart1[totalTimeQ1] = a
            #ganttChart11.append((current,q1[current][1],tempBurstTime))
    
            #print("timeLine >> ",timeLine)
            current = wait[0]
            del wait[0]
    
            timeLine += ganttChart1[totalTimeQ1][1]
    
            #print("q1 >> ",q1)
            totalTimeQ1 -= tempBurstTime
            #print("totalTimeQ1 >> ",totalTimeQ1)
            count -= 1
        
        print("final 00 >> ",ganttChart1)
        #print("final 11 >> ", ganttChart11)
    
        # FCFS for q2
        # find first process
        print("\n")
        print("---------- Q2 ---------")
        print()
        #q2 = {0: [6, 0, 3], 1: [4, 1, 3], 2: [6, 5, 1], 3: [6, 6, 1], 4: [6, 7, 5], 5: [6, 8, 6]}
        totalTimeQ2 = 0
        for i in q2:
            totalTimeQ2 += q2[i][0]
        
        aa = totalTimeQ2
        minA = 99
        minP = 99
        for i in q2:
            if q2[i][1] <= minA:
                minA = q2[i][1]
                if q2[i][2] <= minP:
                    minP = q2[i][2]
                    current = i
    
        #print(q2[current])
        timeLine = q2[current][1]
        aa += timeLine
        #print("timeLine >> ",timeLine)
        ganttChart2 = []
        count = len(q2)
        wait = []
        tempBurstTime = 0
        mcp = 6 # Max current priority
        mcpIndex = 99
        oldCurrent = 99
        startTimeLine = timeLine
        while timeLine < aa:
            tempBurstTime += 1
            a = ((current,startTimeLine, tempBurstTime))
            #print("oldCurrent >> ",oldCurrent, " current >> ",current)
            if current == oldCurrent:
                ganttChart2[len(ganttChart2)-1] = a
            else:
                ganttChart2.append(a)
            oldCurrent = current
            #totalTimeQ2 -= tempBurstTime
            q2[current][0] -= 1
            timeLine += 1
            #print(current,"burstTime of q >> ",q2[current][0])
            found = False
            for i in q2:
                if q2[i][1] == timeLine and q2[i][2] < mcp:
                    found = True
                    mcp = q2[i][2]
                    mcpIndex = i
            
            if not found:
                mcp = q2[current][2]
                mcpIndex = current 
    
            #print("mcp >> ",mcp)
            #print("mcpIndex >> ",mcpIndex)
            #print("current priority >> ",q2[current][2])
    
            if(q2[current][0] == 0):
                tempList = []
                #print("Q2 >> ",q2)
                
                for i in q2:
                    #print("another process >> ",i,q2[i])
                    if q2[i][1]<=timeLine and q2[i][0] != 0:
                        #print("---------- break point ----------")
                        tempList.append(i)
                    
                # Create list for priority
                tempPri = []
                for i in tempList:
                    tempPri.append(q2[i][2])
    
                if(len(tempPri) == 0): break
                # Find highest priority
                x = min(tempPri)
    
                # Count how many highest priority
                dupl = tempPri.count(x)
                #print("dup >> ",dupl)
    
                # if only 1, set current to it
                if dupl == 1:
                    for i in tempList:
                        if q2[i][2] == x:
                            current = i
                            break
                else:
                    # Create list for arrival time
                    tempArr = []
                    for i in tempList:
                        if q2[i][2] == x:
                            tempArr.append(q2[i][1])
    
                    # Find who comes first
                    y = min(tempArr)
                    #print("who come first >> ",y)
                    # set current to it
                    for i in tempList:
                        if q2[i][1] == y:
                            current = i
                            break
                    
                startTimeLine = timeLine
                tempBurstTime = 0
                
            elif q2[current][2] > mcp:
                #print("priority shift")
                current = mcpIndex
                startTimeLine = timeLine
                tempBurstTime = 0
    
            #print()
            #print("timeLine >> ",timeLine)
    
        #print("process - timeLine - burstTime")
        print(ganttChart2)
    
        
        if len(q3) != 0:
            print("\n")
            print("---------- Q3 ---------")
            print()
    
        totalTimeQ3 = 0
        for i in q3:
            totalTimeQ3 += q3[i][0]
        
        aa = totalTimeQ3
        minA = 99
        minP = 99
        for i in q3:
            if q3[i][1] <= minA:
                minA = q3[i][1]
                if q3[i][2] <= minP:
                    minP = q3[i][2]
                    current = i
    
        #print("q3 >> ",q3)
        timeLine = q3[current][1]
        aa += timeLine
        #print("timeLine >> ",timeLine)
        ganttChart3 = []
        count = len(q3)
        wait = []
        tempBurstTime = 0
        mcp = 6 # Max current priority
        mcpIndex = 99
        oldCurrent = 99
        startTimeLine = timeLine
        while timeLine < aa:
            tempBurstTime += 1
            a = ((current,startTimeLine, tempBurstTime))
            #print("oldCurrent >> ",oldCurrent, " current >> ",current)
            if current == oldCurrent:
                ganttChart3[len(ganttChart3)-1] = a
            else:
                ganttChart3.append(a)
            oldCurrent = current
            totalTimeQ1 -= tempBurstTime
            q3[current][0] -= 1
            timeLine += 1
            #print(current,"burstTime of q >> ",q3[current][0])
            found = False
            for i in q3:
                if q3[i][1] == timeLine and q3[i][2] < mcp:
                    found = True
                    mcp = q3[i][2]
                    mcpIndex = i
            
            if not found:
                mcp = q3[current][2]
                mcpIndex = current 
    
            #print("mcp >> ",mcp)
            #print("mcpIndex >> ",mcpIndex)
            #print("current priority >> ",q3[current][2])
    
            if(q3[current][0] == 0):
                tempList = []
                #print("Q3 >> ",q3)
                
                for i in q3:
                    #print("another process >> ",i,q3[i])
                    if q3[i][1]<=timeLine and q3[i][0] != 0:
                        #print("---------- break point ----------")
                        tempList.append(i)
                    
                # Create list for priority
                tempPri = []
                for i in tempList:
                    tempPri.append(q3[i][2])
    
                if(len(tempPri) == 0): break
                # Find highest priority
                x = min(tempPri)
    
                # Count how many highest priority
                dupl = tempPri.count(x)
                #print("dup >> ",dupl)
    
                # if only 1, set current to it
                if dupl == 1:
                    for i in tempList:
                        if q3[i][2] == x:
                            current = i
                            break
                else:
                    # Create list for arrival time
                    tempArr = []
                    for i in tempList:
                        if q3[i][2] == x:
                            tempArr.append(q3[i][1])
    
                    # Find who comes first
                    y = min(tempArr)
                    #print("who come first >> ",y)
                    # set current to it
                    for i in tempList:
                        if q3[i][1] == y:
                            current = i
                            break
                    
                startTimeLine = timeLine
                tempBurstTime = 0
                
            elif q3[current][2] > mcp:
                #print("priority shift")
                current = mcpIndex
                startTimeLine = timeLine
    
            #print()
            #print("timeLine >> ",timeLine)
    
        print("process - timeLine - burstTime")
        print(ganttChart3)
        print()
    
        # final step
        print("---------- Final step ----------\n")
        finalGanttChart1 = []
        finalGanttChart2 = []
        finalGanttChart3 = []
        newGanttChart1 = []
    
        # finalGanttChart1
        # Find first process
        fp = 0 # First process in ganttChart 1
        lp = 0 # Last process in ganttChart 1
        for i,j in ganttChart1.items():
            if fp == 0:
                fp = j[0]
                break
        at = 0
        for i,j in q1f.items():
            print(i,j)
            if i == fp:
                at = j[1]
    
        at2 = at
        print("arrival time Q1 = ", at)
    
        for i,j in ganttChart1.items():
            a = list((j[0],j[1]))
            newGanttChart1.append(a)
            at += j[1]
    
        print("new ganttChart1 >> ",newGanttChart1)
        
        i = 0
        while i < totalTime:
            if i != at2:
                finalGanttChart1.append([-1,1])
                i += 1
            if i == at2:
                for j in newGanttChart1:
                    for k in range(j[1]):
                        finalGanttChart1.append([j[0],1])
                        i += 1
        
        tt = 0
        for i in finalGanttChart1:
            tt += i[1]
        
        tt = totalTime - tt
        #finalGanttChart1.append([-1,tt])
        # finalGanttChart1 done
        print()
        print("finalGanttChart1 >> ",finalGanttChart1)
        print("Length >> ", len(finalGanttChart1))
        realGanttChart1 = []
        for i in range(totalTime):
            realGanttChart1.append(finalGanttChart1[i])
        gc1 = tuple(finalGanttChart1.copy())
        
        # finalGanttChart2
        finalGanttChart2 = finalGanttChart1.copy()
        temp2 = []
        # conver ganttChart2 to 1 unit time
        currentPos = 0
        for i in ganttChart2:
            for k in range(i[1]-currentPos):
                temp2.append((-1,1))
                currentPos += 1
            for k in range(i[2]):
                temp2.append([i[0],1])
                currentPos += 1
        for i in range(totalTime - currentPos):
            temp2.append([-1,1])
    
        print()
        print("temp2 >> ",temp2)
        #print("currentPos >> ", currentPos)
        wait = []
        for i in range(totalTime):
            if finalGanttChart2[i][0]==-1 and temp2[i][0]!=-1 and len(wait)==0:
                finalGanttChart2[i] = temp2[i]
                #print(1)
            elif finalGanttChart2[i][0]!=-1 and temp2[i][0]!=-1:
                wait.append(temp2[i])
                #print(2,temp2[i])
            elif finalGanttChart2[i][0]==-1 and temp2[i][0]==-1 and len(wait)>0:
                finalGanttChart2[i] = wait[0]
                del wait[0]
                #print(3)
            elif finalGanttChart2[i][0]==-1 and temp2[i][0]!=-1 and len(wait)>0:
                finalGanttChart2[i] = wait[0]
                del wait[0]
                wait.append(temp2[i])
            else:
                pass
                #print(finalGanttChart2[i][0]!=-1,temp2[i][0]!=-1,len(wait)>0)
            #print("wait >> ",wait)
        
    
        print()
        print("finalGanttChart2 >> ",finalGanttChart2)
        print("Length >> ", len(finalGanttChart2))
    
        if (len(q3)!=0):
            finalGanttChart3 = finalGanttChart2.copy()
            temp3 = []
            # conver ganttChart2 to 1 unit time
            currentPos = 0
            for i in ganttChart3:
                for k in range(i[1]-currentPos):
                    temp3.append((-1,1))
                    currentPos += 1
                for k in range(i[2]):
                    temp3.append([i[0],1])
                    currentPos += 1
            for i in range(totalTime - currentPos):
                temp3.append([-1,1])
        
            print()
            #print("temp3 >> ",temp3)
            #print("currentPos >> ", currentPos)
            wait = []
            for i in range(totalTime):
                if finalGanttChart3[i][0]==-1 and temp3[i][0]!=-1 and len(wait)==0:
                    finalGanttChart3[i] = temp3[i]
                    #print(1)
                elif finalGanttChart3[i][0]!=-1 and temp3[i][0]!=-1:
                    wait.append(temp3[i])
                    #print(2,temp2[i])
                elif finalGanttChart3[i][0]==-1 and temp3[i][0]==-1 and len(wait)>0:
                    finalGanttChart3[i] = wait[0]
                    del wait[0]
                    #print(3)
                elif finalGanttChart3[i][0]==-1 and temp3[i][0]!=-1 and len(wait)>0:
                    finalGanttChart3[i] = wait[0]
                    del wait[0]
                    wait.append(temp3[i])
                else:
                    pass
                    #print(finalGanttChart2[i][0]!=-1,temp2[i][0]!=-1,len(wait)>0)
                #print("wait >> ",wait)
            
            print()
            print("finalGanttChart3 >> ",finalGanttChart3)
            print("Length >> ", len(finalGanttChart3))
            
            # real final step
            gc1 = finalGanttChart1.copy()
            temp = []
            cpp = 0
            pp = gc1[0][0]
            cp = gc1[0][0]
            for i in gc1:
                cp = i[0]
                #print("current >> ",cp)
                #print("previous>> ",pp)
                #print()
                if cp == pp:
                    cpp += 1
                elif cp != pp:
                    temp.append([pp,cpp])
                    cpp = 1
                #print("count > ",pp," ",cpp)
                pp = i[0]

            temp.append([pp,cpp])
            #print("Temp >> ",temp)
            #print()
            gc1 = temp.copy()
            self.gc1 = gc1
            gc2 = finalGanttChart2.copy()
            gc3 = finalGanttChart3.copy()
            for i in gc2:
                if i[0] in pq1 or i[0] in pq3:
                    i[0] = -1
            temp = []
            cpp = 0
            pp = gc2[0][0]
            cp = gc2[0][0]
            for i in gc2:
                cp = i[0]
                #print("current >> ",cp)
                #print("previous>> ",pp)
                #print()
                if cp == pp:
                    cpp += 1
                elif cp != pp:
                    temp.append([pp,cpp])
                    cpp = 1
                #print("count > ",pp," ",cpp)
                pp = i[0]

            temp.append([pp,cpp])
            #print("Temp >> ",temp)
            #print()
            gc2 = temp.copy()
            self.gc2 = gc2
                
            #print("pq3 >> ",pq3)
            for i in gc3:
                if i[0] in pq1 or i[0] in pq2:
                    i[0] = -1
            temp = []
            cpp = 0
            pp = gc3[0][0]
            cp = gc3[0][0]
            for i in gc3:
                cp = i[0]
                #print("current >> ",cp)
                #print("previous>> ",pp)
                #print()
                if cp == pp:
                    cpp += 1
                elif cp != pp:
                    temp.append([pp,cpp])
                    cpp = 1
                #print("count > ",pp," ",cpp)
                pp = i[0]

            temp.append([pp,cpp])
            #print("Temp >> ",temp)
            #print()
            gc3 = temp.copy()
            self.gc3 = gc3
                
            
            print("\n")
            print("gc1 >> ",gc1)
            print("\n")
            print("gc2 >> ",gc2)
            print("\n")
            print("gc3 >> ",gc3)
            print("\n")

            print("process - burstTime")



    def SRTN(self):
        # reference:
        # self.startingTime = list of arrival time
        # self.timeForEachProcess = list of burst time
        # self.priority = list of priority 
    
        # local variables of SRTN
        arrivalTime = self.startingTime 
        burstTime = self.timeForEachProcess
        priority = self.priority
        remainingTime = burstTime # initialize each initial remaining time as burst time
        finishTime = sum(self.timeForEachProcess)
        processes = []
        processList = [] # list of process to be colored per 1 time unit
        
        currentTime = 2 # initialize at 1
        readyQueue = []
        processLabel = 0
        firstProcess = []
    
        minn = min(arrivalTime)
        print("In SRTN")

        for i in range(self.nop):
            processObj = [processLabel, arrivalTime[i], burstTime[i], priority[i], remainingTime[i]]
            processes.append(processObj)
            if(processes[i][1] == 0):
                firstProcess = processes[i]
            processLabel += 1

        print(processes)

        runningProcess = firstProcess # initialize runningProcess
        processList.append(runningProcess)
        runningProcess[4] -= 1

        print('current time:' + str(currentTime-1))
        print("ready queue: " + str(readyQueue))
        print('running process: ' + str(runningProcess))

        # adds new process to ready queue at time = 1
        for i in range(self.nop):
            if(processes[i][1] == 1):
                readyQueue.append(processes[i])

        # new running process will be the shortest remaining time
        if(runningProcess[4] == 0):
            runningProcess = readyQueue[0]
            readyQueue = readyQueue[1:]
        
        while(currentTime <= finishTime):
                
            print('current time:' + str(currentTime))
            print("ready queue: " + str(readyQueue))
                    
            # compare and do preemption when new process arrives
            if(len(readyQueue) != 0):
                print("something in ready queue")
                if(currentTime == 1):
                    pass
                else:
                    # compare remaining time
                    # if running process remaining time < new process burst time, then continue do the running process
                    if(runningProcess[4] < readyQueue[0][2]):
                        print('running process: ' + str(runningProcess))
                        processList.append(runningProcess)
                        runningProcess[4] -= 1
                        print('remaining time: ' + str(runningProcess[4]))
                    # if running process remaining time = new process burst time, then compare priority
                    elif(runningProcess[4] == readyQueue[0][2]):
                        if (runningProcess[3] <= readyQueue[0][3]):
                            print('running process: ' + str(runningProcess))
                            processList.append(runningProcess)
                            runningProcess[4] -= 1
                            print('remaining time: ' + str(runningProcess[4]))
                        else:
                            readyQueue.append(runningProcess)
                            runningProcess = readyQueue[0]
                            print('running process: ' + str(runningProcess))
                            readyQueue = readyQueue[1:]
                            processList.append(runningProcess)
                            runningProcess[4] -= 1
                            print('remaining time: ' + str(runningProcess[4]))
                    # if running process remaining time > new process burst time, then preempt
                    else:
                        readyQueue.append(runningProcess)
                        runningProcess = readyQueue[0]
                        print('running process: ' + str(runningProcess))
                        readyQueue = readyQueue[1:]
                        processList.append(runningProcess)
                        runningProcess[4] -= 1
                        print('remaining time: ' + str(runningProcess[4]))
            else:
                processList.append(runningProcess)
                print('running process: ' + str(runningProcess))
                runningProcess[4] -= 1
                print('remaining time: ' + str(runningProcess[4]))

            # adds new process to ready queue
            for i in range(self.nop):
                if(processes[i][1] == currentTime):
                    readyQueue.append(processes[i])

            # new running process will be the shortest remaining time
            if(runningProcess[4] == 0 and (len(readyQueue) != 0)):
                runningProcess = readyQueue[0]
                readyQueue = readyQueue[1:]
                
            # sort the readyQueue according to shortest remainingTime and priority
            if(len(readyQueue) != 0):
                readyQueue = sorted(readyQueue, key = lambda x: (x[4], x[3]))
            currentTime += 1

        # Everything has ended, create new list
        print('test bug')
        self.trueSequence.append(processList[0][0])
        self.trueBurstTime.append(1)

        print(processList)
        
        for i in range(1, finishTime):
            if processList[i][0] == processList[i-1][0]:
                self.trueBurstTime[-1] += 1
            else:
                self.trueSequence.append(processList[i][0])
                self.trueBurstTime.append(1)

        print("processList >> ",self.trueSequence)
        print("burstTime >> ",self.trueBurstTime)

    def hideStuff(self):
        j = 280
        # LineEdit for starting time each process
        for i in range(10):
            st = QLineEdit(self)
            st.resize(0, 0)
            st.move(j, 155)
            self.processStartLineEdit.append(st)
            j += 30

        j = 280
        for i in range(10):
            t = QLineEdit(self)
            t.resize(0, 0)
            t.move(j, 185)
            self.processTimeLineEdit.append(t)
            j += 30

        j = 280
        for i in range(10):
            p = QLineEdit(self)
            p.resize(0,0)
            p.move(j,215)
            self.priorityLineEdit.append(p)
            j += 30
            
        # Number for ruler
        for i in range(200):
            self.num = QLabel("", self)
            self.nums.append(self.num)

        # Label for each process
        for i in range(100):
            self.pro = QLabel("",self)
            self.processLabel.append(self.pro)

    def clearStuff(self):
        for i,j,k in zip(self.processStartLineEdit,self.processTimeLineEdit,self.priorityLineEdit):
            i.resize(0,0)
            j.resize(0,0)
            k.resize(0,0)
        
        for i in self.processLabel:
            i.setText("")
        
        for k in self.nums:
            k.setText("")

        self.trueBurstTime.clear()
        self.trueSequence.clear()
        self.startingTime.clear()
        self.timeForEachProcess.clear()
        self.nop = 0

    def checkInput(self, text):
        print(text," ",type(text))
        if text != "1" or text != "2" or text != "3" or text != "4" or text != "5" or text != "6" or text != "7" or text != "8" or text != "9" or text != "10":
            return False
        else:
            return True 



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
