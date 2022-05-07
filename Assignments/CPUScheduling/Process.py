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

'''
Process Class
Creates a process queue for every scheduling algorithm
'''
class Process:
    def __init__(self, arrivalTime, pID, priority, cpuBursts, ioBursts, mode, ready):
        #instance variables
        self.arrivalTime = int(arrivalTime)
        self.pID = int(pID)
        self.priority = int(priority)
        self.CPU_bursts = []
        self.IO_bursts = []
        self.mode = int(mode)
        
        #process attributes
        self.ready = ready
        self.waiting = False
        self.done = False
        self.waitTime = 0
        self.burstTime = 0
        self.BT = 0

        for cburst in cpuBursts:
            self.CPU_bursts.append(int(cburst))

        for iburst in ioBursts:
            self.IO_bursts.append(int(iburst))

    #checking the arrival time for the priority queue
    def __gt__(self,other):
        if(self.mode == 0):
            if (self.arrivalTime > other.arrivalTime):
                return True
            elif(self.arrivalTime == other.arrivalTime):
                if(self.pID < other.pID):
                    return True       
            return False
        elif(self.mode == 1):
            if (self.CPU_bursts[0] > other.cpuBursts[0]):
                return True
            elif(self.CPU_bursts[0] == other.cpuBursts[0]):
                if(self.pID < other.pID):
                    return True       
            return False
        elif(self.mode == 2):
            if (self.priority > other.priority):
                return True
            elif(self.priority == other.priority):
                if(self.pID < other.pID):
                    return True       
            return False
        elif(self.mode == 3):
            if (self.CPU_bursts[0] > other.cpuBursts[0]):
                return True
            elif(self.CPU_bursts[0] == other.cpuBursts[0]):
                if(self.pID < other.pID):
                    return True       
            return False
        else:
            return False
   

    def __lt__(self,other):
        if(self.mode == 0):
            if (self.arrivalTime < other.arrivalTime):
                return True
            elif(self.arrivalTime == other.arrivalTime):
                if(self.pID > other.pID):
                    return True
            return False
        elif(self.mode == 1):
            if (self.CPU_bursts[0] < other.CPU_bursts[0]):
                return True
            elif(self.CPU_bursts[0] == other.CPU_bursts[0]):
                if(self.pID > other.pID):
                    return True
            return False
        elif(self.mode == 2):
            if (self.priority < other.priority):
                return True
            elif(self.priority == other.priority):
                if(self.pID > other.pID):
                    return True
            return False
        elif(self.mode == 3):
            if (self.CPU_bursts[0] < other.CPU_bursts[0]):
                return True
            elif(self.CPU_bursts[0] == other.CPU_bursts[0]):
                if(self.pID > other.pID):
                    return True
            return False
        else:
            return False
