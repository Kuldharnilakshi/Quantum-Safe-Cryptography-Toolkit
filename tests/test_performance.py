import time
from src import compare




def test_key_size_measurement():
sizes = compare.measure_key_sizes()
assert "RSA_public_bytes" in sizes




def test_kyber_keygen_timing():
t = compare.measure_kem_encapsulate_time(iterations=10)
assert "kyber_keygen_seconds" in t