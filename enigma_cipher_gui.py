import tkinter as tk
import customtkinter as ctk
import pyperclip

# --------------------- Konfigurasi Tampilan ---------------------
color = "#003049"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

font_rightheus_large = ("Righteous", 54, "bold")
font_rightheus_medium = ("Righteous", 18)
font_rightheus_small = ("Righteous", 15)

# --------------------- Implementasi Enigma Cipher ---------------------
# Rotor substitusi (Enigma rotors)
rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

# Reflektor substitusi
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def rotate_rotor(rotor, n):
    """Rotasi rotor sebanyak n langkah."""
    return rotor[n:] + rotor[:n]

def enigma_encrypt(text, rotor1_pos=0, rotor2_pos=0, rotor3_pos=0):
    """Fungsi untuk mengenkripsi teks menggunakan Enigma Cipher."""
    encrypted_text = ""
    rotor1, rotor2, rotor3 = rotor_1, rotor_2, rotor_3

    for char in text.upper():
        if char.isalpha():  # Proses hanya huruf
            # Rotasi rotor setiap input
            rotor1_pos = (rotor1_pos + 1) % 26
            rotor1 = rotate_rotor(rotor_1, rotor1_pos)

            if rotor1_pos % 26 == 0:  # Rotor kedua berputar
                rotor2_pos = (rotor2_pos + 1) % 26
                rotor2 = rotate_rotor(rotor_2, rotor2_pos)

                if rotor2_pos % 26 == 0:  # Rotor ketiga berputar
                    rotor3_pos = (rotor3_pos + 1) % 26
                    rotor3 = rotate_rotor(rotor_3, rotor3_pos)

            # Substitusi melalui rotor
            index = ord(char) - ord('A')
            char = rotor1[index]
            index = ord(char) - ord('A')
            char = rotor2[index]
            index = ord(char) - ord('A')
            char = rotor3[index]

            # Reflektor
            index = ord(char) - ord('A')
            char = reflector[index]

            # Kembali melalui rotor secara terbalik
            index = rotor3.index(char)
            char = chr(index + ord('A'))
            index = rotor2.index(char)
            char = chr(index + ord('A'))
            index = rotor1.index(char)
            char = chr(index + ord('A'))

            encrypted_text += char
        else:
            encrypted_text += char  # Tambahkan karakter non-huruf tanpa perubahan
    return encrypted_text

# --------------------- Fungsi Aksi Tombol ---------------------
def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    encrypted_text = enigma_encrypt(text)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)

def decrypt_text():
    """Enigma bersifat simetris, jadi enkripsi dan dekripsi menggunakan fungsi sama."""
    encrypt_text()

def copy_to_clipboard():
    pyperclip.copy(output_entry.get("1.0", tk.END).strip())

def reset_fields():
    text_entry.delete("1.0", tk.END)
    output_entry.delete("1.0", tk.END)

# --------------------- UI Aplikasi ---------------------
app = ctk.CTk()
app.title("Enigma Cipher")
app.geometry("500x600")
app.minsize(height=650, width=500)

# Container Utama
main_frame = ctk.CTkFrame(app, fg_color=color)
main_frame.pack(expand=True, fill="both")

# Judul Aplikasi
title_label = ctk.CTkLabel(
    main_frame, 
    text="Enigma Cipher",
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
