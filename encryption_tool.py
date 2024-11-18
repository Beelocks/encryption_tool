"""
=========================================================================
                SECURITY NOTICE AND DISCLAIMER

WARNING: THIS TOOL IS INTENDED FOR EDUCATIONAL PURPOSES ONLY.

The encryption and decryption functions in this tool are provided "as is". 
Use this tool at your own risk. While the tool has been designed to implement 
known cryptographic algorithms, **no warranty or guarantee is provided for 
the security or functionality of this tool**. The author is not responsible 
for any misuse, damage, or unintended consequences resulting from the use of 
this tool.

### Important Security Considerations:
- **Cryptographic Security**: The strength of cryptographic algorithms depends heavily on key management, key size, and the secure handling of encrypted data. Ensure you are using appropriate key management practices when implementing this tool in any real-world scenario.
- **Quantum Computing**: Some encryption algorithms included in this tool may be vulnerable to attacks using quantum computers. Always evaluate the cryptographic algorithms according to your needs and the latest developments in the field of cryptography.
- **Data Sensitivity**: Never use this tool with highly sensitive or private information unless you are fully aware of the potential vulnerabilities in your environment. Additionally, be cautious of using this tool with public or insecure systems.

If you are unsure about the security implications of this tool, consult with a professional cryptographer or security expert.

=========================================================================
                           DISCLAIMER

This tool is intended for **educational purposes only**. The code provided 
is designed to demonstrate and practice encryption/decryption algorithms, 
and to showcase different cryptographic techniques. **It should not be used 
for any illegal, unethical, or malicious activities.**

The author of this tool **does not take responsibility** for any damage, data 
loss, or legal issues that might arise from its use, including but not limited 
to:
- Unauthorized access to data,
- Decryption of data without permission,
- Use in an insecure or untrusted environment,
- The unintended sharing or exposure of sensitive data.

The cryptographic algorithms presented here are **subject to vulnerabilities**, 
and their security could be compromised depending on various factors such as 
the strength of the key, the algorithm's implementation, or the attack vectors 
used by an adversary. Always stay informed about the latest developments in 
cryptography and quantum computing as they relate to security.

By using this tool, you acknowledge and agree to the above **terms** and that 
the **author and contributors are not liable** for any consequences that result 
from the use of the software.

=========================================================================
                           LICENSE

### License: Absolute Ownership and Redistribution Rights

The code provided in `encryption_tool.py` is released under the **Absolute License** 
which grants you full rights to **use**, **modify**, and **distribute** the code 
under the following conditions:

1. **You are free to use, modify, and distribute** this software for both personal 
   and commercial purposes.
2. **You must not hold the author or contributors liable** for any damages, losses, 
   or consequences resulting from the use of this software.
3. **You must include a copy of this license** along with any redistributed or modified 
   versions of this software.
4. **Any modified versions** of this software should be clearly marked as modified to 
   avoid confusion with the original tool.
5. The author retains **all rights to the original code** and can make changes to 
   this license at their discretion. However, this does not affect existing copies 
   that have already been redistributed under the current terms.

The tool comes **without warranty**, express or implied, including but not limited 
to warranties of merchantability or fitness for a particular purpose. The author 
does not guarantee the correctness, reliability, or security of the software.

By using or distributing this software, you agree to the terms of this **Absolute License**.

=========================================================================
"""


from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import Blowfish, DES
from Cryptodome.Cipher import ChaCha20
from ecdsa import SigningKey, NIST384p
import base64
import blake3
import os
import hashlib
import pynacl.secret
import pynacl.utils
from pqcrypto.kem.kyber import encapsulate, decapsulate

# AES (Advanced Encryption Standard)
def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

