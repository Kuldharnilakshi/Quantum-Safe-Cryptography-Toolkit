"""
Key generation wrappers for classical and prototype post-quantum algorithms.
This file provides simple APIs:
- generate_rsa_keypair()
- generate_aes_key()
- generate_kyber_keypair() # prototype wrapper
- generate_dilithium_keypair() # prototype wrapper


Replace Kyber/Dilithium prototypes with real library calls when available.
"""


from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import json
import base64




def generate_rsa_keypair(key_size=2048):
key = RSA.generate(key_size)
private_pem = key.export_key().decode()
public_pem = key.publickey().export_key().decode()
return {"private": private_pem, "public": public_pem}




def generate_aes_key(size=32):
# size in bytes (32 -> AES-256)
return get_random_bytes(size)




# Prototype PQC keygen functions (placeholders)
# In production use: liboqs, pqcrypto, or other vetted implementation


def generate_kyber_keypair(prototype_param="kyber512"):
# Return mock keys and metadata to illustrate structure
public = base64.b64encode(os.urandom(64)).decode()
private = base64.b64encode(os.urandom(192)).decode()
return {"scheme": "KYBER", "param": prototype_param, "public": public, "private": private}




def generate_dilithium_keypair(prototype_param="dilithium2"):
public = base64.b64encode(os.urandom(64)).decode()
private = base64.b64encode(os.urandom(256)).decode()
return {"scheme": "DILITHIUM", "param": prototype_param, "public": public, "private": private}




if __name__ == "__main__":
print(json.dumps(generate_rsa_keypair(), indent=2))