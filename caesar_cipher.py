import tkinter as tk
import customtkinter as ctk
import pyperclip

color = "#003049"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = caesar_encrypt(text, shift)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)

def decrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    decrypted_text = caesar_decrypt(text, shift)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", decrypted_text)

def copy_to_clipboard():
    pyperclip.copy(output_entry.get("1.0", tk.END).strip())

def reset_fields():
    text_entry.delete("1.0", tk.END)
    output_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)


app = ctk.CTk()
app.title("Caesar Cipher")
app.geometry("500x600")
app.minsize(height=700, width=550)

# ---------------------bagian container ---------------------
main_frame = ctk.CTkFrame(app, fg_color=color)
main_frame.pack(expand=True, fill="both")

# --------------------- bagian font ---------------------
font_rightheus_large = ("Righteous", 54, "bold")
font_rightheus_medium = ("Righteous", 18)
font_rightheus_small = ("Righteous", 15)

# --------------------- judul tugas ---------------------
title_label = ctk.CTkLabel(
    main_frame, 
    text="Caesar Cipher",
    font=font_rightheus_large,
    text_color="white",
    )
title_label.pack(pady=(10, 20))

# --------------------- bagian shift container ---------------------
shift_frame = ctk.CTkFrame(main_frame, fg_color=color)
shift_frame.pack(pady=(10,20))

shift_label = ctk.CTkLabel(
    shift_frame,
    text="Enter Shift : ",
    text_color="white",
    font=font_rightheus_medium,
)
shift_label.pack(side=tk.LEFT, padx=5)

shift_entry = ctk.CTkEntry(
    shift_frame,
    width=100,
    border_color="#a9ff68",
    border_width=2,
    corner_radius=10,
    text_color="white",
    font=font_rightheus_medium,
)
shift_entry.pack(pady=10)

# --------------------- bagian input text ---------------------
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
text_entry.pack(pady=(5,20))

# --------------------- tombol ekripsi & deskripsi ---------------------
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

# --------------------- bagian output ---------------------
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
output_entry.pack(pady=(5,20))

# --------------------- tombol copy & reset ---------------------
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