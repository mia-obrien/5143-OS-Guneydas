import os

def who():
    print(os.popen('who').read()) 
