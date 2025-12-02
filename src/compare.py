"""
Utilities to compare key sizes and timing for classical vs PQC prototypes.
"""
import time
import sys
import json
from .keygen import generate_rsa_keypair, generate_kyber_keypair, generate_dilithium_keypair




def measure_key_sizes():
rsa = generate_rsa_keypair()
kyber = generate_kyber_keypair()
dil = generate_dilithium_keypair()


sizes = {
"RSA_public_bytes": len(rsa["public"].encode()),
"RSA_private_bytes": len(rsa["private"].encode()),
"KYBER_public_bytes": len(kyber["public"].encode()),
"KYBER_private_bytes": len(kyber["private"].encode()),
"DILITHIUM_public_bytes": len(dil["public"].encode()),
"DILITHIUM_private_bytes": len(dil["private"].encode()),
}
return sizes




def measure_kem_encapsulate_time(iterations=100):
# Prototype timing using mock ops
start = time.time()
for _ in range(iterations):
_ = generate_kyber_keypair()
end = time.time()
return {"kyber_keygen_seconds": end - start}




if __name__ == "__main__":
print(json.dumps(measure_key_sizes(), indent=2))