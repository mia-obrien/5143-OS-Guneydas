from os import path


def history(**kwargs):

    redirect = kwargs['params']
    histdic = {}
    count = 1
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "history.log"))
    answer =""
    f= open(filepath,'r')
    print("hello")
    for lines in f:
        histdic[count]=lines
        if(len(redirect) ==0):
            answer = answer + "{}: {}".format(count , lines) +'\n'
        count+=1

    print(answer)
    print(count)
    return answer
