"""
test_kyber.py
Unit tests for Kyber post-quantum key exchange module.
"""

import pytest
from src.kyber import Kyber
from src.exceptions import EncryptionError, DecryptionError


def test_kyber_keygen():
    kyber = Kyber()
    pub, priv = kyber.generate_keypair()
    assert isinstance(pub, bytes)
    assert isinstance(priv, bytes)
    assert len(pub) > 0
    assert len(priv) > 0


def test_kyber_encrypt_decrypt():
    kyber = Kyber()
    pub, priv = kyber.generate_keypair()

    message = b"quantum-safe-test"
    ciphertext = kyber.encrypt(pub, message)
    plaintext = kyber.decrypt(priv, ciphertext)

    assert plaintext == message


def test_kyber_decrypt_failure():
    kyber = Kyber()
    _, priv = kyber.generate_keypair()
    bad_ciphertext = b"invalid"

    with pytest.raises(DecryptionError):
        kyber.decrypt(priv, bad_ciphertext)
