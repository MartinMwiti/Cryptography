from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64

digest = hashes.Hash(hashes.SHA512(), backend=default_backend()) # The higher the SHA the better and more pythsecure
digest.update(b"Python is the best programming language!!")

msg_digest = digest.finalize() 

print('msg_digest: ', len(msg_digest), len(msg_digest)*8)
print('Base64 encoding: ', base64.b64decode(msg_digest + b'=='))
