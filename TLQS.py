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
    tempTrueBurstingTime = []
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
    for i in range(numberOfProcess):
        if priority[i] == 1 or priority[i] == 2: #print(1) 
            j = burstTime[i], arrivalTime[i], priority[i]
            q1[tempTrueSequence[i]] = list(j)
        elif priority[i] == 3 or priority[i] == 4:  #print(2)
            q2[tempTrueSequence[i]] = (burstTime[i], arrivalTime[i], priority[i])
        elif priority[i] == 5 or priority[i] == 6:  #print(3)
            q3[tempTrueSequence[i]] = (burstTime[i], arrivalTime[i], priority[i])
    
    print("q1 >> ",q1)
    print("q2 >> ",q2)
    print("q3 >> ",q3)

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

    ganttChart1 = {}
    wait = []
    current = None
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
    print("current >> ",current)
    count = 12
    tempBurstTime = 0
    for i in range(q1[current][0]):
        if tempBurstTime < quantum:
            tempBurstTime += 1
        else:
            break

    q1[current][0] = q1[current][0] - tempBurstTime
    ganttChart1[totalTimeQ1] = current,tempBurstTime
    print("ganttChart1 >> ",ganttChart1)
    timeLine += ganttChart1[totalTimeQ1][1]
    print("timeLine >> ",timeLine)
    totalTimeQ1 -= tempBurstTime
    print("totalTimeQ1 >> ",totalTimeQ1)

    while totalTimeQ1 > 0 and count > 0: 
        for i in q1:
            if i != current and q1[i][1] <= timeLine:
                wait.append(i)
        
        print("wait >> ",wait)
        print()
        tempBurstTime = 0
        for i in range(q1[wait[0]][0]):
            if tempBurstTime < quantum:
                tempBurstTime += 1
            else:
                break

        q1[wait[0]][0] -= tempBurstTime
        q1[wait[0]][1] += tempBurstTime
        ganttChart1[totalTimeQ1] = wait[0],tempBurstTime 
        
        print("timeLine >> ",timeLine)
        current = wait[0]
        del wait[0]

        timeLine += ganttChart1[totalTimeQ1][1]

        print("q1 >> ",q1)
        totalTimeQ1 -= tempBurstTime
        print("totalTimeQ1 >> ",totalTimeQ1)
        count -= 1
    
    print("final >> ",ganttChart1)



def main():
    arrivalTime = ["0","1","5","6","7","8"]
    priority = ["3","3","2","1","5","6"]
    burstTime = ["6","4","6","6","6","6"]
    quantum = 2
    TLQS(arrivalTime,priority, burstTime, quantum)

if __name__ == "__main__":
    main()