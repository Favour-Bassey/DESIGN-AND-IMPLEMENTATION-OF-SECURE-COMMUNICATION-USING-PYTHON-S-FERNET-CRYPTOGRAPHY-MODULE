# THE eceiver_gui.py

# Import necessary modules
import tkinter as tk  # Used to create GUI windows and widgets
from tkinter import messagebox  # Used to display popup message alerts (error/success)
from crypto_utils import load_key, decrypt_message  # Import utility functions from crypto_utils.py

# Define the function to handle decryption
def handle_decrypt():
    key = load_key()  # Load the symmetric key from the file 'secret.key'
    if not key:  # If no key is returned (e.g. file not found)
        messagebox.showerror("Error", "Encryption key not found. Please ensure 'secret.key' exists.")  # Show error
        return  # Exit the function early if key loading fails

    try:
        # Attempt to read the encrypted data from file
        with open("encrypted.txt", "rb") as file:  # Open the file in binary mode
            encrypted_data = file.read()  # Read all encrypted bytes
    except FileNotFoundError:
        messagebox.showerror("Error", "Encrypted file not found. Please ensure 'encrypted.txt' exists.")  # Show error
        return  # Exit the function if file doesn't exist

    # Try to decrypt the loaded encrypted data using the key
    decrypted = decrypt_message(encrypted_data, key)  # Returns None if invalid key or corrupt data
    if decrypted is None:  # If decryption failed
        messagebox.showerror("Decryption Failed", "Invalid key or corrupted encrypted file.")  # Show error popup
    else:
        # If decryption is successful, show the decrypted message in the textbox
        output_box.config(state="normal")  # Temporarily enable the textbox to modify it
        output_box.delete("1.0", tk.END)  # Clear any previous content from the textbox
        output_box.insert(tk.END, decrypted)  # Insert the decrypted message into the textbox
        output_box.config(state="disabled")  # Set the textbox back to read-only mode

# ---------- Build the GUI layout ----------

window = tk.Tk()
window.title("Receiver - Secure Communication")
window.geometry("500x350")
window.resizable(False, False)
window.configure(bg="#1e1e2f")  # Set dark navy background

# Title label
title = tk.Label(
    window,
    text="Receiver Interface",
    font=("Helvetica", 16, "bold"),
    fg="#ffffff",  # White text
    bg="#1e1e2f"   # Match background
)
title.pack(pady=10)

# Decrypt button
decrypt_btn = tk.Button(
    window,
    text="Load and Decrypt Message",
    width=35,
    command=handle_decrypt,
    bg="#007acc",   # Button background
    fg="white",     # Button text
    activebackground="#005a99",  # Darker on click
    relief="flat"
)
decrypt_btn.pack(pady=10)

# Output label
output_label = tk.Label(
    window,
    text="Decrypted Message:",
    fg="white",
    bg="#1e1e2f",
    font=("Helvetica", 10, "bold")
)
output_label.pack(pady=5)

# Output box for decrypted text
output_box = tk.Text(
    window,
    height=8,
    width=60,
    state="disabled",
    bg="#2e2e3f",      # Slightly lighter than window
    fg="#00ffcc",      # Aqua green text
    insertbackground="white",  # Cursor color
    relief="sunken",
    borderwidth=2
)
output_box.pack()

# Exit button
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