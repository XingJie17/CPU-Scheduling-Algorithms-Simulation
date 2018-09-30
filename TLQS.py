def TLQS(arrivalTime, priority, burstTime, quantum):
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
    
    if len(q2) == 0:
        q2 = q3
    
    print("q1 >> ",q1)
    print("q2 >> ",q2)
    print("q3 >> ",q3)


    totalTime = 0
    for i,j,k in zip(q1,q2,q3):
        totalTime += q1[i][0]
        totalTime += q2[j][0]
        totalTime += q3[k][0]

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
    q2 = {0: [6, 0, 3], 1: [4, 1, 3], 2: [6, 5, 1], 3: [6, 6, 1], 4: [6, 7, 5], 5: [6, 8, 6]}
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
        totalTimeQ1 -= tempBurstTime
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
    
        print("i >> ", i)
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
    print("currentPos >> ", currentPos)
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
        print("temp3 >> ",temp3)
        print("currentPos >> ", currentPos)
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
            else:
                pass
                #print(finalGanttChart2[i][0]!=-1,temp2[i][0]!=-1,len(wait)>0)
            #print("wait >> ",wait)
        
        print()
        print("finalGanttChart3 >> ",finalGanttChart3)
        print("Length >> ", len(finalGanttChart3))
        
        # real final step
        gc1 = finalGanttChart1.copy()
        gc2 = finalGanttChart2.copy()
        gc3 = finalGanttChart3.copy()
        print("pq1 >> ",pq1)
        print("pq2 >> ",pq2)
        for i in gc2:
            if i[0] in pq1 or i[0] in pq3:
                i[0] = -1
            
        print("pq3 >> ",pq3)
        for i in gc3:
            if i[0] in pq1 or i[0] in pq2:
                i[0] = -1
            
        
        print("\n")
        print("gc1 >> ",gc1)
        print("\n")
        print("gc2 >> ",gc2)
        print("\n")
        print("gc3 >> ",gc3)
        print("\n")


def RR(arrivalTime, priority, burstTime, quantum):
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
        #process = sorted(process,key = lambda t:t[2], reverse = True) 
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



def main():
    arrivalTime = ["0","1","5","6","7","8"]
    priority = ["3","3","1","1","5","6"]
    burstTime = ["6","4","6","6","6","6"]
    quantum = 2
    #TLQS(arrivalTime,priority, burstTime, quantum)
    RR(arrivalTime,priority, burstTime, quantum)

if __name__ == "__main__":
    main()
