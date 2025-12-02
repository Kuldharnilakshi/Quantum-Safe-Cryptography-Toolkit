"""
exceptions.py
Custom exception classes for the Quantum-Safe Cryptography Toolkit.
"""


class CryptoError(Exception):
    """General cryptography error."""
    pass


class KeyGenerationError(CryptoError):
    """Raised when key generation fails."""
    pass


class EncryptionError(CryptoError):
    """Raised when encryption fails."""
    pass


class DecryptionError(CryptoError):
    """Raised when decryption fails."""
    pass


class SignatureError(CryptoError):
    """Raised when signing fails."""
    pass


class VerificationError(CryptoError):
    """Raised when signature verification fails."""
    pass
