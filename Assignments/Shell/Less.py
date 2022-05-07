import pydoc

def less(**kwargs):
    params = kwargs['params']
    with open(params, 'r') as f:
        pydoc.pager(f.read())


#if __name__ == "__main__":
#  less("sample.txt")
