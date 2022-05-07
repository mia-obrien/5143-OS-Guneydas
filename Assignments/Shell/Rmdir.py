
#Usage: rmdir folderNamesor

import shutil

def rmdir(**kwargs):
  params = kwargs.get("params", None)
  #params = params[0]
  shutil.rmtree(params)
  print("\n")
  return params + ' successfully removed'
