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
CPU class
Class that determines how an instance of a CPU functions
'''
class CPU:
    def __init__(self,text):
        self.busy = False
        self.timeLeft = 0
        self.curProcess = Process(-1,-1, 1,[-1],[-1],-1,False)
        self.name = text
    
    def assignProcess(self,process):
        self.busy = True
        self.timeLeft = process.CPU_bursts[0]
        self.curProcess = process
        self.curProcess.CPU_bursts.pop(0)


    def tick(self):
        #if any process not to run
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

    def clear(self):
        self.busy = False
        self.timeLeft = 0
        self.curProcess = Process(-1,-1,-1,[-1],[-1],-1,False)
