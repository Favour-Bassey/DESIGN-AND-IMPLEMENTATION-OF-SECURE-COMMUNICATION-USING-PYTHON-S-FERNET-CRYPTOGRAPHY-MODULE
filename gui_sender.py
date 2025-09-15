# sender_gui.py (themed version)

import tkinter as tk
from tkinter import messagebox
from Project.crypto_utils import generate_key, load_key, encrypt_message

# Function to handle encryption
def handle_encrypt():
    key = load_key()
    if not key:
        messagebox.showerror("Error", "Key not found. Please generate a key first.")
        return

    message = input_box.get("1.0", tk.END).strip()
    if not message:
        messagebox.showwarning("Warning", "Message field is empty.")
        return

    try:
        encrypted = encrypt_message(message, key)
        with open("encrypted.txt", "wb") as file:
            file.write(encrypted)
        messagebox.showinfo("Success", "Message encrypted and saved as 'encrypted.txt'.")
        input_box.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed:\n{e}")

# Function to handle key generation
def handle_key_generation():
    try:
        generate_key()
        messagebox.showinfo("Success", "Key generated and saved as 'secret.key'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate key:\n{e}")

# ----------- GUI Setup -----------
window = tk.Tk()
window.title("Sender - Secure Communication")
window.geometry("500x400")
window.resizable(False, False)
window.configure(bg="#1e1e2f")  # Dark navy background

# Title
title_label = tk.Label(
    window,
    text="Sender Interface",
    font=("Helvetica", 16, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title_label.pack(pady=10)

# Generate Key Button
key_btn = tk.Button(
    window,
    text="Generate Encryption Key",
    width=35,
    command=handle_key_generation,
    bg="#007acc",
    fg="white",
    activebackground="#005a99",
    relief="flat"
)
key_btn.pack(pady=8)

# Message Label
msg_label = tk.Label(
    window,
    text="Enter Message to Encrypt:",
    font=("Helvetica", 10, "bold"),
    fg="white",
    bg="#1e1e2f"
)
msg_label.pack(pady=5)

# Multi-line Text Input
input_box = tk.Text(
    window,
    height=8,
    width=60,
    bg="#2e2e3f",
    fg="#00ffcc",
    insertbackground="white",
    relief="sunken",
    borderwidth=2
)
input_box.pack()

# Encrypt Button
encrypt_btn = tk.Button(
    window,
    text="Encrypt and Save Message",
    width=35,
    command=handle_encrypt,
    bg="#007acc",
    fg="white",
    activebackground="#005a99",
    relief="flat"
)
encrypt_btn.pack(pady=10)

# Exit Button
exit_btn = tk.Button(
    window,
    text="Exit",
    width=35,
    command=window.quit,
    bg="#007acc",
    fg="white",
    activebackground="#005a99",
    relief="flat"
)
exit_btn.pack(pady=10)

# Run the GUI
window.mainloop()
