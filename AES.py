# key must be in 16, 24 or 32 bytes long
# text should be in multipiles of 16 bytes

from Crypto.Cipher import AES
key = b'Sixteen byte key'
plain = b'secrets 16 bytes'
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(plain)
ciphertext.encode('hex')
