import os

def wc(**kwargs):
  params = kwargs.get("params", None)
  #flags = kwargs.get("flags", None)
  #params = params[0]
  with open(params) as f:
    data = f.read()
    lines = 0
    words = 0
    chars = 0
    
    
    lineArray = data.split("\n")
    #print(lineArray)

    lines = len(lineArray)

    #if flags == '-l':
      #print("\n")
      #print(lines, params)
      
    for line in lineArray:
      chars += len(line)
      words += len(line.split())
    print("\n")
    print(lines, words, chars,params)
  
    #return (lines,words,chars)
    
  
def unique(input):
  wordDict = {}

  lineArray = input.split("\n")

  for line in lineArray:
    words = line.split()
    for word in words:
      if not word in wordDict:
        wordDict[word] = 0
      wordDict[word] += 1
    
  return wordDict

#if __name__ == "__main__":
  # with open("next.txt") as f:
  #   data = f.read()
  #wc(params = ["sort.txt"])

  #print(wc(data))
