
from random import randint

class ElGamal:

    def __init__(self,p,g):
        
        self.p=p
        self.g=g
        # private key=a
        self.a=randint(0,p-2) 
        #public key=(p, g, A)
        self.A=g**self.a % p   
        self.generateKey()

    def generateKey(self):
        self.publicKey = (self.p,self.g,self.A)
        self.privateKey = self.a
        return (self.publicKey,self.privateKey)

    #receiverPublickey encrypts
    def encrypt(self,msg,receiverPublicKey):
        print('Original Message : ',msg)
        c=(receiverPublicKey**self.a*msg)%self.p
        print('Encrypted Message : ',c,'\n')
        return(c)

    #senderPublicKey decripts  
    def decrypt(self,code,senderPublicKey):
        print('Encrypted Message : ',code)
        org=senderPublicKey**(self.p-1-self.a)*code%self.p
        print('Decrypted Message : ',org)
        return org

 