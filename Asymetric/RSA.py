import random

class RSA:
    
    def __init__(self, P1, P2): 
        self.P1 = P1
        self.P2 = P2
        self.key()
        print('c: ', self.c)
        print('d:', self.d)
        print('n: ', self.n)

    def key(self):
        n = self.P1 * self.P2
        c = random.randrange(1, (self.P1-1)*(self.P2-1))
        (r, u, _) = self.bezout(c, (self.P1-1)*(self.P2-1))
        while(r != 1):
            c = c+1
            (r,u,_) = self.bezout(c, (self.P1-1)*(self.P2-1))
        self.n = n
        self.c = c
        self.d = u
        if u < 0:
            self.d += (self.P1-1)*(self.P2-1)
        return n, c, u

    def encrypt(self, t):
        res = ((t**self.c))%self.n
        return res
        
    def decrypt(self, x):
        x = x**self.d
        x = int(x % self.n)
        return x

    def bezout(self, a, b):
        if b == 0:
            return (a, 1, 0)
        (r, u, v) = self.bezout(b, a%b)
        return (r, v, u-(a//b)*v)

