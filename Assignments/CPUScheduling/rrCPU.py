#!/usr/bin/python
import sys
import random
import threading, queue
import time
from datetime import datetime
from time import sleep
import random
import json
import sys,os
from Process import Process 
'''
CPU Scheduling for Round Robin
'''
class RoundRobinCPU:

    def __init__(self,text):
        #We set 4 as a default value
        self.QUANTUM = 4
        self.busy = False
        self.timeLeft = 0
        self.quantum = self.QUANTUM
        self.curProcess = Process(-1,-1,-1,[-1],[-1],-1,False)
        self.name = text
    
    def assignProcess(self,process):
        self.busy = True
        self.curProcess = process
        self.timeLeft = process.CPU_bursts[0]
        self.curProcess.CPU_bursts.pop(0)
        self.quantum = self.QUANTUM

    def clear(self):
        self.busy = False
        self.timeLeft = 0
        self.quantum = self.QUANTUM
        self.curProcess = Process(-1,-1,-1,[-1],[-1],-1,False)

    def preempt(self, prioQ):  
        self.curProcess.CPU_bursts.insert(0,self.timeLeft)
        prioQ.put(self.curProcess)
        self.clear()

    def tick(self):
        #if there is no process
        if(self.curProcess.pID == -1):
            return

        self.timeLeft-=1
        if(self.timeLeft == 0):
            if(len(self.curProcess.IO_bursts)):
                self.curProcess.waiting = True
                self.curProcess.ready = False
            else:
                self.curProcess.ready = False
                self.curProcess.waiting = False
                self.curProcess.done = True
            
            self.busy = False
        
        self.quantum-=1
