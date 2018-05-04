class process:
    def __init__(self,name=" ",bus=0,arrive=0):
        p_name=name
        p_bus_time=bus
        p_arrival_time=arrive
        p_depart_time=0
        p_start_time=0
        p_run_time=0
        p_t_bus=0

def printtime():
    print("PROCESS NAME\tARRIVAL TIME\tBUS TIME      START EXE TIME\tTERMINATION TIME   WAITING TIME\tTURNARROUND TIME")
    avg_waitng=0
    avg_turnarround=0
    for k in range(count):
        avg_waitng+=obj[k].p_start_time-obj[k].p_arrival_time
        avg_turnarround+=obj[k].p_depart_time-obj[k].p_arrival_time
        print("  ",obj[k].p_name+"\t\t",obj[k].p_arrival_time,"\t\t",obj[k].p_bus_time,"\t\t   ",obj[k].p_start_time,"\t\t      ",obj[k].p_depart_time,"\t\t",obj[k].p_start_time-obj[k].p_arrival_time,"\t\t",obj[k].p_depart_time-obj[k].p_arrival_time )
    print("AVERAGE WAITING TIME IS :  ",avg_waitng/count)
    print("AVERAGE TURNARROUND TIME IS : ",avg_turnarround/count)
#///////////////////////////////////////////////////////////////////////////////////////////////////////


#///////////////////////////////////////////////////////////////////////////////////////////////////////

def inc_time(s=-1):
    global total_time
    global t_index
    total_time+=1
    if s!=-1:
        readylist[s].p_run_time+=1
        if  readylist[s].p_run_time==readylist[s].p_bus_time:
            readylist[s].p_depart_time=total_time
            readylist[s].p_t_bus=55555555
            if t_index!=count:
                t_ind=t_index
                while(obj[t_index].p_arrival_time>total_time):
                    total_time+=1
                for i in range(t_ind,count):
                        if obj[i].p_arrival_time<=total_time:
                            readylist.append(obj[i])
                            t_index+=1
            readylist.sort(key = lambda c: c.p_t_bus)
            del readylist[-1]

count=int(input("how many process you want tu enter "))
obj=[process() for i in range(count)]
for i in range(count):
    obj[i].p_name="p"+str(i)
    obj[i].p_bus_time=int(input("enter the bus time for  process no "+str(i+1)+" : "))
    obj[i].p_arrival_time=int(input("enter the arrival time for  process no "+str(i+1)+" : "))
    obj[i].p_depart_time=0
    obj[i].p_start_time=-1
    obj[i].p_run_time=0
    obj[i].p_t_bus=obj[i].p_bus_time
    import os
    os.system('cls')
obj.sort(key = lambda c: c.p_arrival_time)
readylist=[]
t_value=obj[0].p_arrival_time
readylist.append(obj[0])
t_index=1
while(t_index<count and obj[t_index].p_arrival_time==t_value):
       readylist.append(obj[t_index])
       t_index+=1
total_time=0
while(readylist):
        while(readylist[0].p_arrival_time>total_time):
            total_time+=1
        if(readylist[0].p_start_time==-1):
            readylist[0].p_start_time=total_time
        inc_time(0)
printtime()