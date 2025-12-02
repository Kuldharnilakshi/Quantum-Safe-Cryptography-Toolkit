"""
test_dilithium.py
Unit tests for Dilithium post-quantum signature module.
"""

import pytest
from src.dilithium import Dilithium
from src.exceptions import SignatureError, VerificationError


def test_dilithium_keygen():
    dil = Dilithium()
    pub, priv = dil.generate_keypair()

    assert isinstance(pub, bytes)
    assert isinstance(priv, bytes)


def test_dilithium_sign_and_verify():
    dil = Dilithium()
    pub, priv = dil.generate_keypair()
    message = b"post-quantum-signature"

    signature = dil.sign(priv, message)
    assert dil.verify(pub, message, signature) is True


def test_dilithium_verify_failure():
    dil = Dilithium()
    pub, priv = dil.generate_keypair()
    message = b"hello"
    signature = dil.sign(priv, message)

    with pytest.raises(VerificationError):
        dil.verify(pub, b"tampered", signature)
