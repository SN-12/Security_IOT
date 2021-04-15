
from RandomGenerators.LCG import LCG
from RapidExpo import RapidExpo


class Primes:

    def obtain_prime_numbers(start, end):
            prime_numbers = []
            for i in range(start, end):
                isPrime = True
                for numb in range(2,int(i/2)):
                    if i%numb==0:
                        isPrime = False
                if isPrime:
                    prime_numbers.append(i)
            return prime_numbers

  #  list of prime numbers less than n
    def eratosthene(n):
        L = range(2,n+1)
        nb_Primes = []
        while L:
            nb_Primes.append(L[0])
            L = [x for x in L if x%L[0]!=0]
        return nb_Primes

    #     j = 0 , prime = False
#     while j <= 8:
#         for i in range(1,10):
#             n = i*10 + j
#             print(n)
#             a = random.randint(2, n-1)
#             if (pow(a,n)-1)%n==1:
#                 return True
#         j += 2
#     return prime


    def FermatTest(n):
        if n%2 == 0:
            return False
        lcg = LCG(5)
        rand = lcg.Generator()
        a = next(rand)                    
        if n>9 and ((n%10)%2==0 or n%10==5):
            return False
        return (RapidExpo(a,n)-a)%n == 0   

    #returns True if a is prime
    def RevWitness(self, a, n): 
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


    def Miller_Rabin(n, t=50):
        lcg = LCG(2)
        rand = lcg.Generator()
        
        for _ in range(t):
            #a = random.randint(2, n-1)
            a = 2 + next(rand) % ((n-1)-2+1)  
            if Primes().RevWitness(a, n):
                return True
        return False


