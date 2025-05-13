#Setup
import math
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

#Random Module Functions 

def random():
    return pRNG()/modulo

def randrange(a,b = None,step=1):
    if b == None:
        return int(random()*a/step)*step
    else:
        return a+int(random()*(b-a)/step)*step

def randint(start,stop):
    return start+int(random()*(stop-start+1))

def choice(seq, n = 1, replacement = True):
    seq_length = len(seq)

    if seq_length > 0:
        if (n == 1):
            return seq[randrange(0,seq_length)]
        
        elif n>1 and replacement == True:
            res = []
            for i in range(n):
                res.append(seq[randrange(0,seq_length)])
            return res

        elif n>1 and replacement == False:
            res = []
            if (n <= seq_length):
                for i in range(n):
                    ind  = randrange(0,seq_length)
                    res.append(seq[ind])

                    
                    seq[seq_length-1], seq[ind] = seq[ind], seq[seq_length-1]
                    seq_length -= 1
                return res

    return None 

def shuffle(seq):
    seq_length = len(seq)
    for i in range(seq_length-1,0,-1):
        j = randrange(0,i)
        seq[i],seq[j] = seq[j],seq[i]
    return seq

def shufflestring(string):
    str_length = len(string)
    str_list = list(string)
    shuffle(str_list)
    string = ''.join(str_list)
    return string

#PMFs

def uniform(a,b):
    return a + random()*(b-a)

def uniformseq(a,b,n):
    res = []
    for i in range(n):
        res.append(uniform(a,b))
    return res

def bernoulli(p=0.5):
    return int(random() <= p)

def bernoulliseq(n,p=0.5):
    res = []
    for i in range(n):
        res.append(bernoulli(p))
    return res

def binomial(n,p):
    res = 0
    for i in range(n):
        res += bernoulli(p)
    return res 

def binomialseq(n,p,length):
    res = []
    for i in range(length):
        res.append(binomial(n,p))
    return res 

def geometric(p):
    res = 0
    while (not(bernoulli(p))):
        res+=1
    return res

def geometricseq(p,n):
    res = []
    for i in range(n):
        res.append(geometric(p))
    return res 

def pascal(n,p):
    res = 0
    cnt = 0
    while (cnt < n):
        if (bernoulli(p)):
            cnt+=1
        res+=1
    return res

def pascalseq(n,p,length):
    res = []
    for i in range(length):
        res.append(pascal(n,p))
    return res 

def poisson(alpha,n=2**16):
    p = alpha/n 
    res = binomial(n,p)
    return res

def gaussian(mean = 0,var = 1):
    standard_dev = math.sqrt(var)
    u1 = random()
    u2 = random()
    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mean+standard_dev*z

def exponential(lam):
    p = random()
    return math.log(p)/lam