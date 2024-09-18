import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()  

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"Key: {key}")

# Encryption
plain_text = input("Please enter your text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")


#Decryption
cipher_text = input("Please enter your text to encrypt: ")
plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
