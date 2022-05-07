#!/usr/bin/python
import sys
import random
import threading, queue
import rich
import time
from rich.panel import Panel
from datetime import datetime
from time import sleep
from rich.layout import Layout
from rich.live import Live
from rich.table import Table

from CPU import CPU
from IPU import IPU
from rrCPU import RoundRobinCPU

layout = Layout()

layout.split(
    Layout(name="main"),
    Layout(name="footer"))

layout["main"].split_row(
    Layout(name="upLeft"), 
    Layout(name="upRight")
)

layout["footer"].split_row(
    Layout(name="downLeft"), 
    Layout(name="downRight")
)

layout['upLeft'].ratio = 1
layout['upRight'].ratio = 1

def printDetails(termTable):
    runned = termTable
    LWT = runned[0][1]
    SWT = runned[0][1]
    totalWT = 0.0
    turnAroundTime = 0.0
    totalTAT = 0.0
    avWT = 0.0
    avgTAT = 0.0
    totalUse = 0
    avgUse = 0
    tatPercent = 0
    for i in runned:
        turnAroundTime = i[1]+ i[2]
        totalWT = totalWT + int(i[1])
        totalTAT = totalTAT+ turnAroundTime
        newWT = i[1]
        totalUse += i[3]
        if(newWT>LWT):
            LWT = newWT
        elif(newWT<LWT):
            SWT = newWT
           
    avgTAT = totalTAT/ len(runned)
    avWT = totalWT/ len(runned)
    avgUse = totalUse / len(runned)
    tatPercent = ((avgTAT/len(runned))/2)


    table3 = Table(title="Wait Times")
    table3.add_column("Shortest Wait Time", justify="center")
    table3.add_column("Longest Wait Time",justify="center")
    table3.add_column("Average Wait Time",justify="center")
    table3.add_row(str(SWT),str(LWT),str(avWT) , style= "cyan")

    with Live(layout, screen=True, redirect_stderr=False) as live:
        layout["downLeft"].update(table3)
   
    table2 = Table(title="Usage")
    table2.add_column("Average Turnaround Time",justify="center")
    table2.add_column("CPU usage",justify="center")
    table2.add_row(str(avgTAT), str(tatPercent), style= "purple")

    with Live(layout, screen=True, redirect_stderr=False) as live:
        layout["downRight"].update(table2)
        sleep(100)

'''
Prints the processes
'''
class printProcesses:
    def __init__(self,procList):
        self.procList = procList

    def makeTable(self):
        table = Table(title="Current Processes")
        table.add_column("PID", justify="center")
        table.add_column("Job", justify="center")
        table.add_column("Current Status", justify="center")
        
        #listed = list(self.pList)
        if(not len(self.procList) ==0):
            for item in self.procList:
                pidNum = str(item[0])
                location = str(item[1])
                running = str(item[2])
                table.add_row(pidNum,location,running,style="green")

        return table

    def __rich__(self) -> Panel:
        return Panel(self.makeTable())


'''
Prints terminated processes
'''
class printTerm:
    def __init__(self,procList):
        self.procList = procList

    def makeTable(self):
        table3 = Table(title="Done Jobs")
        table3.add_column("Process ID", justify="center")
        table3.add_column("Wait Time",justify="center")
        table3.add_column("Burst Time",justify="center")
        table3.add_column("Turnaround Time",justify="center")

        if(not len(self.procList) ==0):
            for item in self.procList:
                IDNum = str(item[0])
                waitTime = str(item[1])
                burstTime = str(item[2])
                usage = str(item[3])
                turnAroundTime = str(item[1]+item[2])
                table3.add_row(IDNum,waitTime,burstTime,turnAroundTime, style="red")
              
        return table3

    def __rich__(self) -> Panel:
        return Panel(self.makeTable())

processList = []

