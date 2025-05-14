import time 
multiplier = 23
increment = 53
modulo = 29

def auto():
    return time.time()%modulo

seed = auto()
def setSeed(s):
    global seed 
    seed = s

def setMultiplier(mult):
    global multiplier
    multiplier = mult

def setIncrement(inc):
    global increment
    increment = inc

def setModulo(mod):
    global modulo
    modulo = mod

def pRNG():
    global seed
    seed = (seed*multiplier+increment)%modulo
    return seed

def getModulo():
    return modulo