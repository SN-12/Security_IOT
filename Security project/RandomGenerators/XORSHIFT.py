
class XORSHIFT:

    def __init__(self,seed, a, b, c):
        self.seed = seed
        self.a = a
        self.b = b
        self.c = c


    def generator(self):
        x = self.seed
        while(True):
            x ^= x >> self.a
            x ^= x << self.b
            x ^ x >> self.c
            yield x

