import tkinter as tk
import customtkinter as ctk
import pyperclip
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# --------------------- Konfigurasi Tampilan ---------------------
color = "#003049"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

font_rightheus_large = ("Righteous", 54, "bold")
font_rightheus_medium = ("Righteous", 18)
font_rightheus_small = ("Righteous", 15)

# --------------------- Fungsi Pad & Unpad untuk DES ---------------------
def pad(text):
    """Fungsi untuk padding agar panjang text kelipatan 8 byte."""
    while len(text) % 8 != 0:
        text += ' '
    return text

def encrypt_des(key, text):
    """Fungsi untuk mengenkripsi teks menggunakan DES."""
    text = pad(text)  # Padding teks
    cipher = DES.new(key, DES.MODE_ECB)  # Membuat objek DES dengan mode ECB
    encrypted_text = cipher.encrypt(text.encode('utf-8'))  # Enkripsi teks
    return base64.b64encode(encrypted_text).decode('utf-8')  # Encode ke base64

def decrypt_des(key, encrypted_text):
    """Fungsi untuk mendekripsi teks menggunakan DES."""
    encrypted_text = base64.b64decode(encrypted_text)  # Decode dari base64
    cipher = DES.new(key, DES.MODE_ECB)  # Membuat objek DES dengan mode ECB
    decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8').rstrip()  # Dekripsi teks
    return decrypted_text

# --------------------- Fungsi Aksi Tombol ---------------------
key = get_random_bytes(8)  # Kunci DES harus 8 byte

def encrypt_text():
    """Fungsi untuk mengenkripsi teks dan menampilkannya di output."""
    text = text_entry.get("1.0", tk.END).strip()
    encrypted_text = encrypt_des(key, text)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)

def decrypt_text():
    """Fungsi untuk mendekripsi teks terenkripsi dan menampilkannya di output."""
    encrypted_text = text_entry.get("1.0", tk.END).strip()
    try:
        decrypted_text = decrypt_des(key, encrypted_text)
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", decrypted_text)
    except Exception as e:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", f"Error: {str(e)}")

def copy_to_clipboard():
    """Fungsi untuk menyalin output ke clipboard."""
    pyperclip.copy(output_entry.get("1.0", tk.END).strip())

def reset_fields():
    """Fungsi untuk mereset semua input dan output."""
    text_entry.delete("1.0", tk.END)
    output_entry.delete("1.0", tk.END)

# --------------------- UI Aplikasi ---------------------
app = ctk.CTk()
app.title("DES Cipher")
app.geometry("500x600")
app.minsize(height=650, width=500)

# Container Utama
main_frame = ctk.CTkFrame(app, fg_color=color)
main_frame.pack(expand=True, fill="both")

# Judul Aplikasi
title_label = ctk.CTkLabel(
    main_frame, 
    text="DES Cipher",
    font=font_rightheus_large,
    text_color="white",
)
title_label.pack(pady=(10, 20))

# Input Text
text_label = ctk.CTkLabel(
    main_frame,
    text="Enter Your Text",
    font=font_rightheus_medium,
    text_color="white",
)
text_label.pack(pady=(10, 5))

text_entry = ctk.CTkTextbox(
    main_frame,
    width=400,
    height=100,
    border_color="#a9ff68",
    border_width=2,
    corner_radius=10,
    font=font_rightheus_medium,
    text_color="white",
)
text_entry.pack(pady=(5, 20))

# Tombol Encrypt dan Decrypt
button_frame = ctk.CTkFrame(main_frame, fg_color=color)
button_frame.pack(pady=(10, 20))

encrypt_button = ctk.CTkButton(
    button_frame,
    text="Encrypt",
    width=100,
    height=32,
    font=font_rightheus_small,
    fg_color="#ffa400",
    hover_color="#e59400",
    border_color="#a9ff68",
    border_width=2,
    text_color="black",
    command=encrypt_text,
    corner_radius=15,
)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = ctk.CTkButton(
    button_frame,
    text="Decrypt",
    width=100,
    height=32,
    font=font_rightheus_small,
    fg_color="#ffa400",
    hover_color="#e59400",
    border_color="#a9ff68",
    border_width=2,
    text_color="black",
    command=decrypt_text,
    corner_radius=15,
)
decrypt_button.grid(row=0, column=1, padx=10)

# Output
output_label = ctk.CTkLabel(
    main_frame,
    text="Output Text",
    font=font_rightheus_medium,
    text_color="white",
)
output_label.pack(pady=(20, 5))

output_entry = ctk.CTkTextbox(
    main_frame,
    width=400,
    height=100,
    border_color="#a9ff68",
    border_width=2,
    corner_radius=10,
    font=font_rightheus_medium,
    text_color="white",
)
output_entry.pack(pady=(5, 20))

# Tombol Copy dan Reset
reset_button = ctk.CTkButton(
    main_frame,
    text="Copy",
    width=100,
    height=32,
    font=font_rightheus_small,
    fg_color="#ffa400",
    hover_color="#e59400",
    border_color="#a9ff68",
    border_width=2,
    text_color="black",
    command=copy_to_clipboard,
    corner_radius=15,
)
reset_button.pack(pady=(5, 10))

copy_button = ctk.CTkButton(
    main_frame,
    text="Reset",
    width=100,
    height=32,
    font=font_rightheus_small,
    fg_color="#ffa400",
    hover_color="#e59400",
    border_color="#a9ff68",
    border_width=2,
    text_color="black",
    command=reset_fields,
    corner_radius=15,
)
copy_button.pack(pady=(10, 5))

app.mainloop()
