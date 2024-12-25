import tkinter as tk
import customtkinter as ctk
import pyperclip
from stegano import lsb
import os

# --------------------- Konfigurasi Tampilan ---------------------
color = "#003049"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

font_rightheus_large = ("Righteous", 54, "bold")
font_rightheus_medium = ("Righteous", 18)
font_rightheus_small = ("Righteous", 15)

# --------------------- Fungsi Algoritma Steganografi ---------------------
def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    image_path = file_entry.get().strip()
    if os.path.exists(image_path) and text:
        try:
            output_path = "output_image.png"
            lsb.hide(image_path, text).save(output_path)
            output_entry.delete("1.0", tk.END)
            output_entry.insert("1.0", f"Teks berhasil disisipkan di '{output_path}'")
        except Exception as e:
            output_entry.delete("1.0", tk.END)
            output_entry.insert("1.0", f"Error: {e}")
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", "Masukkan gambar valid dan teks!")

def decrypt_text():
    image_path = file_entry.get().strip()
    if os.path.exists(image_path):
        try:
            hidden_text = lsb.reveal(image_path)
            output_entry.delete("1.0", tk.END)
            if hidden_text:
                output_entry.insert("1.0", hidden_text)
            else:
                output_entry.insert("1.0", "Tidak ada teks tersembunyi di gambar!")
        except Exception as e:
            output_entry.delete("1.0", tk.END)
            output_entry.insert("1.0", f"Error: {e}")
    else:
        output_entry.delete("1.0", tk.END)
        output_entry.insert("1.0", "Masukkan gambar valid!")

def copy_to_clipboard():
    pyperclip.copy(output_entry.get("1.0", tk.END).strip())

def reset_fields():
    text_entry.delete("1.0", tk.END)
    output_entry.delete("1.0", tk.END)
    file_entry.delete(0, tk.END)

# --------------------- UI Aplikasi ---------------------
app = ctk.CTk()
app.title("Steganography")
app.geometry("500x700")
app.minsize(height=700, width=550)

# Container Utama
main_frame = ctk.CTkFrame(app, fg_color=color)
main_frame.pack(expand=True, fill="both")

# Judul Aplikasi
title_label = ctk.CTkLabel(
    main_frame,
    text="Steganography",
    font=font_rightheus_large,
    text_color="white",
)
title_label.pack(pady=(10, 20))

# Input Path Gambar
file_label = ctk.CTkLabel(
    main_frame,
    text="Path Gambar:",
    font=font_rightheus_medium,
    text_color="white",
)
file_label.pack(pady=(10, 5))

file_entry = ctk.CTkEntry(
    main_frame,
    width=400,
    border_color="#a9ff68",
    border_width=2,
    corner_radius=10,
    font=font_rightheus_small,
    text_color="white",
)
file_entry.pack(pady=(5, 20))

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
    font=font_rightheus_small,
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
    command=decrypt_text,
    corner_radius=15,
)
decrypt_button.grid(row=0, column=1, padx=10)

# Output
output_label = ctk.CTkLabel(
    main_frame,
    text="Output",
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
    font=font_rightheus_small,
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
    command=reset_fields,
    corner_radius=15,
)
copy_button.pack(pady=(10, 5))

app.mainloop()
