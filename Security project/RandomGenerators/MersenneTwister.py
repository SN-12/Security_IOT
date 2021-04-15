
class MersenneTwister(object):  
    def __init__(self, seed = 5489): #default seed =5489
        self.w=32 #32-bit word length
        self.n=624 #degree of recurrence
        self.MT = [0]*624
        self.f = 1812433253 #constant parameter to the generator
        self.m = 397
        # u , s , t , l are four shifts
        self.u = 11
        self.s = 7
        self.t = 15
        self.l = 18
        self.a= 0x9908b0df #coefficients of the rational normal form twist matrix
        self.b = 0x9D2C5680 #hexadecimal
        self.c = 0xEFC60000 #hexadecimal
        self.d=0xFFFFFFFF #the bitwise & with d in that case has no effect.
        self.index = 624
        self.lower_mask = (1<<31)-1
        self.upper_mask = 1<<31

        #array to store the state of the generator
        #initialize the generator from a seed
        self.MT[0] = seed
        for i in range(1,624):
            self.MT[i] = self.int_32(self.f*(self.MT[i-1]^(self.MT[i-1]>>self.w-2)) + i)
 
    def generator(self):   
        if self.index >= self.n:
            self.twist()
        while True:
            y = self.MT[self.index]
            y = y^(y>>self.u)
            y = y^((y<<self.s)&self.b)
            y = y^((y<<self.t)&self.c)
            y = y^(y>>self.l)
            self.index+=1
            yield (y) #return lowest w bits of y

    #generate the next n values from the series x_i
    def twist(self):
        for i in range(624):
            x = self.int_32((self.MT[i]&self.upper_mask)+(self.MT[(i+1)%self.n]&self.lower_mask))
            xA = x>>1
            if x%2 != 0: #lowest bit of x is 1
                xA = xA^self.a
            self.MT[i] = self.MT[(i+self.m)%self.n]^xA
        self.index = 0

    def int_32(self, number):
        return int(0xFFFFFFFF & number)

if __name__ == "__main__":
    mersenne_twister = MersenneTwister()
    generator=mersenne_twister.generator()
    for i in range(10):
        print(next(generator))