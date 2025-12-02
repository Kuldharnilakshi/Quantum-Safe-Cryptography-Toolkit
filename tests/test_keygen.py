"""
test_keygen.py
Tests for unified key generation module.
"""

from src.keygen import generate_all_keys


def test_generate_all_keys():
    keys = generate_all_keys()

    assert "kyber" in keys
    assert "dilithium" in keys
    assert "rsa" in keys

    assert isinstance(keys["kyber"]["public"], bytes)
    assert isinstance(keys["dilithium"]["private"], bytes)
    assert keys["rsa"]["public"] is not None
