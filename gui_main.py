# Import tkinter for GUI components and messagebox for pop-up alerts
import tkinter as tk
from tkinter import simpledialog, messagebox
from cryptography.fernet import Fernet #Imports the Fernet
from cryptography.fernet import InvalidToken


def generate_key():
    try:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        messagebox.showinfo("Success", "Key generated and saved as 'secret.key'.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate key:\n{e}")

def load_key():
    """Loads the encryption key from 'secret.key'."""
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "'secret.key' file not found. Please generate a key first.")
        return None

def encrypt_message():
    key = load_key()  # Load the encryption key from 'secret.key'
    if not key:
        return  # If key is not found or loading failed, stop here

    def on_encrypt():
        # Get the message from the Text widget (multi-line input)
        message = text_input.get("1.0", tk.END).strip()
        if message:
            try:
                fernet = Fernet(key)  # Create Fernet object with the loaded key
                encrypted = fernet.encrypt(message.encode())  # Encrypt the message
                with open("encrypted.txt", "wb") as enc_file:  # Save to file
                    enc_file.write(encrypted)
                messagebox.showinfo("Success", "Message encrypted and saved as 'encrypted.txt'.")
                input_window.destroy()  # Close the input window after success
            except Exception as e:
                messagebox.showerror("Error", f"Encryption failed:\n{e}")  # Show error if encryption fails
        else:
            messagebox.showwarning("Warning", "Message box is empty.")  # Warn if input is empty

    # Create a new top-level window (popup) on top of the main GUI
    input_window = tk.Toplevel(window)
    input_window.title("Enter Message to Encrypt")  # Set the title of the popup
    input_window.geometry("400x250")  # Set the size of the popup window
    input_window.resizable(False, False)  # Make it non-resizable

    # Label to instruct the user
    tk.Label(input_window, text="Enter your message:").pack(pady=10)

    # Create a multi-line Text box for entering the message
    text_input = tk.Text(input_window, height=6, width=45)
    text_input.pack()

    # Create a button inside the popup to trigger encryption
    encrypt_btn = tk.Button(input_window, text="Encrypt", command=on_encrypt)
    encrypt_btn.pack(pady=10)
    
def decrypt_message():
    key = load_key()
    if not key:
        return

    try:
        with open("encrypted.txt", "rb") as enc_file:
            encrypted_data = enc_file.read()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_data).decode()
        messagebox.showinfo("Decrypted Message", decrypted)
    except FileNotFoundError:
        messagebox.showerror("Error", "'encrypted.txt' not found. Please encrypt a message first.")
    except InvalidToken:
        messagebox.showerror("Error", "Invalid key or tampered message.")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{e}")


# Create the main application window
window = tk.Tk()  # Initialize the main GUI window
window.title("The Secure Communication with Fernet")  # Set window title
window.geometry("400x300")  # Set fixed window size: 400 pixels wide, 300 pixels tall
window.resizable(False, False)  # Prevent resizing horizontally and vertically

# Add a title label at the top of the window
title_label = tk.Label(
    window,  # Parent widget
    text=" The Secure Communication App",  # Displayed text
    font=("Times New Roman", 16, "bold")  # Font styling: Arial, size 16, bold
)
title_label.pack(pady=20)  # Place the label with 20 pixels of vertical padding

# Add a button for generating the encryption key
generate_key_button = tk.Button(
    window,  # Parent widget
    text="Generate Encryption Key",  # Button label
    width=30,  # Button width (in text units)
    command=generate_key
)
generate_key_button.pack(pady=10)  # Place the button with vertical spacing

# Add a button for encrypting a message
encrypt_button = tk.Button(
    window,
    text="Encrypt Message",
    width=30,
    command=encrypt_message
)
encrypt_button.pack(pady=10)

# Add a button for decrypting a message
decrypt_button = tk.Button(
    window,
    text="Decrypt Message",
    width=30,
    command=decrypt_message
    # command will be added later
)
decrypt_button.pack(pady=10)

# Add an Exit button that closes the application
exit_button = tk.Button(
    window,
    text="Exit",
    width=30,
    command=window.quit  # Calls the built-in method to exit the GUI loop
)
exit_button.pack(pady=10)

# Start the GUI event loop (keeps the window open and responsive)
window.mainloop()
