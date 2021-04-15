import math
from RandomGenerators.BBS import BBS

class BlumGoldwasser:

    def __init__(self):
        self.bbs=BBS(50,450,550)
        self.p=self.bbs.p
        self.q=self.bbs.q
        self.n=self.p*self.q
        self.h=math.ceil(math.log(math.log(self.n,2),2))
        self.generateKey()
    
    def generateKey(self):
        self.n=self.p*self.q
        self.public=self.n
        self.private=(self.p,self.q)
        return (self.public,self.private)

    def encrypt(self,M):
        h=self.h      
        if(len(M)%h)==0:
            self.t=int(len(M)/h)
        else:
            self.t=int(len(M)/h)+1
        t=self.t
        self.r=(next(self.bbs.generator()))%self.n
        x0=(self.r**2)%self.n
        print('\nX0 in encryption : ',x0)
        xi=x0
        c=''
        for i in range(t):
            mi=M[i*h:(i+1)*h]
            xi=(xi**2) % self.n
            xi_binary=bin(xi)
            pi=xi_binary[-h:]

            # convert to binary 
            mi_int=int(mi,2) 
            pi_int=int(pi,2) 

            ci=pi_int ^ mi_int
            ci_binary=format(ci,'0'+ str(h) + 'b')
            c+=ci_binary 
        xt=(xi**2)%self.n
        return c,xt
    
    def decrypt(self,c,x):
        h=self.h
        t=self.t
        # print(t)
        dp = (((self.p + 1) / 4)**(t + 1)) % (self.p - 1)
        dq = (((self.q + 1) / 4)**(t + 1)) % (self.q - 1)
        
        x_dp=x**int(dp)
        x_dq=x**int(dq)
       
        up = x_dp % self.p
        uq = (x_dq) % self.q

        rp=self.bezout(self.p,self.q)[1]
        rq=self.bezout(self.p,self.q)[2]

        x0 = (uq*rp*self.p + up*rq*self.q) % self.n
        print('\nX0 in decryption : ',x0)

        xi = x0
        m = ''
        for i in range(t):
            ci = c[i*h:(i + 1)*h]
            xi = (xi**2) % self.n
            binary_xi=bin(int(xi))
            pi=binary_xi[-h:]
            ci_int=int(ci,2)
            pi_int=int(pi,2)

            mi=ci_int ^ pi_int
            binary_mi=format(mi,'0' + str(h) + 'b')
            m+=binary_mi
        return m

 def bezout(self, a, b):
        if b == 0:
            return (a, 1, 0)
        (r, u, v) = self.bezout(b, a%b)
        return (r, v, u-(a//b)*v)
        
