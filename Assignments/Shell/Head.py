from os import path, getcwd

# default is 1

#params[0]:flag
#params[1]:number
#params[2]:fileName
def head(**kwargs):

  params = kwargs['params']
  flags = kwargs['flags']
  #print(params[2])
  
  
  if flags == '-n':
    end = int(params[0])
    with open(params[1], "r") as f:
      lines = f.read().splitlines()
    print("\n")
    for line in lines[:end]:
      print(line)

  else:
    #print("hello")
    end = 3
    with open(params, "r") as f:
      lines = f.read().splitlines()
    print("\n")
    for line in lines[:end]:
      print(line)

#if __name__ == "__main__":
  #head("-n","3","sample.txt","")
 # head()
