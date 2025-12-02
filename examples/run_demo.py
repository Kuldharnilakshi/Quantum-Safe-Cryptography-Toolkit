"""
Small demo that generates keys, signs a message, encrypts it, and prints sizes/timings.
"""
from src import keygen, encrypt, sign, compare




def main():
message = b"Hello Learners — quantum-safe demo"


print("Generating classical RSA keypair...")
rsa = keygen.generate_rsa_keypair()


print("Generating prototype Kyber/Dilithium keypairs...")
kyber = keygen.generate_kyber_keypair()
dil = keygen.generate_dilithium_keypair()


print("Signing message with RSA...")
rsa_sig = sign.rsa_sign(rsa["private"], message)
print("RSA signature (base64) sample:", rsa_sig[:60], "...")


print("Encrypting message with RSA hybrid scheme...")
ct = encrypt.rsa_encrypt(rsa["public"], message)
print("Ciphertext sample:", ct["ciphertext"]["ct"][:60], "...")


print("Comparing key sizes...")
sizes = compare.measure_key_sizes()
for k, v in sizes.items():
print(k, ":", v)


if __name__ == "__main__":
main()