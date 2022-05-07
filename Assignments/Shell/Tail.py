
import linecache

#import sys

def tail(**kwargs):
    params = kwargs["params"]
    flags = kwargs['flags']
    
    #if(len(params))>1:
      #num = int(params[0])
      #out = []
      #tot_lines = len(open(params[1]).readlines())
      #for i in range(tot_lines - num + 1, tot_lines + 1):
          #out.append(linecache.getline(params[1], i))
      #return(''.join(out))

#params[0]:-n
#params[1]:number
#params[2]:fileName

    #print(len(params))
    #print(params[0])
    if(flags == '-n'):
      #print("heyy")
      print("\n")
      num = int(params[0])
      out = []
      tot_lines = len(open(params[1]).readlines())
      for i in range(tot_lines - num + 1, tot_lines + 1):
          out.append(linecache.getline(params[1], i))
      #print(out)
      
      return(''.join(out))

    else:
      #print("hey")
      print("\n")
      num = 3
      out = []
      tot_lines = len(open(params).readlines())
      for i in range(tot_lines - num + 1, tot_lines + 1):
          out.append(linecache.getline(params, i))
      
      return(''.join(out))

#if __name__ == "__main__":
#  tail(params = ["sample.txt", "1"])
