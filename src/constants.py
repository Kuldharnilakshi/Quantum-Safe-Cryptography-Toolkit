"""
constants.py
Global constants and configuration parameters for the toolkit.
"""

# Version info
TOOLKIT_NAME = "Quantum-Safe Cryptography Toolkit"
VERSION = "1.0.0"

# Algorithm identifiers
ALGO_KYBER = "Kyber"
ALGO_DILITHIUM = "Dilithium"
ALGO_RSA = "RSA"
ALGO_AES = "AES"

# Default settings
DEFAULT_KEY_SIZE_RSA = 2048
DEFAULT_AES_KEY_BYTES = 32

# File naming conventions
KEY_DIR = "keys/"
PUBLIC_KEY_SUFFIX = "_pub.key"
PRIVATE_KEY_SUFFIX = "_priv.key"

# Benchmark settings
DEFAULT_BENCHMARK_RUNS = 10
