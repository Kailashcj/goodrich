#!/bin/python

class CaesarCipher:
  """Class for doing encryption and decryption using caesar cipher technique"""

  def __init__(self, shift):
    """constructor"""
    encoder = [None] * 26 # temp list for encryption
    decoder = [None] * 26 # temp list for decryption
    for k in range(26):
      encoder[k] = chr((k + shift) % 26 + ord('A'))  # ord('A') = 65 + k + shift_number % 26 will give some remainder. that will be added to 65 and a chr is created.
      decoder[k] = chr((k - shift) % 26 + ord('A'))
    self._forward = ''.join(encoder)
    self._backward = ''.join(decoder)

  def encrypt(self, message):
    """return string representing encrypted message"""
    return self._transform(message, self._forward)

  def decrypt(self, secret):
    """return decrypted message given a secret"""
    return self._transform(secret, self._backward)

  def _transform(self, orignal, code):
    """utility to perform transformation based on given code string"""
    msg = list(orignal)
    for k in range(len(msg)):
      if msg[k].isupper():  # notice, the code will only consider upper letter and ignore any punctuations as it is
        j = ord(msg[k]) - ord('A')
        msg[k] = code[j]  # find the element at jth position in the list code and replace in current string.
    return ''.join(msg)    

if __name__=='__main__':
  cipher = CaesarCipher(3)  # constructor call
  message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
  coded = cipher.encrypt(message)
  print('Secret:', coded)
  answer = cipher.decrypt(coded)
  print('Message:', answer)


