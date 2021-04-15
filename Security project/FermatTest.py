from RandomGenerators.LCG import LCG
from RapidExpo import RapidExpo

def FermatTest(n):
    if n%2 == 0:
        return False
    lcg = LCG(5)
    rand = lcg.Generator()
    a = next(rand)
    if n>9 and ((n%10)%2==0 or n%10==5):
        return False
    return (RapidExpo(a,n)-a)%n == 0