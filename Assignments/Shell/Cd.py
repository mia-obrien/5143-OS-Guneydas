import os
from os.path import expanduser

def cd(**kwargs):
  params = kwargs.get("params", " ")

  if not params:
    params = "~"
  

  #print(params)
  
  if '~' in params:
    params = params.replace('~', expanduser('~'))
    os.chdir(params)
      

    
  elif '..' in params:
    os.chdir(os.path.dirname(os.getcwd()))
      
  elif params:
    os.chdir(params)
  print('in ' + os.getcwd())



#if __name__ == "__main__":
#cd  cd(params = "/home/runner/WonderfulSpotlessRecords/GeeksForGeeks/test")
