import os
import numpy as np
from PIL import Image
from tkinter import Tk, Button, Label, filedialog, messagebox, simpledialog

# Encrypt function using XOR and seeded random key-stream
def encrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        h, w, c = pixels.shape
        flat_pixels = pixels.reshape(-1, 3)

        # Use a seeded random generator based on the key
        rng = np.random.default_rng(seed=key)
        key_stream = rng.integers(0, 256, size=flat_pixels.shape, dtype=np.uint8)

        # XOR the pixels with the key-stream
        encrypted_flat = np.bitwise_xor(flat_pixels, key_stream)
        encrypted_pixels = encrypted_flat.reshape(h, w, 3)

        encrypted_image = Image.fromarray(encrypted_pixels)
        encrypted_image.save(output_path)
        messagebox.showinfo("Success", f"🔐 Image encrypted and saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

# Decrypt function using XOR and seeded random key-stream
def decrypt_image(image_path, output_path, key):
    try:
        img = Image.open(image_path).convert("RGB")
        pixels = np.array(img)

        h, w, c = pixels.shape
        flat_pixels = pixels.reshape(-1, 3)

        # Use the same key for decryption (same key-stream generation)
        rng = np.random.default_rng(seed=key)
        key_stream = rng.integers(0, 256, size=flat_pixels.shape, dtype=np.uint8)

        # XOR the encrypted pixels with the key-stream
        decrypted_flat = np.bitwise_xor(flat_pixels, key_stream)
        decrypted_pixels = decrypted_flat.reshape(h, w, 3)

        decrypted_image = Image.fromarray(decrypted_pixels)
        decrypted_image.save(output_path)
        messagebox.showinfo("Success", f"🔓 Image decrypted and saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

# GUI Actions
def on_encrypt_click():
    image_path = filedialog.askopenfilename(title="Select Image to Encrypt", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if not image_path:
        return
    save_folder = filedialog.askdirectory(title="Select Folder to Save Encrypted Image")
    if not save_folder:
        return
    key = simpledialog.askstring("Enter Key", "Enter a numeric key for encryption/decryption:")
    if not key:
        return
    try:
        key = int(key)
    except ValueError:
        messagebox.showerror("Invalid Key", "Please enter a valid numeric key.")
        return
    output_path = os.path.join(save_folder, "encrypted_image.png")
    encrypt_image(image_path, output_path, key)

def on_decrypt_click():
    image_path = filedialog.askopenfilename(title="Select Image to Decrypt", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if not image_path:
        return
    save_folder = filedialog.askdirectory(title="Select Folder to Save Decrypted Image")
    if not save_folder:
        return
    key = simpledialog.askstring("Enter Key", "Enter the numeric key used for encryption/decryption:")
    if not key:
        return
    try:
        key = int(key)
    except ValueError:
        messagebox.showerror("Invalid Key", "Please enter a valid numeric key.")
        return
    output_path = os.path.join(save_folder, "decrypted_image.png")
    decrypt_image(image_path, output_path, key)

# GUI Setup
def create_gui():
    root = Tk()
    root.title("🛡️ Image Encryptor/Decryptor")
    root.geometry("350x150")
    root.resizable(False, False)

    Label(root, text="Select an action:", font=("Arial", 14)).pack(pady=10)

    Button(root, text="🔒 Encrypt Image", font=("Arial", 12), width=20, command=on_encrypt_click).pack(pady=5)
    Button(root, text="🔓 Decrypt Image", font=("Arial", 12), width=20, command=on_decrypt_click).pack(pady=5)

    root.mainloop()

# Run the app
if __name__ == "__main__":
    create_gui()
