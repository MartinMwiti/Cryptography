from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"Python is the best programming language!!")
digest.update(b"Python is the best programming Language!!")

msg_digest = digest.finalize()  # digest of the above two lines

# multiply by 8 to convert from bytes to bits
print('msg_digest: ', len(msg_digest), len(msg_digest)*8)
print('Base64 encoding: ', base64.b64decode(msg_digest + b'='))
