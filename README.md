# README

## Aplikasi Kriptografi dan Steganografi dengan Python

Aplikasi ini merupakan kumpulan implementasi dari berbagai algoritma enkripsi dan steganografi, yaitu **Caesar Cipher**, **DES (Data Encryption Standard)**, **Enigma Cipher**, dan **Steganografi (LSB)**. Aplikasi ini dibuat menggunakan Python dengan antarmuka berbasis **Tkinter** dan **CustomTkinter**.

---

## Fitur Utama

1. **Caesar Cipher**
   - Algoritma enkripsi sederhana yang menggeser huruf berdasarkan nilai geser (*shift*).
   - Fitur:
     - Enkripsi teks berdasarkan nilai shift yang diberikan.
     - Dekripsi teks yang telah dienkripsi dengan shift yang sama.
     - Salin hasil ke clipboard.
     - Reset seluruh input dan output.

2. **DES (Data Encryption Standard)**
   - Algoritma enkripsi simetris menggunakan kunci 8 byte.
   - Fitur:
     - Enkripsi teks menjadi ciphertext menggunakan kunci tertentu.
     - Dekripsi ciphertext menjadi teks asli dengan kunci yang sama.
     - Salin hasil ke clipboard.
     - Reset seluruh input dan output.

3. **Enigma Cipher**
   - Implementasi sederhana dari mesin enigma untuk simulasi enkripsi dan dekripsi teks.
   - Fitur:
     - Enkripsi teks dengan pengaturan rotor yang dapat disesuaikan.
     - Dekripsi teks dengan pengaturan rotor yang sama.
     - Salin hasil ke clipboard.
     - Reset seluruh input dan output.

4. **Steganografi (LSB)**
   - Teknik menyembunyikan teks ke dalam gambar menggunakan metode **Least Significant Bit (LSB)**.
   - Fitur:
     - Enkripsi teks ke dalam gambar.
     - Dekripsi teks yang disembunyikan dalam gambar.
     - Salin hasil dekripsi ke clipboard.
     - Reset seluruh input dan output.

---

## Teknologi yang Digunakan

- **Python 3**
- **Library**:
  - `tkinter` dan `customtkinter` untuk antarmuka pengguna.
  - `Crypto` (untuk algoritma DES).
  - `stegano` (untuk steganografi LSB).
  - `pyperclip` (untuk fungsi salin ke clipboard).

---

## Instalasi

1. **Clone Repository**:
   ```bash
   git clone https://github.com/zidanmubarak/enkripsi-python.git 
   cd enkripsi-python
   ```

2. **Pasang Dependencies**:
   ```bash
   pip install tkinter customtkinter pyperclip pycryptodome stegano
   ```
