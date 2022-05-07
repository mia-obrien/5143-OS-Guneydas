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
IPU Class
IO processing unit functions
'''
class IPU:
    def __init__(self,text):
        self.busy = False
        self.timeLeft = 0
        self.curProcess = Process(-1,-1,-1,[-1],[-1],-1,False)
        self.name = text
    
    def assignProcess(self,process):
        self.busy = True
        self.curProcess = process
        self.timeLeft = process.IO_bursts[0]
        self.curProcess.IO_bursts.pop(0)

    def tick(self):
        #if no process to run
        if(self.curProcess.pID == -1):
            return
          
        self.timeLeft-=1
        if(self.timeLeft == 0):
            if(len(self.curProcess.CPU_bursts)):
                self.curProcess.waiting = False
                self.curProcess.ready = True
            else:
                self.curProcess.ready = False
                self.curProcess.waiting = False
            
            self.busy = False

    def clear(self):
        self.busy = False
        self.timeLeft = 0
        self.curProcess = Process(-1,-1,-1,[-1],[-1],-1,False)
