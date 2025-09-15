# Import Fernet and InvalidToken for encryption/decryption and error handling
from cryptography.fernet import Fernet, InvalidToken

# Function to generate and save a symmetric encryption key
def generate_key():
    """Generates and saves a symmetric Fernet key."""
    key = Fernet.generate_key()  # Generate a new Fernet key (base64 encoded 32-byte key)
    with open("secret.key", "wb") as key_file:  # Open 'secret.key' in write-binary mode
        key_file.write(key)  # Write the key to the file

# Function to load the encryption key from file
def load_key():
    """Loads the encryption key from 'secret.key'."""
    try:
        with open("secret.key", "rb") as key_file:  # Try opening the key file in read-binary mode
            return key_file.read()  # Return the key content (bytes)
    except FileNotFoundError:
        return None  # If file is not found, return None (used to show an error in GUI)

# Function to encrypt a plain text message
def encrypt_message(message, key):
    """Encrypts the given message using the provided key."""
    fernet = Fernet(key)  # Create a Fernet object using the given key
    return fernet.encrypt(message.encode())  # Encode the message to bytes and encrypt it

# Function to decrypt encrypted data
def decrypt_message(encrypted_data, key):
    """Decrypts the given encrypted message using the provided key."""
    fernet = Fernet(key)  # Create a Fernet object using the provided key
    try:
        return fernet.decrypt(encrypted_data).decode()  # Try decrypting and decoding to string
    except InvalidToken:
        return None  # If the key is wrong or data is tampered with, return None
