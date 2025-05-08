# Task 2: Image Encryption Tool with Pixel Manipulation

## Overview

This project demonstrates a basic **image encryption and decryption** system using **pixel manipulation with XOR operation** and a **key-based pseudo-random stream**. The program also features a user-friendly **GUI using Tkinter** for ease of use.

---

## 🔐 Features

- Encrypt and decrypt any `.jpg`, `.jpeg`, `.png`, or `.bmp` image
- Uses XOR encryption with a seeded random number stream
- Simple Tkinter-based GUI
- Prompt for a numeric key to ensure repeatable encryption/decryption

---

## 🛠️ How It Works

- **Encryption**:
  - Image pixels are converted to a NumPy array.
  - A key-stream is generated using a user-provided numeric key.
  - Each pixel is XORed with the key-stream for encryption.

- **Decryption**:
  - The same process is reversed using the same numeric key.

> 🔑 Note: The same key **must** be used for both encryption and decryption.

---

## 📦 Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `Pillow`
  - `tkinter` (built-in with Python)

To install missing dependencies:

```bash
pip install numpy Pillow
```

---

## 🚀 How to Run

Run the script using:

```bash
python image_encryptor.py
```

The GUI will launch with options to encrypt or decrypt an image.

---

## 🎨 UI

- Minimal and responsive GUI
- Icons:
  - 🔒 Encrypt
  - 🔓 Decrypt
- Prompts for image selection, save location, and key input

---

## 👨‍💻 Developed By

**Sneha K M**  
_ProDigy Infotech Internship Project_

---

## ⚠️ Disclaimer

This is a simple educational tool and should **not** be used for serious image security or cryptographic purposes.

