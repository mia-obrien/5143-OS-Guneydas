import os

def sort(**kwargs):
    read_file =[]
    params = kwargs["params"]
    flags = kwargs.get("flags", None)
    if params: 
       with open(params, "r+") as f:
        read_file = f.read().splitlines()
        read_file.sort()
        print(read_file)
    return

#if __name__ == "__main__":
#pwd  sort(params = "/home/runner/WonderfulSpotlessRecords/sort.txt")
