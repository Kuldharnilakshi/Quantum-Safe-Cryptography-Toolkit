"""
main.py
Entry point for the Quantum-Safe Cryptography Toolkit.
"""

from src.keygen import generate_all_keys
from src.benchmark import measure_time, print_benchmark_result


def main():
    print("\n=== Quantum-Safe Cryptography Toolkit ===")

    # Generate all keys
    keys = generate_all_keys()
    print("Keys generated successfully!")

    # Example: benchmark RSA key generation
    from src.classical_crypto import ClassicalCrypto
    cc = ClassicalCrypto()

    result = measure_time(cc.generate_rsa_keys, repeats=5)
    print_benchmark_result("RSA Key Generation", result)


if __name__ == "__main__":
    main()
