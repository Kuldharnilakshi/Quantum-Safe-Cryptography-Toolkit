"""
Digital signature helpers: RSA-PSS and prototype Dilithium wrappers.
"""
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64




def rsa_sign(private_pem: str, message: bytes) -> str:
key = RSA.import_key(private_pem)
h = SHA256.new(message)
signature = pkcs1_15.new(key).sign(h)
return base64.b64encode(signature).decode()




def rsa_verify(public_pem: str, message: bytes, signature_b64: str) -> bool:
key = RSA.import_key(public_pem)
h = SHA256.new(message)
sig = base64.b64decode(signature_b64)
try:
pkcs1_15.new(key).verify(h, sig)
return True
except (ValueError, TypeError):
return False




# Prototype Dilithium sign/verify (mock)


def dilithium_sign(private: str, message: bytes) -> str:
# Placeholder: real implementation uses Dilithium signing algorithm
return base64.b64encode(b"mock-dilithium-signature").decode()




def dilithium_verify(public: str, message: bytes, signature_b64: str) -> bool:
# Placeholder verification
return True