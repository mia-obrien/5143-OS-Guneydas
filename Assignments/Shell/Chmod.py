import os, sys, stat

def chmod(**kwargs):
  params = kwargs["params"]
  # params = params[0]
  # #this is the first item in the list
  # second = params[1]
  # file = params[2]
  #params = params[0]
  
  
  #print(param)
  #second = kwargs["second"]
 # print(second)


  
  # Allows changes for user
  # if params == "u":

  #   if params == "+":

  #     if params == "r":
  #       os.chmod(file, stat.S_IREAD)
  #       print("User can read file now.")

  #     elif params == "w":
  #       os.chmod(file, stat.S_IWRITE)
  #       print("User can write to file now.")

  #     elif params == "x":
  #       os.chmod(file, stat.S_IEXEC)
  #       print("User can execute file now.")

  #     elif params == "a":
  #       os.chmod(file, stat.S_IRWXU)
  #       print("User can do everything now.")

  #     else:
  #       print("Incorrect Input.")
  
  # # Allows changes for groups
  # elif params == "g":

  #   if params == "+":
           
  #     if params == "r":
  #       os.chmod(file, stat.S_IRGRP)
  #       print("Group can read file now.")

  #     elif params == "w":
  #       os.chmod(file, stat.S_IWGRP)
  #       print("Groups can write to file now.")

  #     elif params == "x":
  #       os.chmod(file, stat.S_IXGRP)
  #       print("Group can execute file now.")

  #     elif params == "a":
  #       os.chmod(file, stat.S_IRWXG)
  #       print("Groups can do everything now.")

  # # Allows changes for others
  # elif params == "o":

  #   if params == '+':

  #     if params == "r":
  #       os.chmod(file, stat.S_IROTH)
  #       print("Others can read file now.")

  #     elif params == "w":
  #       os.chmod(file, stat.S_IWOTH)
  #       print("Others can write to file now.")

  #     elif params == "x":
  #       os.chmod(file, stat.S_IXOTH)
  #       print("Group can execute file now.")

  #     elif params == "a":
  #       os.chmod(file, stat.S_IRWXO)
  #       print("Others can do everything now.")      
      
  if params:
 
    num = params[0]
    num = str(num)
    num = int(num, 8)
  
    os.chmod(params[1], num)

    # Tell the user the file permissions were changed.
    print("File permissions for", params[1], " were changed!")

  return

if __name__=="__main__":
  #-rwxrwxrwx 1 runner runner    0 Feb 12 22:28 test.txt
  #-rw-r--r-- 1 runner runner   47 Feb 14 05:35 sort.txt
  #drwxr-xr-x 1 runner runner    0 Feb 14 19:10  please2

  chmod(param = " " , second = ["777", "sort.txt"])
