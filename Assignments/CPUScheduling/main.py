#!/usr/bin/python
import random
import threading, queue
import time
from datetime import datetime
from time import sleep
import json
import sys,os
from Process import Process 
from CPU import CPU
from IPU import IPU
from display import *

FCFSQ = queue.PriorityQueue()
SJFQ = queue.PriorityQueue()
PSQ = queue.PriorityQueue()
RRQ = queue.Queue()

def helper():
  print("*********************************************************************")
  print("* Course: CSE 5143 Advanced Operating Systems                       *")
  print("* Project: Project 2                                                *")
  print("* Authors 1: Mihriban Guneydas                                      *")
  print("* Authors 2: Deangelo Brown                                         *")
  print("* Goal : This program is design to simulate how different algorithms*")
  print("*        schedule different processes.                              *")
  print("* Usage: python3 fileName algoName CPUNumber IPUNumber              *")
  print("*        For algoName use 1 for First Come First Serve              *")
  print("*        For algoName use 2 for Shortest Job First                  *")
  print("*        For algoName use 3 for Priority                            *")
  print("*        For algoName use 4 for Round Robin                         *")
  print("* Note: Please don't forget to install rich before(pip install rich)*")
  print("*********************************************************************")
  sleep(7)
'''
Driver code
'''
if __name__ =="__main__":

    helper()
    #Usage
    if len(sys.argv) != 4:
      print("Usage: python3 fileName algoName CPUNumber IPUNumber")
      print("    For algoName use 1 for First Come First Serve")
      print("    For algoName use 2 for Shortest Job First")
      print("    For algoName use 3 for Priority")
      print("    For algoName use 4 for Round Robin")
      sleep(10)
      exit()
      
    algo = sys.argv[1]
    cpuNum = sys.argv[2]
    ipuNum = sys.argv[3]
    
    termin = []

    #parsing
    with open('data.dat') as reader:
        lines = reader.read().splitlines()
    
    for item in lines:
        item = item.split(" ")

        arrivalTime = item[0]
        pID = item[1]
        priority = item[2].split("p")
        priority = priority[1]
        CPU_bursts = item[3::2]
        IO_bursts = item[4::2]
      
        #creating the objects
        fcfsinfo = Process(arrivalTime, pID, priority, CPU_bursts, IO_bursts,0, True)
        sjfinfo = Process(arrivalTime, pID, priority, CPU_bursts, IO_bursts,1, True)
        psinfo = Process(arrivalTime, pID, priority, CPU_bursts, IO_bursts,2, True)
        roundrobininfo = Process(arrivalTime, pID, priority, CPU_bursts, IO_bursts,3, True)
      
        #we are adding objects to the queue
        FCFSQ.put(fcfsinfo)
        SJFQ.put(sjfinfo)
        PSQ.put(psinfo)
        RRQ.put(roundrobininfo)

    #in here we are passing a job to the scheduler
    if int(algo)==1:
        termin = Scheduler(FCFSQ,int(cpuNum),int(ipuNum))
    if int(algo)==2:
        termin = Scheduler(SJFQ,int(cpuNum),int(ipuNum))
    if int(algo)==3:
        termin = Scheduler(PSQ,int(cpuNum),int(ipuNum))
    if int(algo)==4:
        termin = RRScheduler(RRQ,int(cpuNum),int(ipuNum))
          
    printDetails(termin)
