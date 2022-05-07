import os

def grep(**kwargs):
  
  params = kwargs.get('params',None)
  flags = kwargs.get('flags',None)

  if "-" in flags:
    params.insert(0,flags)
  print(params)
  print(flags)
  
  if params[0]=='-l' :
    with open(params[2], "r") as f: #params[0]:-l params[1]:keyword params[2]:fileName
      lines = f.read().splitlines()
    for line in lines:
      if params[1] in line:
        print(params[2])

  #if(params[1]!='-l'):
  else:
    with open(params[1], "r") as f: #params[0]:keyword params[1]:fileName
      lines = f.read().splitlines()
    linenum = 0
    for line in lines:
      if params[0] in line:
        print(linenum, line)

      linenum += 1
    #print(line)

  #return 9999
