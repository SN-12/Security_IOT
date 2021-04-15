
import random

class OneTimePad:

  def __init__(self):
    self.message = []


  def Encryption(self):
    encoded_message = []
    for i in range(len(self.message)):
      encoded_message.append(self.message[i] ^ self.key[i])
    return encoded_message

  def Decryption(self):
    decoded_message = []
    for i in range(len(self.message)):
      decoded_message.append(self.message[i] ^ self.key[i])
    return decoded_message

  def pseudorandom(self, n):
    self.key = [0] * n 
    self.key[0] = 1
    for i in range(1, n):
      self.key[i] = random.randrange(2)
    print("The key is:\t\t  " + str(self.key))
    return self.key

if __name__ == "__main__":
  MyMessage = (0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1)
  print("The message to be incoded:" + str(MyMessage))
  onetimepad = OneTimePad()
  onetimepad.message = MyMessage
  n = len(MyMessage)
  key = onetimepad.pseudorandom(n)
  enc = onetimepad.Encryption()
  print("The encoded message is:\t  " + str(enc))