'''
Scheduler Function
'''    
def Scheduler(prioQ,cpuNum,ipuNum):

    ioQ = queue.PriorityQueue()
    terminated = []
    usage = 0
    cpuList = []
    ipuList = []
    for x in range (cpuNum):
        cpuList.append(CPU("cpu"+str(x)))

    for n in range (ipuNum):
        ipuList.append(IPU("ipu"+str(n)))

 
    while ((not (prioQ.empty())) or (not (ioQ.empty()))):
        for cpu in cpuList:
            if(cpu.busy):
                usage+=1
        
            if((not cpu.busy) and (not (prioQ.empty()))):
                item = prioQ.get()
                cpu.assignProcess(item)
                processList.append((str(item.pID),cpu.name,"Processing"))     
            cpu.tick()
    
            if(cpu.curProcess.waiting):
                ioQ.put(cpu.curProcess)
                processList.append((str(cpu.curProcess.pID),"Wait Queue","Waiting"))
                
                cpu.clear()
                
            elif (cpu.curProcess.done):
                processList.append((str(cpu.curProcess.pID),cpu.name,"CPU Burst Completed"))
                terminated.append((cpu.curProcess.pID, cpu.curProcess.waitTime, cpu.curProcess.BT, usage))
                cpu.clear()
 
        for process in prioQ.queue:
            process.BT+=1
        
        for ipu in ipuList:
            if((not ipu.busy) and (not (ioQ.empty()))):
                item = ioQ.get()
                ipu.assignProcess(item)
                processList.append((str(item.pID),ipu.name,"Processing IO"))

            ipu.tick()

            for process in ioQ.queue:
                process.waitTime+=1

            if(ipu.curProcess.ready):
                processList.append((str(ipu.curProcess.pID),"Ready Queue","Ready for CPU"))
                prioQ.put(ipu.curProcess)
                ipu.curProcess.BT+=1
                processList.append((str(ipu.curProcess.pID),ipu.name,"IO burst completed"))
                ipu.clear()  
        
        P = printProcesses(processList)
        T = printTerm(terminated)

        with Live(layout, screen=True, redirect_stderr=False) as live:
            layout["upLeft"].update(P)
            layout["upRight"].update(T)
            sleep(0.2)
            
    return terminated


'''
Scheduler function for Round Robin
'''    
def RRScheduler(prioQ,cpuNum,ipuNum):

    ioQ = queue.PriorityQueue()
    terminated = []
    usage = 0
    cpuList = []
    ipuList = []

    for x in range (cpuNum):
        cpuList.append(RoundRobinCPU("cpu"+str(x)))

    for n in range (ipuNum):
        ipuList.append(IPU("ipu"+str(n)))
    
    while ((not (prioQ.empty())) or (not (ioQ.empty()))):
        for cpu in cpuList:
            if(cpu.busy):
                usage+=1

            if((not cpu.busy) and (not (prioQ.empty()))):
                item = prioQ.get()
                cpu.assignProcess(item)
                processList.append((str(item.pID),cpu.name,"Processing"))       
            cpu.tick()
           
            if(cpu.curProcess.waiting):
                ioQ.put(cpu.curProcess)
                processList.append((str(cpu.curProcess.pID),"Wait Queue","Waiting"))
                
                cpu.clear()

            #else if the process has terminate
            elif (cpu.curProcess.done):
                processList.append((str(cpu.curProcess.pID),cpu.name,"CPU Burst Completed"))
                terminated.append((cpu.curProcess.pID, cpu.curProcess.waitTime, cpu.curProcess.BT, usage))
                cpu.clear()     

            if(cpu.quantum == 0):
                cpu.preempt(prioQ)

        for process in prioQ.queue:
            process.BT+=1 

        for ipu in ipuList:
            if((not ipu.busy) and (not (ioQ.empty()))):
                item = ioQ.get()
                ipu.assignProcess(item)
                processList.append((str(item.pID),ipu.name,"Processing IO"))

            ipu.tick()

            for process in ioQ.queue:
                process.waitTime+=1
                
            if(ipu.curProcess.ready):
                processList.append((str(ipu.curProcess.pID),"Ready Queue","Ready for CPU"))
                prioQ.put(ipu.curProcess)
                ipu.curProcess.BT+=1
                processList.append((str(ipu.curProcess.pID),ipu.name,"IO burst completed"))
                ipu.clear() 

        P = printProcesses(processList)
        T = printTerm(terminated)

        with Live(layout, screen=True, redirect_stderr=False) as live:
            layout["upLeft"].update(P)
            layout["upRight"].update(T)
            sleep(0.2)
    
    return terminated
