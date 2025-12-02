from setuptools import setup, find_packages

setup(
    name="quantum-safe-crypto-toolkit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "cryptography",
        "numpy"
    ],
    description="A toolkit for classical and post-quantum cryptography.",
    author="Your Name",
    license="MIT",
)
