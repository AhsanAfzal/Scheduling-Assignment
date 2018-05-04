quanta=3
count=0
obj=[]
cpu=[]
total_time=0
waiting_queue=[]
executed=[]
readylist=[]
class process:
     def __init__(self):
            p_name=" "
            p_bus_time=0
            p_arrival_time=0
            p_input_after=0
            p_waiting=0
            rem_quantum=0
            rem_input=0
            p_depart_time=0
            p_start_time=0
            p_run_time=0
            p_dept_waiting=0
#/////////////////////////////////////////////////////////////////////////////////////
def loadreadyqueue():
    global total_time
    global obj
    global readylist
    while(obj and obj[0].p_arrival_time==total_time):
            readylist.append(obj[0])
            del obj[0]
    while(waiting_queue and waiting_queue[0].p_dept_waiting==total_time):
        readylist.append(waiting_queue[0])
        del waiting_queue[0]
#/////////////////////////////////////////////////////////////////////////////////////
def printtime():
    global count
    global executed
    print("PROCESS NAME\tARRIVAL TIME\tBUS TIME      START EXE TIME\tTERMINATION TIME   WAITING TIME\tTURNARROUND TIME")
    avg_waitng=0
    avg_turnarround=0
    for k in range(count):
        avg_waitng+=executed[k].p_depart_time-executed[k].p_arrival_time-executed[k].p_bus_time
        avg_turnarround+=executed[k].p_depart_time-executed[k].p_arrival_time
        print("  ",executed[k].p_name+"\t\t",executed[k].p_arrival_time,"\t\t",executed[k].p_bus_time,"\t\t   ",executed[k].p_start_time,"\t\t      ",executed[k].p_depart_time,"\t\t",executed[k].p_depart_time-executed[k].p_arrival_time-executed[k].p_bus_time,"\t\t",executed[k].p_depart_time-executed[k].p_arrival_time )
    print("AVERAGE WAITING TIME IS :  ",avg_waitng/count)
    print("AVERAGE TURNARROUND TIME IS : ",avg_turnarround/count)
#///////////////////////////////////////////////////////////////////////////////////////////////////////
def inc_time():
    global total_time
    global obj
    global readylist
    global cpu
    global waiting_queue
    global quanta
    total_time+=1
    loadreadyqueue()
    cpu[0].rem_quantum-=1
    cpu[0].rem_input-=1
    cpu[0].p_run_time+=1
    #------------------------------------------------------------
    if(cpu[0].p_run_time==cpu[0].p_bus_time):
        cpu[0].p_depart_time=total_time
        executed.append(cpu[0])
        del cpu[0]
        if(readylist):
            cpu.append(readylist[0])
            del readylist[0]
        elif waiting_queue or obj:
            while(True):
                total_time+=1
                loadreadyqueue()
                if(readylist):
                    break
            cpu.append(readylist[0])
            del readylist[0]
    elif (cpu[0].rem_input==0):
        if cpu[0].rem_quantum==0:
               cpu[0].rem_quantum=quanta
        cpu[0].p_dept_waiting=total_time+cpu[0].p_waiting
        cpu[0].rem_input=cpu[0].p_input_after
        waiting_queue.append(cpu[0])
        del cpu[0]
        if(readylist):
            while(readylist[0].p_arrival_time>total_time):
                total_time+=1
                loadreadyqueue()
            cpu.append(readylist[0])
            del readylist[0]
        elif waiting_queue or obj:
            while(True):
                total_time+=1
                loadreadyqueue()
                if(readylist):
                    break
            cpu.append(readylist[0])
            del readylist[0]
        waiting_queue.sort(key=lambda c: c.p_dept_waiting)

    elif(cpu[0].rem_quantum==0):
        cpu[0].rem_quantum=quanta
        readylist.append(cpu[0])
        del cpu[0]
        if(readylist):
            cpu.append(readylist[0])
            del readylist[0]    
#////////////////////////////////////////////////////////////////////////////////////
def inputtime():
        global obj
        global quanta
        global count
        count=int(input("how many process you want t0 enter "))
        obj=[process() for i in range(count)]
        for i in range(count):
            obj[i].p_name="p"+str(i)
            obj[i].p_bus_time=int (input ("enter the burst time for  process no "+str(i+1)+" : "))
            obj[i].p_arrival_time=int(input("enter the arrival time for  process no "+str(i+1)+" : "))
            if 1==int(input("enter ( 1 ) if program will wait for input else press any other button : ")):
                obj[i].p_input_after= int(input("enter the time after which process will go for input : "))
                obj[i].rem_input=obj[i].p_input_after
                obj[i].p_waiting=int(input("enter the time for which process will wait for input : "))
            else:
                obj[i].p_input_after=0
                obj[i].rem_input=-1
                obj[i].p_waiting=0
            obj[i].p_depart_time=0
            obj[i].p_start_time=-1
            obj[i].p_run_time=0
            obj[i].p_dept_waiting=0
            obj[i]. rem_quantum=quanta
            import os
            os.system('cls')
        obj.sort(key = lambda c: c.p_arrival_time)
        temp=obj[0].p_arrival_time
        cpu.append(obj[0])
        del obj[0]
        while(obj and obj[0].p_arrival_time==temp):
            readylist.append(obj[0])
            del obj[0]
      #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
inputtime()
while(cpu):
        while(cpu[0].p_arrival_time>total_time):
            total_time+=1
            loadreadyqueue()
        if(cpu[0].p_start_time==-1):
           cpu[0].p_start_time=total_time
        inc_time()
printtime()