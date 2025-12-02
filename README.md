# Quantum-Safe Cryptography Toolkit


Prototype toolkit demonstrating classical vs post-quantum cryptography (Kyber, Dilithium) in Python.


**Contents**
- `src/` — implementation modules (key generation, encryption, signing, comparison)
- `examples/` — small demo scripts
- `tests/` — performance and correctness tests
- `docs/` — usage and design notes


## Features
- Key generation for classical (RSA) and PQC (Kyber, Dilithium) — prototype implementations/wrappers
- Encryption (symmetric + hybrid) and digital signatures
- Performance comparison scripts measuring key sizes, encryption/decryption speed
- Clear, commented code suitable for demonstration to NCCU COE reviewers


## Quickstart
1. Create a Python virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate on Windows
pip install -r requirements.txt