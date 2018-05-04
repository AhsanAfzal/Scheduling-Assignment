import os
import time
from collections import OrderedDict
from operator import itemgetter
import json

totaltime=0

def printtime():
    print("PROCESS NAME\tARRIVAL TIME\tBUS TIME      START EXE TIME\tTERMINATION TIME   WAITING TIME\tTURNARROUND TIME")
    avg_waitng=0
    avg_turnarround=0
    for k in r_queue:
        avg_waitng+=r_queue[k][2]-r_queue[k][0]
        avg_turnarround+=r_queue[k][2]-r_queue[k][0]+r_queue[k][4]
        print("  ",k+"\t\t",r_queue[k][0],"\t\t",r_queue[k][4],"\t\t   ",r_queue[k][2],"\t\t      ",r_queue[k][3],"\t\t",r_queue[k][2]-r_queue[k][0],"\t\t",r_queue[k][2]-r_queue[k][0]+r_queue[k][4]) 
    print("AVERAGE WAITING TIME IS :  ",avg_waitng/no_of_programs)
    print("AVERAGE TURNARROUND TIME IS : ",avg_turnarround/no_of_programs)
#///////////////////////////////////////////////////////////////////////////////////////////////////////
def inc_time(s='no'):
    global totaltime
    totaltime+=1
    if s!='no':
        r_queue[s][1]-=1
        if(r_queue[s][1]==0):
            r_queue[s][3]=totaltime

#///////////////////////////////////////////////////////////////////////////////////////////////////////
def loading():
    print("LOADING ",end="")
    for i in range(0,40):
        print('█',end='',flush=True)
        time.sleep(.010)
    print("",end='\n')
#///////////////////////////////////////////////////////////////////////////////////////////////////////
r_queue={}

#taking input //////////////////////////////////////////////////////////////////////////////////////////
no_of_programs=int(input("ENTER THE TOTAL NUMBER OF PRG YOU WANT TO RUN : "))

for i in range(0,int(no_of_programs)):
    bus_time=int(input("ENTER TOTAL BUS TIME FOR PROCESS "+str(i+1)+" : "))
    arrival_time = int(input("ENTER ARRIVAL TIME FOR PROCESS "+str(i+1)+" : "))
    os.system('cls')
    #///////////////////\\\0\\\\\\\\///1\\\\\\2=startexecution time\\\\3=temination time
    r_queue["p"+str(i)]=[arrival_time,bus_time,0,0,bus_time]
    loading()
    os.system('cls')
r_queue=OrderedDict(sorted(r_queue.items(),key=itemgetter(1)));

#////////////////////////////////////////////////////////////////////////////////////////////////////////
for k in r_queue:
    chk=True                                                                                    
    while(r_queue[k][1]!=0):
        #if cpu is idle
        if (r_queue[k][0]>totaltime):
            while True:
                inc_time()
                if r_queue[k][0]==totaltime:
                    break;
        else:
            if  r_queue[k][2]==0 and chk==True:
                r_queue[k][2]=totaltime
                chk=False
            inc_time(k)
        
printtime()