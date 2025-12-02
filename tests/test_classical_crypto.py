"""
test_classical_crypto.py
Tests for RSA & AES classical cryptography implementations.
"""

from src.classical_crypto import ClassicalCrypto


def test_rsa_keygen():
    cc = ClassicalCrypto()
    pub, priv = cc.generate_rsa_keys()

    assert pub is not None
    assert priv is not None


def test_aes_encrypt_decrypt():
    cc = ClassicalCrypto()
    key = cc.generate_aes_key()

    msg = b"classical-encryption"
    ciphertext = cc.aes_encrypt(key, msg)
    plaintext = cc.aes_decrypt(key, ciphertext)

    assert plaintext == msg
