"""
Encryption helpers: classical hybrid RSA+AES and prototype Kyber-based hybrid.
"""
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64




def rsa_encrypt(public_pem: str, plaintext: bytes) -> dict:
public_key = RSA.import_key(public_pem)
cipher_rsa = PKCS1_OAEP.new(public_key)
# generate ephemeral symmetric key
sym_key = get_random_bytes(32)
ciphertext_sym = aes_encrypt(sym_key, plaintext)
enc_sym = cipher_rsa.encrypt(sym_key)
return {"enc_sym": base64.b64encode(enc_sym).decode(), "ciphertext": ciphertext_sym}




def rsa_decrypt(private_pem: str, enc_sym_b64: str, ciphertext_blob: dict) -> bytes:
private_key = RSA.import_key(private_pem)
cipher_rsa = PKCS1_OAEP.new(private_key)
sym_key = cipher_rsa.decrypt(base64.b64decode(enc_sym_b64))
return aes_decrypt(sym_key, ciphertext_blob)




def aes_encrypt(key: bytes, plaintext: bytes) -> dict:
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ct = cipher.encrypt(pad(plaintext, AES.block_size))
return {"iv": base64.b64encode(iv).decode(), "ct": base64.b64encode(ct).decode()}




def aes_decrypt(key: bytes, ciphertext_blob: dict) -> bytes:
iv = base64.b64decode(ciphertext_blob["iv"])
ct = base64.b64decode(ciphertext_blob["ct"])
cipher = AES.new(key, AES.MODE_CBC, iv)
return unpad(cipher.decrypt(ct), AES.block_size)




# Prototype Kyber hybrid encrypt/decrypt (mock)


def kyber_encrypt(public_key: str, plaintext: bytes) -> dict:
# A real implementation would use the Kyber KEM to encapsulate a symmetric key.
# Here we return a mock structure with a dummy encapsulated key and AES-encrypted payload.
enc_sym = base64.b64encode(get_random_bytes(80)).decode()
sym_key = get_random_bytes(32)
ciphertext = aes_encrypt(sym_key, plaintext)
return {"enc_sym": enc_sym, "ciphertext": ciphertext}




def kyber_decrypt(private_key: str, enc_sym: str, ciphertext_blob: dict) -> bytes:
# Real implementation decapsulates; prototype uses mock key derivation
sym_key = get_random_bytes(32) # THIS IS A PROTOTYPE PLACEHOLDER
return aes_decrypt(sym_key, ciphertext_blob)