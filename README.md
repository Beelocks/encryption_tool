# encryption_tool

1. Instalasi Dependensi
Sebelum menjalankan encryption_tool.py, pastikan Anda telah menginstal semua dependensi yang dibutuhkan. Beberapa pustaka yang digunakan dalam skrip ini, seperti PyCryptodome, ecdsa, blake3, dan pqcrypto, perlu diinstal terlebih dahulu.

Buka terminal atau command prompt, lalu instal pustaka yang diperlukan dengan menjalankan perintah berikut:

bash
Copy code
pip install pycryptodome ecdsa blake3 pqcrypto pynacl
2. Menyiapkan Skrip
Salin Kode Python:

Buka editor teks favorit Anda (misalnya, VS Code, Sublime Text, atau bahkan Notepad).
Salin kode dari encryption_tool.py yang telah diberikan sebelumnya.
Simpan Skrip:

Simpan file dengan nama encryption_tool.py pada direktori yang mudah diakses. Misalnya, di direktori C:\encryption_tool (Windows) atau /home/user/encryption_tool (Linux/Mac).
3. Menjalankan Skrip
Setelah Anda menyiapkan skrip, buka terminal atau command prompt dan arahkan ke direktori tempat Anda menyimpan encryption_tool.py.

Di Windows:
Buka Command Prompt atau PowerShell.

Arahkan ke direktori tempat skrip disimpan, misalnya:

bash
Copy code
cd C:\encryption_tool
Jalankan skrip dengan perintah:

bash
Copy code
python encryption_tool.py
Di Linux/Mac:
Buka Terminal.

Arahkan ke direktori tempat skrip disimpan, misalnya:

bash
Copy code
cd /home/user/encryption_tool
Jalankan skrip dengan perintah:

bash
Copy code
python3 encryption_tool.py
4. Menggunakan Menu Interaktif
Setelah menjalankan skrip, Anda akan melihat menu interaktif di terminal/command prompt. Menu ini memungkinkan Anda untuk memilih algoritma enkripsi yang ingin digunakan dan input data yang akan dienkripsi.

Langkah-Langkah Menggunakan Program:
Memilih Algoritma Enkripsi: Setelah skrip berjalan, Anda akan melihat daftar pilihan algoritma enkripsi. Berikut adalah contoh tampilan menu:

markdown
Copy code
Pilih algoritma enkripsi yang ingin digunakan:
1. AES (Advanced Encryption Standard)
2. RSA (Rivest-Shamir-Adleman)
3. Blowfish
4. DES (Data Encryption Standard)
5. ChaCha20
6. ECC (Elliptic Curve Cryptography)
7. HMAC (Hash-based Message Authentication Code)
8. Post-Quantum Cryptography (Kyber)
9. Hybrid Encryption (AES + RSA)
10. Blake3 Hashing
11. Encrypt/Decrypt File
12. Keluar
Memasukkan Pilihan Algoritma:

Ketik nomor algoritma yang ingin Anda pilih dan tekan Enter. Misalnya, untuk memilih AES, ketik 1 dan tekan Enter.
Memasukkan Data:

Program akan meminta Anda untuk memasukkan data yang ingin dienkripsi. Misalnya:
kotlin
Copy code
Masukkan data yang ingin dienkripsi: Hello, this is a test message!
Masukkan data yang ingin Anda enkripsi, misalnya:

kotlin
Copy code
Hello, this is a test message!
Melihat Hasil Enkripsi dan Dekripsi:

Setelah memasukkan data, program akan menampilkan hasil enkripsi dan dekripsi. Misalnya, untuk AES:
kotlin
Copy code
Data asli: Hello, this is a test message!
Data yang dienkripsi: b64_encrypted_data_here
Data yang didekripsi: Hello, this is a test message!
Hasil enkripsi akan ditampilkan dalam bentuk base64 agar mudah dibaca.

Mengulangi atau Keluar:

Setelah satu enkripsi selesai, Anda akan kembali ke menu utama dan dapat memilih algoritma lain atau keluar dari program dengan memilih 12.
5. Enkripsi File
Untuk mengenkripsi dan mendekripsi file menggunakan AES:

Pilih opsi 11. Encrypt/Decrypt File dari menu.

Program akan meminta Anda untuk memasukkan nama file yang ingin dienkripsi. Pastikan file tersebut ada di direktori yang sama dengan skrip atau masukkan path lengkapnya.

yaml
Copy code
Masukkan nama file yang ingin dienkripsi: example.txt
Program akan mengenkripsi file menggunakan AES dan menghasilkan file dengan ekstensi .enc. File yang telah dienkripsi akan disimpan di direktori yang sama.

Untuk mendekripsi file, pilih kembali opsi 11 dan masukkan nama file yang terenkripsi, misalnya example.txt.enc.

6. Keluar dari Program
Jika Anda ingin keluar dari program, cukup pilih pilihan 12 (Keluar) di menu utama.

Contoh Penggunaan:
Berikut adalah contoh interaksi dengan program:

markdown
Copy code
Pilih algoritma enkripsi yang ingin digunakan:
1. AES (Advanced Encryption Standard)
2. RSA (Rivest-Shamir-Adleman)
3. Blowfish
4. DES (Data Encryption Standard)
5. ChaCha20
6. ECC (Elliptic Curve Cryptography)
7. HMAC (Hash-based Message Authentication Code)
8. Post-Quantum Cryptography (Kyber)
9. Hybrid Encryption (AES + RSA)
10. Blake3 Hashing
11. Encrypt/Decrypt File
12. Keluar
Masukkan nomor algoritma yang ingin Anda gunakan: 1
Masukkan data yang ingin dienkripsi: Hello, this is a test message!
Data asli: Hello, this is a test message!
Data yang dienkripsi: b64_encrypted_data_here
Data yang didekripsi: Hello, this is a test message!
7. Catatan Penting:
Pastikan Anda memiliki Python 3.6 atau versi yang lebih baru.
Beberapa algoritma kriptografi, seperti Post-Quantum Cryptography (Kyber), memerlukan pustaka pihak ketiga seperti pqcrypto, yang mungkin memerlukan pengaturan tambahan.
Enkripsi file: Pastikan file yang ingin Anda enkripsi tersedia dan dapat diakses oleh skrip.
