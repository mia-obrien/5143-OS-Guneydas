import os

def mkdir(**kwargs):
  #new_dir = kwargs["new_dir"]
  params = kwargs["params"]
  #params = params[0]
  #params = str(params)
  parent_dir = os.getcwd()
  
#Path
  path = os.path.join(parent_dir, params)
  
# Create the directory
  os.mkdir(path)
  print("Directory '%s' created" %params)
  #print(params)
