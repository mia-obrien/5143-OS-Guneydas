
  #print("params :: ==== :: " ,params)
#py  shutil.move(params[0],params[1])≥ mv "/home/runner/CommonWarlikeWorkplaces/sample.txt" "/home/runner/CommonWarlikeWorkplaces/second.txt"


import shutil

def mv(**kwargs):
  params = kwargs["params"]
  #destination = kwargs["destination"]
  shutil.move(params[0], params[1])
  return "\n"+params[0]+" to " +params[1]+' successfully moved'
  
