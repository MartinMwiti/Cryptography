# key must be in 16, 24 or 32 bytes long
# plaintext should be in multipiles of 16 bytes


'''
A cipher object is stateful: once you have decrypted a message
    you cannot decrypt (or encrypt) another message with the same
    object.
'''

from Crypto.Cipher import AES
'''
key = b'Sixteen byte key'
data = b'hello from other side'

e_cipher = AES.new(key, AES.MODE_EAX)
e_data = e_cipher.encrypt(data)

# You need to create a new cipher object after encryption to do the decryption.
d_cipher = AES.new(key, AES.MODE_EAX, e_cipher.nonce)
d_data = d_cipher.decrypt(e_data)

print("Encryption was: ", e_data)
print("Original Message was: ", d_data)
'''

def paddedKey(key):
    while len(key) % 8 != 0:  # checks remainder # add blank spaces till the key becomes divisible by 8 i.e remainder = 0
        key += '' * (8 - len(key) % 8)
    return key

def paddedText(text):
    while len(text) % 16 != 0:
        text += '' * (16 - len(text) % 16)
    return text


# plain_input = input('Enter in the text to be encrypted: ')
# plain = paddedText(plain_input)

# key_input = input('Enter in a key between 16 and 32 characters: ')
# key = paddedKey(key_input)

# cipher = AES.new(key, AES.MODE_GCM)
# ciphertext = cipher.encrpt(plain)
# print(ciphertext)


# def encryting_text():
#     key_input = input('Enter in a key between 16 and 32 characters: ')
#     key = paddedKey(key_input)
#     length = len(key_input)
#     while (length< 16 | length> 32):
#         print("Key needs to be between 16 characters and 32 characters")
#         key_input = input('Enter in a key between 16 and 32 characters: ')
#         length = len(key_input)       
#         if length== 16:
#             key = paddedKey(key_input)
#             break
               
#     return key

# key = encryting_text()
# print(key)


# cipher = AES.new(key, AES.MODE_EAX)
# ciphertext = cipher.encrpt(plain)
# print(ciphertext)

# # Decrypt
# d_cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
# d_data = d_cipher.decrypt(ciphertext)
# print(d_data)


# REFERENCE
https: // www.novixys.com/blog/using-aes-encryption-decryption-python-pycrypto/
