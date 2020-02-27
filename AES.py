# key must be in 16, 24 or 32 bytes long
# plaintext should be in multipiles of 16 bytes

from Crypto.Cipher import AES

from Crypto.Cipher import AES

key = b'Sixteen byte key'
data = b'hello from other side'

e_cipher = AES.new(key, AES.MODE_OCB)
e_data = e_cipher.encrypt(data)

# You need to create a new cipher object after encryption to do the decryption.
d_cipher = AES.new(key, AES.MODE_OCB, e_cipher.nonce)
d_data = d_cipher.decrypt(e_data)

print("Encryption was: ", e_data)
print("Original Message was: ", d_data)
