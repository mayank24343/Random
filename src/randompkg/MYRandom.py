from . import MYpRNG 
modulo = MYpRNG.getModulo()

def random():
    return MYpRNG.pRNG()/modulo

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