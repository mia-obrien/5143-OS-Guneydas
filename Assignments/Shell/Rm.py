import os

def rm(**kwargs):
  
  params = kwargs['params']

  dirname = params[0]
  filename = params[1]
  pathname = os.path.abspath(os.path.join(dirname, filename))
  if pathname.startswith(dirname):
    os.remove(pathname)

#rm /home/runner/CommonWarlikeWorkplaces c.txt
