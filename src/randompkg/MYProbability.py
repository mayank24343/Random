from . import MYRandom
import math

def uniform(a,b):
    return a + MYRandom.random()*(b-a)

def uniformSeq(length,a,b):
    res = []
    for i in range(length):
        res.append(uniform(a,b))
    return res

def bernoulli(p=0.5):
    return int(MYRandom.random() <= p)

def bernoulliseq(length,p=0.5):
    res = []
    for i in range(length):
        res.append(bernoulli(p))
    return res

def binomial(n,p):
    res = 0
    for i in range(n):
        res += bernoulli(p)
    return res 

def binomialSeq(length,n,p):
    res = []
    for i in range(length):
        res.append(binomial(n,p))
    return res 

def geometric(p):
    res = 0
    while (not(bernoulli(p))):
        res+=1
    return res

def geometricSeq(length,p):
    res = []
    for i in range(length):
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

def pascalSeq(length,n,p):
    res = []
    for i in range(length):
        res.append(pascal(n,p))
    return res 

def poisson(alpha,n=2**16):
    p = alpha/n 
    res = binomial(n,p)
    return res

def poissonSeq(length,alpha,n=2**16):
    res = []
    for i in range(length):
        res.append(poisson(alpha,n))
    return res

def gaussian(mean = 0,var = 1):
    standard_dev = math.sqrt(var)
    u1 = MYRandom.random()
    u2 = MYRandom.random()
    z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    return mean+standard_dev*z

def gaussianSeq(length, mean = 0, var = 1):
    res = []
    for i in range(length):
        res.append(gaussian(mean,var))
    return res

def exponential(lam):
    p = MYRandom.random()
    return math.log(p)/lam

def exponentialSeq(length,lam):
    res = []
    for i in range(length):
        res.append(exponential(lam))
    return res
