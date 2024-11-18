# Encryption Tool

## Description

This Python script provides a comprehensive suite for encrypting and decrypting data using a variety of cryptographic algorithms. The tool is designed to help users learn and experiment with different encryption methods, including both **symmetric** and **asymmetric** cryptography.

### Supported Algorithms
The tool includes the following cryptographic algorithms:
- **AES (Advanced Encryption Standard)**: A symmetric encryption algorithm widely used for securing data.
- **RSA (Rivest-Shamir-Adleman)**: An asymmetric algorithm used for encryption and digital signatures.
- **Blowfish**: A symmetric block cipher that can be used for encryption.
- **DES (Data Encryption Standard)**: A symmetric-key algorithm that was once widely used in cryptography.
- **ChaCha20**: A fast and secure stream cipher.
- **ECC (Elliptic Curve Cryptography)**: A public-key cryptosystem based on elliptic curves, offering strong security with small keys.
- **HMAC (Hash-based Message Authentication Code)**: A mechanism for message integrity and authentication.
- **Post-Quantum Cryptography (Kyber)**: An encryption method designed to be secure against attacks from quantum computers.
- **Hybrid Encryption (AES + RSA)**: Combines the strengths of both AES (for symmetric encryption) and RSA (for asymmetric encryption).
- **Blake3**: A fast cryptographic hash function.

### Key Features:
- **Interactive Command-Line Interface (CLI)**: Choose your encryption algorithm, input data, and see the encryption and decryption results instantly.
- **Flexible Input**: Supports encrypting strings, files, and generating hashes.
- **File Encryption/Decryption**: Encrypt and decrypt entire files with ease.
- **Post-Quantum Encryption**: Implement Kyber, an algorithm designed to be secure against quantum computing threats.
- **Cryptographic Hashing**: Supports hashing with the secure and fast Blake3 algorithm.

### Intended Use:
This tool is designed for educational purposes to help users understand and explore cryptographic techniques. It is **not recommended for production use** in securing sensitive data, as it lacks advanced key management and secure protocols.

### Security Notice:
This tool is for educational purposes only and is provided "as-is" without warranty. The author is not responsible for any damages caused by the use of this tool. Users should not use this tool in real-world applications involving sensitive or private data.

### License:
This project is licensed under the **Absolute License**, which allows for unrestricted usage, modification, and distribution, with the following restrictions:
- Users are responsible for ensuring the secure usage of cryptographic algorithms.
- The author is not responsible for any damage or misuse caused by the tool.

## Installation
To use this tool, simply clone this repository or download the script `encryption_tool.py` to your local machine. Make sure you have Python 3.6 or higher installed.

Install the required dependencies with pip:

