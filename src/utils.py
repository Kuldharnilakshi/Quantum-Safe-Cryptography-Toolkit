"""
utils.py
Utility helper functions for encoding, decoding, hashing, and randomness.
"""

import base64
import secrets
import hashlib


def generate_secure_random_bytes(length: int = 32) -> bytes:
    """Generate cryptographically secure random bytes."""
    return secrets.token_bytes(length)


def sha3_hash(data: bytes) -> bytes:
    """Return SHA3-256 hash of the input data."""
    return hashlib.sha3_256(data).digest()


def b64_encode(data: bytes) -> str:
    """Base64 encode bytes to string."""
    return base64.b64encode(data).decode()


def b64_decode(data: str) -> bytes:
    """Base64 decode string into bytes."""
    return base64.b64decode(data)


def compare_bytes(a: bytes, b: bytes) -> bool:
    """Constant-time comparison to avoid timing attacks."""
    return secrets.compare_digest(a, b)
