from RandomGenerators.LCG import LCG


#returns True if a is prime
def RevWitness(a, n): 
    m = n-1
    y = 1
    while(m != 0):
        if m%2 == 1:
            y = (a*y) % n
            m = m - 1
        else:
            b = a
            a = (a*a) % n
            if a == 1 and b != 1 and b != n-1:
                return False
            m = m/2
    if y != 1:
        return False
    else:
        return True


def Miller_Rabin(n, t=100):
    lcg = LCG(2)
    rand = lcg.Generator()
    for _ in range(t):
        #a = random.randint(2, n-1)
        a = 2 + next(rand) % ((n-1)-2+1)  
        if RevWitness(a, n):
            return True
    return False
