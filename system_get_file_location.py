import os

def get_loc():
    currentDir = os.path.dirname(__file__)
    print(currentDir)
    return currentDir