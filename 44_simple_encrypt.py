"""Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""

from itertools import zip_longest

def decrypt(encrypted_text, n):
  text = encrypted_text
  
  if n <= 0:
      return text
  
  mid = len(encrypted_text) // 2

  for _ in range(n):
    odd_index = text[:mid]
    even_index = text[mid:]

    even_and_odd_zipped = zip_longest(even_index, odd_index, fillvalue="")
    text = "".join([even + odd for even, odd in even_and_odd_zipped])
    
  return text


def encrypt(text, n):
  ecrypted_text = text
  if n <= 0:
      return ecrypted_text
  
  for _ in range(n):
      odd_index = ecrypted_text[1::2]
      even_index = ecrypted_text[::2]
      ecrypted_text = odd_index + even_index
  
  return ecrypted_text

print(encrypt("This is a test!", 0)) # "This is a test!"
print(encrypt("This is a test!", 1)) # "hsi  etTi sats!"
print(encrypt("This is a test!", 2)) # "s eT ashi tist!"
print("\n***************************\n")
print(decrypt("This is a test!", 0) ) #"This is a test!"
print(decrypt("hsi  etTi sats!", 1) ) #"This is a test!"
print(decrypt("s eT ashi tist!", 2) ) #"This is a test!"
print(decrypt(" Tah itse sits!", 3) ) #"This is a test!"
print(decrypt("This is a test!", 4) ) #"This is a test!"
print(decrypt("This is a test!", -1)) ## "This is a test!"
