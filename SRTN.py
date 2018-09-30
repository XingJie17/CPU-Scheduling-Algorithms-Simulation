import Process

def SRTN(self):
    # reference:
    # self.startingTime = list of arrival time
    # self.timeForEachProcess = list of burst time
    # self.priority = list of priority 

    # local variables of SRTN
    processLabel = self.processLabel
    arrivalTime = self.startingTime 
    burstTime = self.timeForEachProcess
    priority = self.priority
    remainingTime = burstTime # initialize each initial remaining time as burst time
    finishTime = sum(self.timeForEachProcess)
    processList = [] # list of process to be colored per 1 time unit
    
    currentTime = 1 # initialize at 1
    processList = []
    readyQueue = []
    

    for i in range(self.numberOfProcess):
        processList.append(Process(processLabel[i], arrivalTime[i], burstTime[i], priority[i], remainingTime[i]))
        if(processList[i].arrivalTime == 0):
            firstProcess = processList[i]

    runningProcess = firstProcess # initialize runningProcess
    
    while(currentTime != finishTime):
        # adds new process to ready queue
        for i in range(self.numberOfProcess):
            if(processList[i].arrivalTime == currentTime):
                readyQueue.append(processList[i])
                
        # compare and do preemption when new process arrives
        if(len(readyQueue) != 0):
            if(readyQueue[-1].arrivalTime == currentTime):
                if(runningProcess == firstProcess):
                    processList.append(readyQueue[0].processLabel) # color it
                    readyQueue = readyQueue[1:] # delete from ready queue
                    runningProcess.remainingTime -= 1
                else: # compare remaining time
                    # if running process remaining time < new process burst time, then continue do the running process
                    if(runningProcess.remainingTime < readyQueue[0].burstTime):
                        processList.append(runningProcess.processLabel)
                        runningProcess.remainingTime -= 1
                    # if running process remaining time = new process burst time, then compare priority
                    elif(runningProcess.remainingTime == readyQueue[0].burstTime):
                        if (runningProcess.priority <= readyQueue[0].priority):
                            processList.append(runningProcess.processLabel)
                            runningProcess.remainingTime -= 1
                        else:
                            readyQueue.append(runningProcess)
                            runningProcess = readyQueue[0]
                            readyQueue = readyQueue[1:]
                            processList.append(runningProcess.processLabel)
                            runningProcess.remainingTime -= 1
                    # if running process remaining time > new process burst time, then preempt
                    else:
                        readyQueue.append(runningProcess)
                        runningProcess = readyQueue[0]
                        readyQueue = readyQueue[1:]
                        processList.append(runningProcess.processLabel)
                        runningProcess.remainingTime -= 1
            currentTime += 1
        else:
            processList.append(runningProcess.processLabel)
            runningProcess.remainingTime -= 1
            currentTime += 1
            
        # sort the readyQueue according to shortest remainingTime and priority
        # to-do
        readyQueue = sorted(readyQueue, key = lambda x: (x.remainingTime, x.priority))

        # new running process will be the shortest remaining time
        if(runningProcess.remainingTime == 0):
            runningProcess = readyQueue[0]
            readyQueue = readyQueue[1:]


def main():
    arrivalTime = ["0","1","5","6","7","8"]
    priority = ["3","3","2","1","5","6"]
    burstTime = ["6","4","6","6","6","6"]
    quantum = 2
    SRTN(Process)

if __name__ == "__main__":
    main()