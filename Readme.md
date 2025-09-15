# Secure Communication Using Python's Fernet Cryptography

## 📌 Overview
This project demonstrates secure communication using Python’s `cryptography.fernet` module.  
It includes:
- **Key Generation**  
- **Message Encryption (Sender GUI)**  
- **Message Decryption (Receiver GUI)**  

## 🚀 Features
- GUI for both **Sender** and **Receiver**  
- Uses **AES-128 (Fernet)** for encryption and decryption  
- Error handling for invalid/tampered data  

## 📂 Project Structure
Project/
│── gui_sender.py # Sender GUI (Encrypts messages)
│── gui_receiver.py # Receiver GUI (Decrypts messages)
│── gui_main.py # Optional main script
│── secret.key # Generated Fernet key
│── encrypted.txt # Stores encrypted messages
│── README.md # Documentation