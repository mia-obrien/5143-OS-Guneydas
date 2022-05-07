import Pwd
import Who
import Chmod
import Mkdir
import Copy
import Mv
import Wc
import Ls
import Less
import Cd
import Sort
import Rm
import Tail
import Head
import Rmdir
import Grep
import Exit
import History
import Cat

class CommandHelper(object):
    def __init__(self):
        self.commands = {}
        self.commands["pwd"] = Pwd.pwd
        self.commands["who"] = Who.who
        self.commands["mkdir"] = Mkdir.mkdir
        self.commands["chmod"] = Chmod.chmod
        self.commands["copy"] = Copy.cp
        self.commands["mv"] = Mv.mv
        self.commands["wc"] = Wc.wc
        self.commands["ls"] = Ls.ls
        self.commands["less"] = Less.less
        self.commands["cd"] = Cd.cd
        self.commands["sort"] = Sort.sort
        self.commands["rm"] = Rm.rm
        self.commands["tail"] = Tail.tail
        self.commands["head"] = Head.head
        self.commands["rmdir"] = Rmdir.rmdir
        self.commands["grep"] = Grep.grep
        self.commands["history"] = History.history
        self.commands["cat"] = Cat.cat
        self.commands["exit"] = Exit.exit
        
        #self.commands["ls"] = ls
        #self.commands["exit"] = exit

    def invoke(self, rawCmd):
      dictCmd = self.parseCmd(rawCmd)
      listOfCommands = {}

      #print('invoking with this dict :: ',dictCmd)

      cmd = dictCmd.get("cmd", None)
      params = dictCmd.get("params",None)
      flags = dictCmd.get("flags",None)
      

      #second = kwargs.get("second", None)
      listOfCommands["pwd"] = Pwd.pwd
      listOfCommands["who"] = Who.who
      listOfCommands["mkdir"] = Mkdir.mkdir
      listOfCommands["chmod"] = Chmod.chmod
      listOfCommands["cp"] = Copy.cp
      listOfCommands["mv"] = Mv.mv
      listOfCommands["wc"] = Wc.wc
      listOfCommands["ls"] = Ls.ls
      listOfCommands["less"] = Less.less
      listOfCommands["cd"] = Cd.cd
      listOfCommands["sort"] = Sort.sort
      listOfCommands["tail"] = Tail.tail
      listOfCommands["head"] = Head.head
      listOfCommands["rm"] = Rm.rm
      listOfCommands["rmdir"] = Rmdir.rmdir
      listOfCommands["grep"] = Grep.grep
      listOfCommands["exit"] = Exit.exit
      listOfCommands["history"] = History.history
      listOfCommands["cat"] = Cat.cat

      #print(cmd, params)

      #useCommand = listOfCommands[cmd]
      useCommand = listOfCommands[cmd](params=params,flags=flags)
      #print(useCommand)
      
      return useCommand
    
    # if command not in self.commands:
    #   print("This command doesn't exist!")

    def parseCmd(self,cmd):
      """
        cmd
        flags
        params
        redirect 
      Returns:
        Dictionary with each component
      Example:
        {
          "cmd":"cat",
          "flags":"-fax"
          "params":['main.py','lib1.py',...]
          "redirectType":(">",">>")
          "target":"output"
        }
      """
      newCmd = {}
      redirFlag = False

      # Check for redirect and split on that
      if ">" in cmd:
        redirFlag = True
        redirectType = "new"
        cmd,target = cmd.split('>')
      elif ">>" in cmd:
        redirFlag = True
        redirectType = "concat"
        cmd,target = cmd.split('>>')

      # check for flag character
      cmd = cmd.split()

      # handle the rest 
      
      newCmd["cmd"] = cmd[0]
      if len(cmd) >1:
        newCmd["flags"] = cmd[1]
      if len(cmd) >2:
        newCmd["params"] = cmd[2:]

      if len(cmd) == 2:
        #newCmd['params'].insert(0,newCmd["flags"])
        newCmd['params'] = newCmd ['flags']
        #del newCmd['flags']
      
      if len(cmd) >1 and len(cmd) != 2:
        if not "-" in newCmd["flags"]:
          newCmd['params'].insert(0,newCmd["flags"])
          #newCmd['params'] = newCmd ['flags'] +newCmd['params']
          #del newCmd['flags']

      if redirFlag:
        newCmd["redirectType"] = redirectType
        newCmd["target"] = target.strip()
      return newCmd
