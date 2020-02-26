'''
The hashlib module defines an API for accessing different cryptographic hashing algorithms. To work with a specific hash algorithm, use the appropriate constructor function or new() to create a hash object. 
'''

import hashlib

'''
md5 = hashlib.md5()
print(type(md5))
md5.update(b'Python')
print(md5.digest())

print(md5.hexdigest())  # show in hex - containing only hexadecimal digits

sha = hashlib.sha1(b'Python').hexdigest()
print(sha)



# View all available algo in the my system
print(hashlib.algorithms_available) 
# view all available in the hashlib module
print(hashlib.algorithms_guaranteed)

# passed object should be in byte form
hashed_string = hashlib.sha224(b'Hello World!')
hex_digest = hashed_string.hexdigest()
print(hex_digest)

digest = hashed_string.digest()
print(digest)


hashed_string2 = hashlib.sha256(b'Hello World!')
hex_digest = hashed_string2.hexdigest()
print(hex_digest)

hashed_string3 = hashlib.sha512(b'Hello World!')
hex_digest = hashed_string3.hexdigest()
print(hex_digest)
'''
'''
# md5 accept object in byte
hash = hashlib.md5(b'Hello Python!!!')
hash
print(hash.hexdigest())
print(hash.block_size)
print(hash.digest_size)

hash1 = hashlib.sha256(b'Hello Python!!!')
hash
print(hash1.hexdigest())
print(hash1.block_size)
print(hash1.digest_size)
'''

# DSA HASHING ALGORITHM
# print(hashlib.algorithms_available)
# hash = hashlib.new('DSA')
# hash.update(b'Python is the best')
# print(hash.hexdigest())


# SHAKE algorithm
hash = hashlib.shake_256(b'Hello World!')
# Getting specific length you want
print(hash.digest(10))
print(hash.hexdigest(10))

hash2 = hashlib.shake_128(b'Hello World!')
# Getting specific length you want
print(hash2.digest(10))
print(hash2.hexdigest(20))
