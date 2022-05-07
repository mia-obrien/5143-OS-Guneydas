import shutil

def cp(**kwargs):

    params = kwargs['params']
  

    shutil.copyfile(params[0], params[1])
    return "\n"+params[0]+" to " +params[1]+' successfully copied'

#cp "/home/runner/CommonWarlikeWorkplaces/sample.txt" "/home/runner/CommonWarlikeWorkplaces/second.txt"
