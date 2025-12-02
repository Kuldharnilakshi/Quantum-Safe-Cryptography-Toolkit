"""
conftest.py
Shared pytest fixtures for the entire test suite.
"""

import pytest
from src.kyber import Kyber
from src.dilithium import Dilithium
from src.classical_crypto import ClassicalCrypto


@pytest.fixture
def kyber():
    return Kyber()


@pytest.fixture
def dilithium():
    return Dilithium()


@pytest.fixture
def classical():
    return ClassicalCrypto()
