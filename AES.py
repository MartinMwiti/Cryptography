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
    while len(key) % 8 != 0: #checks remainder 
        key +='' # add blank spaces till the key becomes divisible by 8 i.e remainder = 0
    return key

def paddedText(text):
    while len(text) % 16 != 0:
        text += ''  # add blank spaces till the text becomes divisible by 16 i.e remainder = 0
    return text

plain_input = input('Enter in the text to be encrypted: ')
plain = paddedText(plain_input)

key_input = input('Enter in a key between 16 and 32 characters: ')
key = paddedKey(key_input)

if (len(key_input) < 16 | len(key_input) > 32):
    print("key must be between 16 and 32")

cipher = AES.new(key)
ciphertext = cipher.encrpt(plain)
print(ciphertext)



