import os
import stat
import time
import sys
import pwd, grp


def get_mode_info(mode):

    perms="-"
    link=""

    if stat.S_ISDIR(mode):
        perms="d"
    elif stat.S_ISLNK(mode):
        perms="l"
        link = os.readlink(filename)
        if not os.path.exists(filename):
            pass
    elif stat.S_ISREG(mode):
        if mode & (stat.S_IXGRP|stat.S_IXUSR|stat.S_IXOTH): #bitwise operators
            pass
    mode=stat.S_IMODE(mode)
    for who in "USR", "GRP", "OTH":
        for what in "R", "W", "X":
            #lookup attribute at runtime using getattr
            if mode & getattr(stat,"S_I"+what+who):
                perms=perms+what.lower()
            else:
                perms=perms+"-"
    #return multiple bits of info in a tuple
    return (perms, link)


def ls(**kwargs):
  flags = kwargs.get("flags", None)
  #params = params[0]
  

  #cmd = "cat  -lah  main.py  lib1.py  stuff.txt > output"
  #c,r = os.get_terminal_size()
  #parsed = parseCmd(cmd)
  now = int(time.time())
  recent = now - (6*30*24*60*60)

  if flags == '-lah':
    files = os.listdir()
  
    for filename in files:
        try:
          stat_info = os.lstat(filename)
        except:
            sys.stderr.write("%s: No such file or directory\n" % filename)
            continue
        perms, link = get_mode_info(stat_info.st_mode)
        nlink = "%4d" % stat_info.st_nlink
          #print(nlink)
        try:
          name = "%-8s" % pwd.getpwuid(stat_info.st_uid)[0]
            # print(name)
        except KeyError:
            name = "%-8s" % stat_info.st_uid
        try:
            group = "%-8s" % grp.getgrgid(stat_info.st_gid)[0]
              #print(group)
        except KeyError:
            group = "%-8s" % stat_info.st_gid

        size = "%8d" % stat_info.st_size

        ts = stat_info.st_mtime
        if (ts < recent) or (ts > now): #boolean operators
            time_fmt = "%b %e  %Y"
        else:
            time_fmt = "%b %e %R"
        time_str = time.strftime(time_fmt, time.gmtime(ts))

        sys.stdout.write("%s %s %s %s %s %s %s \n" % (perms,nlink,name,group,size,time_str, filename))

  if not flags:
    file = "" + "\n"
    files = os.listdir()
    for filename in files:
      file += filename
    return file

    return ""
    


if __name__ == "__main__":
  ls()
  # cat = ''
  # if :
  #   print("hello")
