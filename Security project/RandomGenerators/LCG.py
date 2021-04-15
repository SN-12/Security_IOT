
class LCG:   
    def __init__(self, seed, a=22695477, c=1, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generator(self):
        x = self.seed
        while True:
            x = (self.a*x  +self.c) % self.m
            yield x

