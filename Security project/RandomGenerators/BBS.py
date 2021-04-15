
class BBS:
    def __init__(self, seed, start=100, end=200):
        self.seed = seed
        self.start = start
        self.end = end
        self.getPrimes()
       

    def generate_primes(self, start, end):
        primes = []
        for i in range(start, end):
            isPrime = True
            for num in range(2,int(i/2)):
                if i%num==0:
                    isPrime = False
            if isPrime:
                primes.append(i)
        return primes

   
    def getPrimes(self):
        primes = self.generate_primes(self.start, self.end)
        pq = []
        while len(pq) < 2:
            for prime in primes:
                if prime % 4 == 3:
                    pq.append(prime)
        self.p = pq[0]
        self.q = pq[1]

    def generator(self): 
        M = self.p*self.q
        x = self.seed
        while(True):
            x = (x**2)%M
            yield x 
        
