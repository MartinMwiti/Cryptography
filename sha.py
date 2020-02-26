'''
The hashlib module defines an API for accessing different cryptographic hashing algorithms. To work with a specific hash algorithm, use the appropriate constructor function or new() to create a hash object. 
'''

import hashlib

md5 = hashlib.md5()
print(type(md5))
md5.update(b'Python')
print(md5.digest())

print(md5.hexdigest())  # show in hex - containing only hexadecimal digits

sha = hashlib.sha1(b'Python').hexdigest()
print(sha)