def aes_decrypt(key, encrypted_data):
    nonce, tag, ciphertext = encrypted_data[:16], encrypted_data[16:32], encrypted_data[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

# RSA (Rivest-Shamir-Adleman)
def rsa_encrypt(public_key, data):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    return encrypted_data

def rsa_decrypt(private_key, encrypted_data):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data

# Blowfish Encryption
def blowfish_encrypt(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_data = data + (8 - len(data) % 8) * chr(8 - len(data) % 8)
    encrypted_data = cipher.encrypt(padded_data.encode('utf-8'))
    return encrypted_data

def blowfish_decrypt(key, encrypted_data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
    padding_length = ord(decrypted_data[-1])
    return decrypted_data[:-padding_length]

# DES (Data Encryption Standard)
def des_encrypt(key, data):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = data + (8 - len(data) % 8) * chr(8 - len(data) % 8)
    encrypted_data = cipher.encrypt(padded_data.encode('utf-8'))
    return encrypted_data

def des_decrypt(key, encrypted_data):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
    padding_length = ord(decrypted_data[-1])
    return decrypted_data[:-padding_length]

# ChaCha20 Encryption
def chacha20_encrypt(key, data):
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(data.encode('utf-8'))
    return cipher.nonce + ciphertext

def chacha20_decrypt(key, encrypted_data):
    nonce, ciphertext = encrypted_data[:8], encrypted_data[8:]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')

# Elliptic Curve Cryptography (ECC) - Signing and Verifying
def ecc_sign(private_key, data):
    sk = SigningKey.from_string(private_key, curve=NIST384p)
    signature = sk.sign(data.encode('utf-8'))
    return signature

def ecc_verify(public_key, signature, data):
    vk = SigningKey.from_string(public_key, curve=NIST384p).get_verifying_key()
    return vk.verify(signature, data.encode('utf-8'))

# HMAC (Hash-based Message Authentication Code)
def hmac_generate(key, message):
    hmac = hashlib.new('sha256', key.encode('utf-8'))
    hmac.update(message.encode('utf-8'))
    return hmac.hexdigest()

# Post-Quantum Cryptography (Kyber)
def post_quantum_kyber_encrypt(data):
    # Encapsulate kunci publik
    public_key, secret_key = encapsulate()
    ciphertext, shared_secret = encapsulate(public_key)
    return ciphertext, shared_secret

def post_quantum_kyber_decrypt(ciphertext, secret_key):
    # Dekapsulasi dengan kunci privat
    shared_secret = decapsulate(ciphertext, secret_key)
    return shared_secret

# Blake3 Hashing
def generate_blake3_hash(data):
    return blake3.blake3(data.encode('utf-8')).hexdigest()

# Hybrid Encryption (AES + RSA)
def hybrid_encrypt(data):
    # Generate RSA key pair
    rsa_key = RSA.generate(2048)
    public_key = rsa_key.publickey()
    private_key = rsa_key

    # Generate random AES key
    aes_key = get_random_bytes(16)

    # Encrypt data with AES
    cipher_aes = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data.encode('utf-8'))

    # Encrypt AES key with RSA
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    return encrypted_aes_key, cipher_aes.nonce, tag, ciphertext, private_key

def hybrid_decrypt(encrypted_aes_key, nonce, tag, ciphertext, private_key):
    # Decrypt AES key with RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Decrypt data with AES
    cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    decrypted_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return decrypted_data.decode('utf-8')

# Enkripsi File
def encrypt_file(filename, key):
    cipher = AES.new(key, AES.MODE_GCM)
    with open(filename, 'rb') as file:
        file_data = file.read()
        ciphertext, tag = cipher.encrypt_and_digest(file_data)

    with open(filename + ".enc", 'wb') as file_enc:
        [ file_enc.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    print(f"File '{filename}' berhasil dienkripsi.")

def decrypt_file(filename, key):
    with open(filename, 'rb') as file_enc:
        nonce, tag, ciphertext = [ file_enc.read(x) for x in (16, 16, -1) ]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

    with open(filename.replace(".enc", ".dec"), 'wb') as file_dec:
        file_dec.write(decrypted_data)
    print(f"File '{filename}' berhasil didekripsi.")

# Menu utama
def menu():
    print("\nPilih algoritma enkripsi yang ingin digunakan:")
    print("1. AES (Advanced Encryption Standard)")
    print("2. RSA (Rivest-Shamir-Adleman)")
    print("3. Blowfish")
    print("4. DES (Data Encryption Standard)")
    print("5. ChaCha20")
    print("6. ECC (Elliptic Curve Cryptography)")
    print("7. HMAC (Hash-based Message Authentication Code)")
    print("8. Post-Quantum Cryptography (Kyber)")
    print("9. Hybrid Encryption (AES + RSA)")
    print("10. Blake3 Hashing")
    print("11. Encrypt/Decrypt File")
    print("12. Keluar")

# Fitur pengimputan dan hasil yang mendetail
def get_input():
    algorithm = input("Masukkan nomor algoritma yang ingin Anda gunakan: ")

    data = input("Masukkan data yang ingin dienkripsi: ")

    if algorithm == '1':  # AES
        key = get_random_bytes(16)
        encrypted_data = aes_encrypt(key, data)
        decrypted_data = aes_decrypt(key, encrypted_data)

    elif algorithm == '2':  # RSA
        private_key = RSA.generate(2048)
        public_key = private_key.publickey().export_key()
        encrypted_data = rsa_encrypt(public_key, data)
        decrypted_data = rsa_decrypt(private_key.export_key(), encrypted_data)

    elif algorithm == '3':  # Blowfish
        key = get_random_bytes(8)
        encrypted_data = blowfish_encrypt(key, data)
        decrypted_data = blowfish_decrypt(key, encrypted_data)

    elif algorithm == '4':  # DES
        key = get_random_bytes(8)
        encrypted_data = des_encrypt(key, data)
        decrypted_data = des_decrypt(key, encrypted_data)

    elif algorithm == '5':  # ChaCha20
        key = get_random_bytes(32)
        encrypted_data = chacha20_encrypt(key, data)
        decrypted_data = chacha20_decrypt(key, encrypted_data)

    elif algorithm == '6':  # ECC
        private_key = SigningKey.generate(curve=NIST384p).to_string()
        signature = ecc_sign(private_key, data)
        decrypted_data = ecc_verify(private_key, signature, data)

    elif algorithm == '7':  # HMAC
        key = input("Masukkan kunci HMAC: ")
        hmac_result = hmac_generate(key, data)
        decrypted_data = hmac_result

    elif algorithm == '8':  # Post-Quantum Cryptography (Kyber)
        ciphertext, shared_secret = post_quantum_kyber_encrypt(data)
        decrypted_data = post_quantum_kyber_decrypt(ciphertext, shared_secret)

    elif algorithm == '9':  # Hybrid Encryption (AES + RSA)
        encrypted_aes_key, nonce, tag, ciphertext, private_key = hybrid_encrypt(data)
        decrypted_data = hybrid_decrypt(encrypted_aes_key, nonce, tag, ciphertext, private_key)

    elif algorithm == '10':  # Blake3
        hashed_data = generate_blake3_hash(data)
        decrypted_data = hashed_data

    elif algorithm == '11':  # File Encryption/Decryption
        filename = input("Masukkan nama file yang ingin dienkripsi: ")
        key = get_random_bytes(16)
        encrypt_file(filename, key)
        decrypted_data = "File telah dienkripsi dan didekripsi."

    elif algorithm == '12':  # Exit
        print("Keluar dari program.")
        return

    print(f"Data asli: {data}")
    print(f"Data yang dienkripsi: {base64.b64encode(encrypted_data).decode('utf-8')}")
    print(f"Data yang didekripsi: {decrypted_data}")

# Menjalankan menu utama
if __name__ == "__main__":
    while True:
        menu()
        get_input()
