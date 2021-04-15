
class LFSR:

    def __init__(self, seed:list, connexion:list):
        self.seed = seed
        self.connexion = connexion

    def generator(self):
        s = self.seed
        while True:
            r=0
            for i in self.connexion:
                r ^= s[i]
            s.insert(0, r)
            s.pop(len(s)-1)
            yield r

