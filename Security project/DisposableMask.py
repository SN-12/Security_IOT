from RandomGenerators.LCG import LCG
from RandomGenerators.XORSHIFT import XORSHIFT
from RandomGenerators.BBS import BBS
from RandomGenerators.LFSR import LFSR
from RandomGenerators.MersenneTwister import MersenneTwister


class DisposableMask():

    def __init__(self, msgLen, generator: str, seed: any, *key):
        self.generatorType = generator
        self.msgLen = msgLen
        if generator == 'lcg' and len(key) == 3:
            lcg = LCG(seed, key[0], key[1], key[2])
            self.generator = lcg.Generator()
        elif generator == 'xorshift' and len(key) == 3:
            xorshift = XORSHIFT(seed, key[0], key[1], key[2])
            self.generator = xorshift.Generator()
        elif generator == 'bbs' and len(key) == 2:
            bbs = BBS(seed, key[0], key[1])
            self.generator = bbs.Generator()
        elif generator == 'lfsr' and len(key) == 1:
            lfsr = LFSR(seed, key[0])
            self.generator = lfsr.generator()
        elif generator == 'mersenneTwister' and len(key) == 0:
            mt = MersenneTwister(seed)
            self.generator = mt.generator()
        else:
            raise Exception('arguments error')

    def generateMask(self):
        mask = next(self.generator)
        mask = bin(mask)[2:]
        while self.msgLen > len(mask):
            mask += bin(next(self.generator))[2:]
        mask = mask[-self.msgLen:]
        return mask

    def encrypt(self, msg):
        gen = self.generateMask()
        crypt = ''
        for i in range(0, len(msg)):
            crypt += str(int(msg[i]) ^ int(gen[i]))
        return gen, crypt

    def decrypt(self, gen, crypt):
        msg = ''
        for i in range(0, len(crypt)):
            msg += str(int(crypt[i]) ^ int(gen[i]))
        return msg


if __name__ == "__main__":

    mj = DisposableMask(5, 'mersenneTwister', 5)
    print('using MersenneTwister Generator')

    gen, crypt = mj.encrypt('00111')
    msg = mj.decrypt(gen, crypt)
    print('orginal: 00111')
    print('encrypted:', crypt)
    print('mask:', gen)
    print('decrypted:', msg)
    print("\n")
    gen, crypt = mj.encrypt('10101')
    msg = mj.decrypt(gen, crypt)
    print('orginal: 10101')
    print('encrypted:', crypt)
    print('mask:', gen)
    print('decrypted:', msg)
    print()
    gen, crypt = mj.encrypt('11111')
    msg = mj.decrypt(gen, crypt)
    print('orginal: 11111')
    print('encrypted:', crypt)
    print('mask:', gen)
    print('decrypted:', msg)